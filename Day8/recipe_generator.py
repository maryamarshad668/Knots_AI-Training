from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
ingredients = input("Enter ingredients you have (comma separated): ")
messages = [
    {"role": "system", "content": "You are a helpful cooking assistant."},
    {"role": "user", "content": f"Give me 2 simple recipes using these ingredients: {ingredients}"}
]
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages,
    temperature=0.7
)
recipes = response.choices[0].message.content
print("\n--- RECIPES ---")
print(recipes)
messages.append({"role": "assistant", "content": recipes})
messages.append({"role": "user", "content": f"Produce a shopping list for the generated recipes, excluding these ingredients I already have: {ingredients}"})
response2 = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages,
    temperature=0.7
)
shopping_list = response2.choices[0].message.content
print("\n--- SHOPPING LIST ---")
print(shopping_list)