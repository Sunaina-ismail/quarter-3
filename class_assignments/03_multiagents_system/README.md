# 🤖 Multi-Agent AI Assistant
## Author: Sunaina_Ismail

This project is a smart **Multi-Agent System** built using **Chainlit** and the **Gemini API**, created as part of an assignment.

##  Description

The system features a **Manager Agent** that intelligently routes user queries to specialized agents based on the topic:
-  **Web Dev Agent**: Handles questions related to frontend/backend and website development.
-  **Mobile App Agent**: Supports queries about Android, iOS, Flutter, and React Native.
-  **Marketing Agent**: Assists with digital marketing, branding, and promotional strategies.

Each agent uses the **Gemini 2.0 Flash** model for intelligent responses.

##  Features

- Smart routing of queries to relevant agents
- Greeting and info handling by Manager Agent
- Error handling for invalid or unsupported questions
- Seamless user interaction via Chainlit UI

##  Test Questions

- `What is React.js and how does it work?` → Web Dev Agent  
- `How to publish a Flutter app to Play Store?` → Mobile App Agent  
- `How do I grow my brand using Instagram?` → Marketing Agent  
- `What’s your name?` → Manager responds with policy message  
- `Tell me about mobile apps and web development together.` → ❌ (Will show why multiple topics are not allowed at once)

## 🛠 Built With

- **Python**
- **Chainlit**
- **Gemini API (2.0 Flash Model)**
- **Dotenv**

## 😊 Developer Note

It was a fun and exciting project to build!  
Working with multiple agents and routing logic made me even more curious and passionate about AI systems. 💙

