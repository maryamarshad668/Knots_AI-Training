# Day 9 Project — AI Product Suite

Three small apps demonstrating semantic search, image generation, and function calling 

```
day9_project/
├── semantic_search.py      # Embedding-based cosine similarity search
├── image_generator.py      # Image generation via free public API
└── function_caller.py      # Local LLM tool-use for external APIs
```

## Part A — semantic_search.py

Searches YouTube-style transcript chunks using semantic similarity instead of keyword matching.

**How it works:** each transcript chunk is converted into a vector using a local embedding model, and cosine similarity ranks chunks against the user's query.

**Tech:** `sentence-transformers` (runs the `all-MiniLM-L6-v2` model locally, no key).

**Setup:**
```
pip install sentence-transformers
python semantic_search.py
```

First run downloads the model (~80MB), cached after that — works offline from then on.

**Example:**
```
Ask a question: what is deep learning
Intro to AI @ 06:00 (score: 0.637)
Deep learning uses neural networks with many layers to model complex patterns.
```

## Part B — image_generator.py

Generates educational illustrations of historical monuments with a safety metaprompt applied.

**How it works:** builds a metaprompt that constrains the model to child-safe, educational content, then requests an image and saves it as a PNG.

**Tech:** [Pollinations.ai](https://pollinations.ai) free public image API (no key, no signup).

**Setup:**
```
pip install requests
python image_generator.py
```

**Example:**
```
Enter a historical monument name: Great Pyramid of Giza
Image saved as generated-monument.png
```

**Note:** this API streams image bytes directly rather than returning `b64_json`, so there's no manual base64 decode step here (unlike the Azure/OpenAI version).

## Part C — function_caller.py

Gives a chatbot the ability to call a real function (Microsoft Learn course search) based on user intent.

**How it works:** defines a JSON schema for `search_courses()`, passes it to the LLM as a tool, and if the model decides to call it, the script executes the real function and feeds the result back for a final natural-language answer.

**Tech:** [Ollama](https://ollama.com) running Llama 3.2 locally 

**Setup:**
```
ollama pull llama3.2
pip install ollama requests
python function_caller.py
```

**Example:**
```
Ask about a course: Find me an Azure course for beginners
```

**Note:** smaller local models are less consistent than GPT-4o at deciding *when* to trigger a tool call. If it just replies in plain text, rephrase more explicitly ("Search Microsoft Learn for beginner Azure courses") or try a larger model (`ollama pull llama3.1`).

## Why free/local instead of Azure OpenAI?

The original spec calls for Azure OpenAI (`text-embedding-ada-002`, `gpt-image-2`, `gpt-4o`). This version swaps each piece for a free/local equivalent so the project runs without provisioning Azure resources or paying for API usage — the core concepts (embeddings + cosine similarity, image generation + metaprompting, function calling / tool use) are identical either way.
