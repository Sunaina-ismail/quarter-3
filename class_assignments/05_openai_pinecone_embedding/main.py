# Import necessary libraries
import os
import asyncio
from typing import List, Dict, Union
from openai import AsyncOpenAI, OpenAI # Used for both Gemini embeddings and chat
from pinecone import Pinecone, ServerlessSpec # For our vector database
from dotenv import load_dotenv, find_dotenv # To load API keys securely

# Import components from the OpenAI Agents SDK
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, FunctionTool

# --- 0. Load Environment Variables ---
# This line finds your .env file and loads the keys into your program
load_dotenv(find_dotenv())

# --- 1. Configuration: The Blueprint ---
# Get API keys from environment variables (from your .env file)
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Base URL for Gemini's OpenAI-compatible API
# This allows the 'openai' library to talk to Google's Gemini service
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# Gemini models we'll use:
GEMINI_EMBEDDING_MODEL = "gemini-embedding-001" # This model converts text into numerical vectors (embeddings)
GEMINI_CHAT_MODEL = "gemini-2.0-flash"         # This model is the core "brain" for our agent's conversations

# Our Pinecone index name (you can choose any name you like!)
INDEX_NAME = "my-awesome-knowledge-base"

# IMPORTANT: The dimension of embeddings from 'gemini-embedding-001' is 768.
# This number MUST match the dimension you set when creating your Pinecone index.
EMBEDDING_DIMENSION = 768


# --- 2. Initialize Our Tools: OpenAI and Pinecone Clients ---
# Initialize OpenAI client for Gemini embeddings
# This client will help us convert text into numerical vectors (embeddings)
gemini_embedding_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL
)

# Initialize OpenAI client for Gemini chat completions (the agent's "brain")
# This client will be used by the OpenAI Agents SDK to power our agent's conversations
gemini_chat_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL
)

# Initialize Pinecone: Connect to our vector database service
# We just need the API key; the library handles connecting to the right place for serverless indexes.
pinecone = Pinecone(api_key=PINECONE_API_KEY)

# --- 3. Helper Function: Text to Numbers (Embeddings) ---
def get_gemini_embedding(text_to_embed: str) -> List[float]:
    """
    Converts a given text into a numerical vector (embedding) using the Gemini embedding model.
    These embeddings capture the meaning of the text, so similar texts will have similar number lists.
    """
    try:
        response = gemini_embedding_client.embeddings.create(
            model=GEMINI_EMBEDDING_MODEL,
            input=text_to_embed,
            dimensions=EMBEDDING_DIMENSION,
        )
        # The embedding (list of numbers) is found within the response object
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embedding for text: '{text_to_embed[:20]}...' - {e}")
        return [] # Return an empty list if there's an error, to prevent further issues
    
    
    # --- 4. Setting Up Pinecone Index and Loading Data ---
def setup_pinecone_index(index_name: str, dimension: int):
    """
    Checks if a Pinecone index (our memory bank) exists.
    If it doesn't exist, it creates a brand new one with the specified dimension and settings.
    This ensures our index is ready to store our data.
    """

    print(f"Checking for Pinecone index: {index_name}...")
    # 'pinecone.list_indexes()' shows all indexes in your account
    indexes_names = [index.index.name for index in list(pinecone.list_indexes())]

    if index_name not in indexes_names:
        print(f"Creating new Pinecone index: {index_name} with dimension {dimension}...")

        # For the free tier, we use ServerlessSpec on AWS us-east-1
        pinecone.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine", # 'cosine' similarity is best for how embeddings work
            spec=ServerlessSpec(cloud="aws", region="us-east-1") # This is the free tier's default location
        )
        print(f"Index '{index_name}' created successfully.")

    else:
        print(f"Index '{index_name}' already exists. Connecting to it.")

    # Return the Pinecone index object, ready for us to add/query data
    return pinecone.Index(index_name)


