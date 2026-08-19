import os
from google import genai
from vectorstore import create_vectorstore,search

def load_document():
    with open("knowledge.txt","r",encoding="utf-8") as file:
        return file.read()

def chunk_text(text,size=500):
    paragraphs=[p.strip() for p in text.split("\n\n") if p.strip()]
    chunks=[]
    current=""

    for paragraph in paragraphs:
        if len(current)+len(paragraph)>size:
            if current:
                chunks.append(current)
            current=paragraph
        else:
            current+=("\n"+paragraph if current else paragraph)

    if current:
        chunks.append(current)

    return chunks

text=load_document()
chunks=chunk_text(text)
index=create_vectorstore(chunks)

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer(question):
    results=search(index,chunks,question)

    context="\n\n".join(results)

    prompt=f"""Answer the question only using the provided context.
If the answer is not present in the context, say:
"I don't have enough information in the knowledge base to answer that."

Do not use outside knowledge.

Context:
{context}

Question:
{question}
"""

    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text