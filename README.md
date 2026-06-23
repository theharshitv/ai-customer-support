# AI Customer Support System

A multi-route AI customer support backend built with Python and FastAPI. It classifies incoming customer messages and responds using the right AI agent based on what the customer needs.

Built this as a hands-on project to learn how real AI systems work behind the scenes.

---

## What it does

When a customer sends a message, the system:
1. Reads the message
2. Figures out what they want (billing, refund, technical issue, etc.)
3. Picks the right AI agent for that category
4. Replies with a relevant, context-aware response
5. Saves the full conversation to a database

So if someone says "I want a refund", it doesn't just send a generic reply. It routes them to a refund agent that knows exactly how to handle that situation.

---

## Tech Stack

- **Python** for everything
- **FastAPI** for the backend server
- **Groq API** (Llama 3.3 70B) for the AI responses
- **Supabase** (PostgreSQL) for storing conversations
- **python-dotenv** for managing API keys

---

## Project Structure

```
ai-customer-support
1. main.py - FastAPI server and /chat endpoint
2. router.py - Intent classification and response generation
3. llm.py - Groq API calls
4. prompts.py - System prompts for each support agent
4. db.py - Supabase database functions
5. .env - API keys (not pushed to GitHub)
```

---

## How the Routing Works

The system uses a two-step LLM call:

1. First call classifies the message into one of five categories: BILLING, REFUND, TECHNICAL, GENERAL, or ESCALATE
2. Second call generates a reply using the system prompt for that category

Each category has its own personality and instructions. For example the refund agent is empathetic and asks for an order ID. The technical agent is step-by-step and structured. ESCALATE skips the LLM entirely and flags the conversation for a human.

---

## How to Run Locally

**1. Clone the repo**
```
git clone https://github.com/theharshitv/ai-customer-support.git
cd ai-customer-support
```

**2. Create a virtual environment**
```
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Create a `.env` file in the root folder**
```
GROQ_KEY=your_groq_api_key
SUPABASE_PROJECT_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
```

**5. Run the server**
```
uvicorn main:app --reload
```

**6. Test it with Postman**

Send a POST request to `http://localhost:8000/chat` with this body:
```json
{
    "customer_id": "user_123",
    "message": "I want a refund for my order"
}
```

You will get back the intent and the AI response.

---

## API Reference

### POST /chat

Request body:
```json
{
    "customer_id": "string",
    "message": "string",
    "channel": "whatsapp" (default)
}
```

Response:
```json
{
    "intent": "REFUND",
    "response": "I'm here to help with your refund..."
}
```

---

## What I Learned Building This

- How to structure a Python backend from scratch
- How LLM routing works using system prompts
- How to persist conversation history in PostgreSQL so the AI has memory
- How webhooks work and how external services talk to your server
- How to manage API keys and environment variables properly

---

## What's Next

- Add WhatsApp channel via Twilio
- Add email channel via Gmail SMTP
- Build a simple dashboard to view open and escalated conversations
- Deploy to Railway

---

Made by Harshit Verma | B.Tech CSE (AI)
