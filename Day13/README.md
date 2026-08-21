# AI Travel Planning Agent

A conversational AI agent built with the **OpenAI Agents SDK** that plans personalized trips based on destination, budget, and duration. It remembers conversation context across turns, supports follow-up edits like "make it cheaper," and refuses requests unrelated to travel planning using guardrails.

Built as part of Day 13 of the Knots AI Training program.

## Features

- **Conversational itinerary planning** — provide a destination, budget, and number of days, and the agent generates a structured day-by-day plan.
- **Session memory** — follow-up messages like "make it cheaper" or "add a museum on day 2" update the existing itinerary instead of starting over.
- **Custom tool** — `get_hotel_price` returns an estimated nightly hotel cost based on destination and budget tier.
- **Guardrails** — off-topic requests (e.g. "how do I bake a cake?") are detected and politely declined, keeping the conversation focused on travel planning.
- **Gemini-compatible** — configured to run on Google's Gemini API through its OpenAI-compatible endpoint, so no OpenAI key is required.

## Project Structure

```
Day13/
├── agent.py            # Main agent logic, guardrails, and session loop
├── tools.py            # Custom Python tool(s) attached to the agent
├── .env                # API key (not committed to git)
├── .gitignore          # Excludes .env and cache files from git
├── requirements.txt    # Python dependencies
└── README.md
```

## Setup

**1. Clone the repo and navigate to this folder**

```bash
cd ai-travel-agent
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file in this folder with:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Once running, chat with the agent directly in your terminal:

```
You: I want to visit Japan for 5 days on a mid-range budget
Agent: [generates a day-by-day itinerary for Japan]

You: make it cheaper
Agent: [updates the same itinerary with lower-cost options]

You: how do I bake a cake?
Agent: I can only help with travel planning requests.
```

Type `exit` to quit.

## How It Works

- **`tools.py`** defines `get_hotel_price`, a custom function tool the agent can call to estimate accommodation costs for a given destination and budget tier.
- **`agent.py`** defines two agents:
  - A **guardrail agent** that classifies whether a user message is travel-related.
  - The main **Travel Planner agent**, which generates and updates itineraries, calls `get_hotel_price` when relevant, and is blocked from responding if the guardrail agent flags a message as off-topic.
- **`SQLiteSession`** persists conversation history locally, so the agent has full context for follow-up requests without you needing to resend previous messages.

## Notes

- The model is configured to use Gemini (`gemini-3.6-flash`) via its OpenAI-compatible API. To switch back to OpenAI, replace the `gemini_client`/`gemini_model` setup in `agent.py` with a standard `OpenAIChatCompletionsModel` call using `OPENAI_API_KEY`.
