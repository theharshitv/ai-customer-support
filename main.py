from fastapi import FastAPI
from pydantic import BaseModel
from db import get_or_create_conversation, update_conversation, escalate_conversation
from router import handle_message
from fastapi.responses import HTMLResponse

app = FastAPI()

class ChatRequest(BaseModel):
    customer_id: str
    message: str
    channel: str = "whatsapp"
    
@app.get("/")
async def home():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat(request: ChatRequest):
    conv = get_or_create_conversation(request.customer_id, request.channel)
    
    history = conv["messages"]
    
    result = handle_message(request.message, history)
    intent = result["intent"]
    response = result["response"]
    
    history.append({"role": "user", "content": request.message})
    history.append({"role": "assistant", "content": response})
    
    update_conversation(conv["id"], history, intent)
    
    if intent == "ESCALATE":
        escalate_conversation(conv["id"])
    
    return {"intent": intent, "response": response}