import os
import asyncio
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, Agent
from agents.run import RunConfig
import chainlit as cl

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

# Web-dev agent
web_dev_agent = Agent(
    name="Web_dev_agent",
    instructions="You are a web developer agent. Help the user with anything related to websites, frontend, or backend development.",
    model=model
)

# mobile agent
mobile_agent = Agent(
    name="Mobile_agent",
    instructions="You are a mobile app agent. Assist with topics like Android, iOS, Flutter, or React Native.",
    model=model
)
 
# marketing agent 
marketing_agent = Agent(
    name="Marketing_agent",
    instructions="You are a marketing agent. Help the user with digital marketing, branding, and promotion strategies.",
    model=model
)

# manager agent
triage_agent = Agent(
    name="Triage agent",
    instructions="""
You are a smart manager agent responsible for routing queries to the correct specialized agent.

Rules:
- Do NOT answer technical questions yourself.
- For questions related to **Web development**, **Mobile App development**, or **Marketing**, route the query to the appropriate agent using handoff.
- If the query mentions more than one topic (like both web development and marketing), politely respond with:
  "Please ask about **one topic at a time**: Web development, Mobile App development, or Marketing."
- Only respond directly to greetings or casual social messages like "hi", "hello", or "how are you" with a friendly message such as:
  "Hello! How can I assist you with Web development, Mobile App development, or Marketing today?"
- If the question is outside these topics, or asks for personal information (e.g. name, address, phone), respond with:
  "Sorry, I cannot provide or handle any personal information. I am designed only to assist with Web development, Mobile App development, or Marketing questions."
"""
,
    handoffs=[web_dev_agent, mobile_agent, marketing_agent],
    model=model
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



# Welcome message (chainlit)
@cl.on_chat_start
async def welcome():
    await cl.Message(
        author="🤖 AI Assistant",
        content="Welcome! 👋 Ask me anything related to **Web development**, **Mobile App development**, or **Marketing**."
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()

    try:
        loading_msg = cl.Message(author="🤖", content="**Generating response...**")
        await loading_msg.send()
      
        result = await Runner.run(triage_agent, input=user_input, run_config=config)


        #  final response
        final_response = f"### Agent's Response\n\n{result.final_output.strip()}"
        await cl.Message(author="📘 AI Assistant", content=final_response).send()

    except Exception as e:
        print("Error:", e)
        await cl.Message(
            author=" Error",
            content="Oops! Something went wrong while processing your request. Please try again."
        ).send()
