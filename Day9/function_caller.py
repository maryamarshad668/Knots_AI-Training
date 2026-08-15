import json
import requests
import ollama

def search_courses(role, product=None, level=None):
    url = "https://learn.microsoft.com/api/catalog/"
    params = {"roles": role}
    if product:
        params["products"] = product
    if level:
        params["levels"] = level
    response = requests.get(url, params=params)
    data = response.json()
    modules = data.get("modules", [])[:5]
    results = []
    for m in modules:
        results.append({"title": m.get("title"), "summary": m.get("summary"), "url": m.get("url")})
    return results

tools = [{
    "type": "function",
    "function": {
        "name": "search_courses",
        "description": "Retrieves Microsoft Learn courses based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "role": {"type": "string", "description": "The role of the learner"},
                "product": {"type": "string", "description": "The product being covered"},
                "level": {"type": "string", "description": "Experience level (beginner, intermediate, advanced)"}
            },
            "required": ["role"]
        }
    }
}]

MODEL = "llama3.2"

def run_chat(user_message):
    messages = [{"role": "user", "content": user_message}]
    response = ollama.chat(model=MODEL, messages=messages, tools=tools)
    msg = response["message"]

    if msg.get("tool_calls"):
        messages.append(msg)
        for tool_call in msg["tool_calls"]:
            args = tool_call["function"]["arguments"]
            result = search_courses(**args)
            messages.append({
                "role": "tool",
                "content": json.dumps(result)
            })
        final_response = ollama.chat(model=MODEL, messages=messages)
        print(final_response["message"]["content"])
    else:
        print(msg["content"])

if __name__ == "__main__":
    user_message = input("Ask about a course: ")
    run_chat(user_message)