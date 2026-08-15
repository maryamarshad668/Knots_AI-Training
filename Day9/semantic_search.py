import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

transcripts = [
    {"video": "Intro to AI", "timestamp": "00:00", "text": "Artificial intelligence is the simulation of human intelligence by machines."},
    {"video": "Intro to AI", "timestamp": "03:00", "text": "Machine learning is a subset of AI that learns patterns from data."},
    {"video": "Intro to AI", "timestamp": "06:00", "text": "Deep learning uses neural networks with many layers to model complex patterns."},
    {"video": "Prompt Engineering", "timestamp": "00:00", "text": "Prompt engineering is the practice of designing inputs to get better outputs from LLMs."},
    {"video": "Prompt Engineering", "timestamp": "03:00", "text": "Few shot prompting gives the model examples to guide its response."},
    {"video": "Function Calling", "timestamp": "00:00", "text": "Function calling lets an LLM invoke external tools and APIs."},
    {"video": "Function Calling", "timestamp": "03:00", "text": "The model returns a JSON payload describing which function to call and with what arguments."}
]

def get_embedding(text):
    return model.encode(text)

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def build_index(data):
    for item in data:
        item["embedding"] = get_embedding(item["text"])
    return data

def search(query, index, top_k=3):
    query_vec = get_embedding(query)
    scored = []
    for item in index:
        score = cosine_similarity(query_vec, item["embedding"])
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_k]

if __name__ == "__main__":
    index = build_index(transcripts)
    query = input("Ask a question: ")
    results = search(query, index)
    for score, item in results:
        print(f"{item['video']} @ {item['timestamp']} (score: {score:.3f})")
        print(item["text"])
        print("---")