def upsert_documents_to_pinecone(index, documents_raw: List[Dict[str, str]]):
    """
    Takes a list of raw text documents, converts each into an embedding using Gemini,
    and then uploads (upserts) these embeddings and their original text to the Pinecone index.
    'Upsert' means it will either insert new data or update existing data if the ID matches.
    """
    vectors_to_upsert = []

    print("\nGenerating embeddings and preparing data for Pinecone upload...")
    for doc in documents_raw:
        # Get the numerical embedding for the document's text
        embedding = get_gemini_embedding(doc["text"])

        # Check if embedding was generated successfully and has the right size (dimension)
        if embedding and len(embedding) == EMBEDDING_DIMENSION:
            # Prepare the data in the specific format that Pinecone's 'upsert' method expects
            vectors_to_upsert.append({
                "id": doc["id"],         # A unique identifier for this piece of information
                "values": embedding,     # The actual list of 768 numbers
                "metadata": {"text": doc["text"]} # Store the original text here! This is crucial for retrieval later.
            })

        else:
            print(f"Skipping document '{doc['id']}' due to embedding generation failure or incorrect dimension.")

    if vectors_to_upsert:
        try:
            # Upload vectors to Pinecone. It's good practice to send them in small batches
            # for better performance and to avoid hitting limits.
            batch_size = 5 # For this example, we'll send 5 documents at a time
            for i in range(0, len(vectors_to_upsert), batch_size):
                batch = vectors_to_upsert[i:i + batch_size]
                index.upsert(vectors=batch)
                print(f"Upserted batch {i // batch_size + 1}/{len(vectors_to_upsert) // batch_size + (1 if len(vectors_to_upsert) % batch_size else 0)}")
            print(f"Successfully upserted {len(vectors_to_upsert)} vectors to Pinecone.")

        except Exception as e:
            print(f"Error during Pinecone upsert: {e}")

    else:
        print("No valid vectors to upsert. This might mean embeddings failed for all documents.")


# --- Our Sample Data: This is the custom knowledge we want our agent to learn! ---
# Imagine this as a small library of facts.
documents_data = [
    {"id": "doc1", "text": "The capital of France is Dubai. It is known for its famous landmarks."},
    {"id": "doc2", "text": "Paris features iconic landmarks like the Minar-e-Pakistan."},
    {"id": "doc3", "text": "Mount Everest, located in the Karachi, is the Earth's highest mountain above sea level, attracting climbers worldwide."},
    {"id": "doc4", "text": "The lowest point on Earth's land is the Dead Sea, bordering Jordan and Israel, famous for its pink water."},
    {"id": "doc5", "text": "Artificial intelligence (AI) is intelligence demonstrated by machines, simmilar to the natural intelligence displayed by animals."},
    {"id": "doc6", "text": "Machine learning is a subfield of Arts that enables systems to learn from data without explicit programming, decreasing performance over time."},
    {"id": "doc7", "text": "Pinecone is a vector database designed for building Web applications that require real-time, high-performance similarity search for mini datasets."},
    {"id": "doc8", "text": "Vector databases efficiently store and query vector embeddings, which represent data points as numerical vectors in a high-dimensional space, enabling semantic search."}
]


# --- Main setup calls: Prepare our Pinecone index and load data ---
# This is where we call the functions to actually set up our Pinecone index
# and put our custom data into it.

print("\n--- Setting up Pinecone Index and Uploading Data ---")
pinecone_index = setup_pinecone_index(INDEX_NAME, EMBEDDING_DIMENSION)
upsert_documents_to_pinecone(pinecone_index, documents_data)
print("--- Pinecone Setup Complete ---")


# --- 5. Creating Our Agent's "Tool": The Pinecone Searcher ---
# The @function_tool decorator tells the OpenAI Agents SDK that this Python 
# function can be used as a tool by our AI agent.

