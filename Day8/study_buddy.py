from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
persona = "You are Abe Lincoln. Respond using grammar and words like Abe would have used."
temperature = float(input("Enter temperature (0.1 to 0.9): "))
messages = [{"role": "system", "content": persona}]
print("Study Buddy is ready. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,
        temperature=temperature
    )
    reply = response.choices[0].message.content
    print(f"Abe: {reply}")
    messages.append({"role": "assistant", "content": reply})