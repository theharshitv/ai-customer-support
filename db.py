import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

anon_key = os.getenv("SUPABASE_ANON_KEY")
project_url = os.getenv("SUPABASE_PROJECT_URL")

supabase = create_client(project_url, anon_key)

def get_or_create_conversation(customer_id, channel):
    response = (
        supabase.table("conversations")
        .select("*")
        .eq("customer_id", customer_id)
        .eq("status", "open")
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]
    
    new_conversation = {
        "customer_id": customer_id,
        "channel": channel,
        "messages": [],
        "status": "open",
    }

    response = (
        supabase.table("conversations")
        .insert(new_conversation)
        .execute()
    )

    return response.data[0]

def update_conversation(conv_id, messages, intent):
    response = (
        supabase.table("conversations")
        .update({"messages": messages, "intent": intent})
        .eq("id", conv_id)
        .execute()
    )

    return response

def escalate_conversation(conv_id):
    response = (
        supabase.table("conversations")
        .update({"status": "escalated"})
        .eq("id", conv_id)
        .execute()
    )

    return response