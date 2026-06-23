import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_KEY"),
)

def call_llm(messages: list) -> str:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# if __name__ == "__main__":
#     result = call_llm([{"role": "user", "content": "What is 2+2?"}])
#     print(result)