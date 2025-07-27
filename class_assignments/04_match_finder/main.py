from agents import Agent, Runner, WebSearchTool, function_tool, set_tracing_disabled
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import requests
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
if not OPENAI_API_KEY:
    raise KeyError("OPENAI_API_KEY not found in environment.")


WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_API_TOKEN")
WHATSAPP_INSTANCE_ID = os.getenv("WHATSAPP_INSTANCE_ID")
ULTRAMSG_API_URL = os.getenv("ULTRAMSG_API_URL")


@function_tool
def get_matched_rishta(condition: str, age: int, match_gender: str, profession: str = "") -> list[dict]:
    """
    Return rishta entries from Google Sheet based on age condition, opposite gender,
    and optionally profession.

    - condition: One of '==', '>', '<', '>=', '<=', '!='
    - age: Age to compare
    - looking_for_gender: The user's gender (to find opposite)
    - profession: Optional; filter by this profession (case-insensitive match)
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)
    gspread_client = gspread.authorize(creds)

    sheet = gspread_client.open("FakeMatches").worksheet("Sheet1")
    records = sheet.get_all_records()

    if condition not in ['==', '>', '<', '>=', '<=', '!=']:
        return []

    match_gender = match_gender.strip().capitalize()
    print(f"🔍 Filtering rishtas for: Gender={match_gender}, Age {condition} {age}, Profession={profession}")

    filtered = []
    for person in records:
        try:
            print("👉 Checking person:", person)
            person_age = int(person.get("Age", 0))
            person_gender = person.get("Gender", "").strip()
            person_profession = person.get("Job", "").lower().strip()

            if person_gender != match_gender:
                print("❌ Skipped: Gender mismatch")
                continue

            if profession and profession.lower() not in person_profession:
                print(f"❌ Skipped: Profession '{person_profession}' does not match filter '{profession}'")
                continue

            if condition == "==" and person_age == age:
                filtered.append(person)
                print("Match found:", person)
            elif condition == "!=" and person_age != age:
                filtered.append(person)
                print("Match found:", person)
            elif condition == ">" and person_age > age:
                filtered.append(person)
                print("Match found:", person)
            elif condition == "<" and person_age < age:
                filtered.append(person)
                print("Match found:", person)
            elif condition == ">=" and person_age >= age:
                filtered.append(person)
                print("Match found:", person)
            elif condition == "<=" and person_age <= age:
                filtered.append(person)
                print("Match found:", person)
        except:
            continue

    print(f" Total Matches Found: {len(filtered)}")
    return filtered


@function_tool
def send_match_to_whatsapp(message: str, recipient_number: str) -> str:
    """
    Sends a WhatsApp message using the UltraMsg API.
    """
    if not ULTRAMSG_API_URL:
        return "Missing ULTRAMSG_API_URL in environment."

    payload = {
        "token": WHATSAPP_API_TOKEN,
        "to": recipient_number,
        "body": message
    }

    try:
        response = requests.post(ULTRAMSG_API_URL, data=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Failed to send message to {recipient_number}: {e}"

    return f"Message successfully sent to {recipient_number}"




agent = Agent(
    name="RishtaAuntyAgent",
    model= "gpt-4o-mini",
 instructions="""
You are a digital rishtay wali aunty 👵— polite, cheerful, and a little nosy like every real aunty.

You'll receive filtered rishtay from a tool based on:
- Age condition (like > 25)
- Gender (user's gender — find opposite)
- Optional profession (e.g., Doctor, Engineer, etc.)

🎯 Your task:
1. Pick one best match based on all given criteria.
2. Search the match on linkedin and give all details about match with the message to user.
3. Send a rishta-style message in polite aunty tone:
    - Include Name, Age, Job, and City
    - Add a respectful compliment (like: “well-settled”, “decent ladki/beta”)
    - Use 1-2 soft emojis (🌸💍 etc.)
    - End with a kind dua line.

📌 If NO rishta is found:
- If the profession filter fails: say “No rishta found with that profession” and kindly suggest a match from a similar profession, **only if available**.
- If no one meets the age/gender filter: respond with “Beta, aaj koi perfect rishta nahi mila… lekin dua zaroor hai ❤️”

Use Urdu if user used Urdu. Otherwise, reply in English.
Send the message using WhatsApp tool.
"""

,
    tools=[get_matched_rishta, send_match_to_whatsapp, WebSearchTool()],
)



@cl.on_chat_start
async def welcome():
    await cl.Message(
        content="""🌸 *Assalamualaikum beta!* 👵  
Main hoon *Rishta Aunty Agent*, aap ke liye tayar *AI-powered rishtay* le kar! 💍

Aap sirf apni requirements batayein — age, profession, city, ya jo dil kare…  
Aur agar WhatsApp number bhi dein to rishta *seedha inbox mein!* 😄📱"""
    ).send()
    
    
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()
    
    try:
        # Initial loader message
        loading_msg = cl.Message(author="🤖", content="🔍 **Finding the perfect match please wait....**")
        await loading_msg.send()
      
        # Run the agent
        result = await Runner.run(agent, input=user_input)

        # Update message with final output
        loading_msg.content = f"{result.final_output.strip()}"
        await loading_msg.update()

    except Exception as e:
        print("Error:", e)
        await cl.Message(
            author="❌ Error",
            content="Oops! Kuch masla ho gaya rishta dhoondtay hue 😔. Dobara try karein ya details check karein."
        ).send()
