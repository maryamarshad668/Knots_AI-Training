# Day 8 Project: Building AI Apps (Free Gemini Version)

Two simple beginner-friendly AI apps using Google Gemini's free API (no credit card required).

## Files
- `.env` - stores your Gemini API key
- `recipe_generator.py` - generates recipes from ingredients, then a shopping list
- `study_buddy.py` - chat with an Abe Lincoln persona tutor

## Get a free API key

1. Go to https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API key"
4. Copy the key into `.env`:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Setup

```
pip install openai python-dotenv
```

Note: we still use the `openai` Python package, just pointed at Google's OpenAI-compatible endpoint. No need to install a separate Google SDK.

## Running the Recipe Generator

```
python recipe_generator.py
```

Example:
```
Enter ingredients you have (comma separated): apple, flour
```

The app will:
1. Generate 2 recipes using those ingredients
2. Ask the AI again to build a shopping list of missing ingredients

## Running the Study Buddy

```
python study_buddy.py
```

Example:
```
Enter temperature (0.1 to 0.9): 0.7
```

- Lower temperature (0.1) = more focused, predictable answers
- Higher temperature (0.9) = more creative, varied answers

Then chat with Abe Lincoln. Type `quit` to exit.

## Notes
- Model used: `gemini-2.5-flash`
- Gemini's free tier has daily and per-minute rate limits, but no cost and no card required
- Never share your `.env` file or commit it to GitHub
- Google's free tier may use your prompts for model improvement, so avoid sending private/sensitive data