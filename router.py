from prompts import CLASSIFIER_PROMPT, ROUTE_PROMPTS
from llm import call_llm

VALID_CATEGORIES = ["BILLING", "REFUND", "TECHNICAL", "GENERAL", "ESCALATE"]

def classify_intent(message):
    prompt = CLASSIFIER_PROMPT.format(message=message)
    result = call_llm([{"role": "user", "content": prompt}])
    category = result.strip().upper()
    if category not in VALID_CATEGORIES:
        return "GENERAL"
    return category

    
def generate_response(intent, history):
    if intent == "ESCALATE":
        return "Thank you for your patience. Our Team will contact you soon."
    
    system_prompt = ROUTE_PROMPTS[intent]
    
    msg_list = [{"role": "system", "content": system_prompt}] + history
    return call_llm(msg_list)


def handle_message(message, history):
    intent = classify_intent(message)
    # history.append({"role": "user", "content": message})
    response = generate_response(intent, history)
    response_dict = {"intent": intent, "response": response}
    return response_dict