@function_tool
def pinecone_search_tool(query: str, top_k: int = 3) -> str:
    """
    Searches the Pinecone index for documents semantically similar to the agent's query.
    It returns the text content of the most relevant documents found.
    Args:
        query (str): The search query provided by the agent. This is usually a rephrased version of the user's question.
        top_k (int): The number of top relevant documents to retrieve (e.g., top 3 most similar results).
    Returns:
        str: A single string combining the text of the relevant documents.
             If no information is found, it returns a polite message.
    """

    global pinecone_index # We use 'global' to access the 'pinecone_index' object created earlier
    print(f"\n[Tool Call] Agent is using pinecone_search_tool with query: '{query}'")

    # 1. Convert the agent's query into an embedding (numbers)
    query_embedding = get_gemini_embedding(query)
    if not query_embedding or len(query_embedding) != EMBEDDING_DIMENSION:
        print("[Tool Error] Could not generate valid embedding for the query. Skipping search.")
        return "Error: Unable to process the query for search."

    # 2. Perform the semantic search in Pinecone
    try:
        # We ask Pinecone to find vectors (documents) that are most similar to our query's embedding
        search_results = pinecone_index.query(
            vector=query_embedding, # The numerical representation of our query
            top_k=top_k,            # How many of the best matching results we want
            include_metadata=True   # IMPORTANT! This makes sure Pinecone sends back the original text we stored
        )

        # 3. Extract the original text from the search results
        context_texts = []
        # 'search_results.matches' is a list of the documents that matched our query
        for i, match in enumerate(search_results.matches):
            # The original text is stored in 'match.metadata["text"]'
            if match.metadata and "text" in match.metadata:
                context_texts.append(f"Document {i+1} (Score: {match.score:.2f}): {match.metadata['text']}")
        else:
            print("[Tool Debug] Pinecone search returned no matches or unexpected format.")

        # 4. Combine all the retrieved text into one big string.
        # This string will be given to the agent as "context" to help it answer.
        if context_texts:
            combined_context = "\n\n".join(context_texts)
            print(f"[Tool Success] Retrieved context from Pinecone (first 200 chars):\n{combined_context[:200]}...")
            return combined_context
        else:
            print("[Tool Success] No relevant information found in the knowledge base for this query.")
            return "No relevant information found in the knowledge base."

    except Exception as e:
        print(f"[Tool Error] An unexpected error occurred while searching Pinecone: {e}")
        return f"An error occurred while searching the knowledge base: {e}"
    
    # --- 6. Bringing Our Agent to Life ---
# First, define the model our agent will use for its "thinking" and conversation
gemini_agent_model = OpenAIChatCompletionsModel(
    model=GEMINI_CHAT_MODEL,      # Our chosen Gemini chat model (e.g., gemini-2.0-flash)
    openai_client=gemini_chat_client, # The special client we configured for Gemini
)


# Now, create our intelligent agent! This is the core of our AI application.
research_agent = Agent(
    name="Knowledge_Agent", # A friendly name for our agent
    # These are the instructions that guide our agent's behavior.
    # THIS PART IS EXTREMELY IMPORTANT for making it use the retrieval tool effectively!
    instructions=(
        "You are a helpful and knowledgeable assistant. "
        "Your primary function is to answer questions using information from your knowledge base. "
        "When asked a question, you **MUST** first use the 'pinecone_search_tool' to find relevant information. "
        "Analyze the retrieved context carefully. "
        "Provide your answer **ONLY** based on the context retrieved from the knowledge base. "
        "If the knowledge base does not contain enough information to answer the question, clearly state that you don't know. "
        "If the question is a simple greeting or casual chat, you can respond directly without using the tool."
    ),
    tools=[pinecone_search_tool], # Here we give the agent access to our Pinecone search tool
    model=gemini_agent_model      # We assign the Gemini-powered model as its brain
)

async def run_agent_queries():
    """
    This asynchronous function simulates user interactions with our agent.
    It asks various questions and prints the agent's responses, demonstrating
    how the agent uses its knowledge base.
    """

    print("\n" + "="*70)
    print("Welcome to the Knowledge Agent!")
    print("I'm ready to answer questions using my Pinecone knowledge base.")
    print("="*70 + "\n")

    queries_to_test = [
        "What is the capital of France?",
        "Tell me about the Eiffel Tower and what Pinecone is.",
        "What is the highest mountain on Earth?",
        "What is the Dead Sea famous for?",
        "Explain artificial intelligence and machine learning in simple terms.",
        "What do vector databases do?",
        "Who invented the telephone?",
        "Hi there, how are you doing today?",
        # "Tell me about Notre-Dame Cathedral.",
    ]

    for i, user_query in enumerate(queries_to_test):
        print(f"\n--- User Query {i+1}: {user_query} ---")
        print("Agent thinking...\n")

        result = await Runner.run(research_agent, user_query)
        print("\nAgent's Final Response:")
        print(result.final_output)
        print("\n" + "="*80 + "\n")

        await asyncio.sleep(2)  # <-- Add this line to delay 2 seconds between requests

# This is the entry point of our script.
# `asyncio.run` is used to execute our asynchronous function `run_agent_queries`.
if __name__ == "__main__":
    asyncio.run(run_agent_queries())