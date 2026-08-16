# Day 10 — Security, RAG, Agents & Fine-Tuning

```
day10_project/
├── secure_rag.py
├── policies.txt
├── autogen_team.py
├── fine_tune_prep.py
├── support_data.csv
├── support_data.jsonl
└── support_data_sft.jsonl
```

## Part A — secure_rag.py

Local RAG pipeline using TF-IDF embeddings and cosine nearest-neighbor search, with a prompt injection filter on input and a toxicity filter on output.

### Setup
```powershell
pip install scikit-learn numpy
```

### Run
```powershell
python secure_rag.py
```

Reads `policies.txt` in the same folder. Prints answers for 3 sample queries, including a blocked prompt injection attempt.

---

## Part B — autogen_team.py

Multi-agent system: a `Coder` agent writes code, a `Reviewer` agent checks it for security flaws, and a `UserProxyAgent` executes it and manages the conversation. Uses a local Ollama model, so no API key is required.

### Setup
```powershell
pip install ag2
```
Install Ollama: https://ollama.com/download/windows
```powershell
ollama pull llama3.1
`.

### Run
```powershell
python autogen_team.py
```

Watch the Coder, Reviewer, and UserProxy collaborate in the terminal on building a secure web scraper.

Notes:
- Uses `ag2` (fork of the classic `pyautogen` API) since `pyautogen==0.2.35` doesn't support Python 3.13+.
- `use_docker` is set to `False` in `code_execution_config`, so generated code runs directly on your machine. Set it to `True` instead if you have Docker Desktop installed, for safer sandboxed execution.

---

## Part C — fine_tune_prep.py

Converts a CSV of customer support examples into JSONL format for Hugging Face `SFTTrainer` fine-tuning.

### Setup
No extra installs needed — uses Python's built-in `csv` and `json` modules.

### Run
```powershell
python fine_tune_prep.py
```

Reads `support_data.csv` in the same folder. Produces:
- `support_data.jsonl` — raw instruction/context/response records
- `support_data_sft.jsonl` — formatted `{"text": "..."}` records ready for fine-tuning

### Using the output for fine-tuning
```python
from datasets import load_dataset
dataset = load_dataset("json", data_files="support_data_sft.jsonl")
```
Pass this dataset into `SFTTrainer` with a base model such as Llama 3 8B or Mistral (e.g. via Unsloth or Hugging Face `transformers`).

---

## Quick Start (all three)
```powershell
pip install scikit-learn numpy ag2
ollama pull llama3.1
python secure_rag.py
python autogen_team.py
python fine_tune_prep.py
```