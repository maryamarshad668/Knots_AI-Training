import faiss
from embeddings import create_embeddings

def create_vectorstore(chunks):
    embeddings=create_embeddings(chunks)
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def search(index,chunks,query,k=3):
    embedding=create_embeddings([query])
    distances,indices=index.search(embedding,k)
    return [chunks[i] for i in indices[0] if i<len(chunks)]