import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from agents import Agent, Runner, SQLiteSession, InputGuardrail, GuardrailFunctionOutput, OpenAIChatCompletionsModel, set_tracing_disabled
set_tracing_disabled(True)
from openai import AsyncOpenAI
from pydantic import BaseModel
from tools import get_hotel_price
gemini_client = AsyncOpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)
class GuardrailOutput(BaseModel):
    is_travel_related: bool
    reasoning: str
guardrail_agent = Agent(
    name="Guardrail Check",
    instructions="Determine if the user's message is related to travel planning, itineraries, hotels, flights, or budgets. If not, set is_travel_related to false.",
    output_type=GuardrailOutput,
    model=gemini_model,
)
async def travel_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final = result.final_output
    return GuardrailFunctionOutput(output_info=final, tripwire_triggered=not final.is_travel_related)
travel_agent = Agent(
    name="Travel Planner",
    instructions="You are a travel planning assistant. Gather destination, budget, and number of days if missing. Generate a structured day-by-day itinerary. If the user asks to change or cheapen the plan, update the existing itinerary using conversation history instead of starting over. Use get_hotel_price when discussing accommodation costs.",
    tools=[get_hotel_price],
    input_guardrails=[InputGuardrail(guardrail_function=travel_guardrail)],
    model=gemini_model,
)
async def main():
    session = SQLiteSession("travel_session")
    print("AI Travel Agent. Type exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        try:
            result = await Runner.run(travel_agent, user_input, session=session)
            print("Agent:", result.final_output)
        except Exception:
            print("Agent: I can only help with travel planning requests.")
if __name__ == "__main__":
    asyncio.run(main())