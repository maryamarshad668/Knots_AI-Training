from rag import answer

print("AI FAQ Assistant")
print("Type 'exit' to quit")

while True:
    question=input("\nYou: ")

    if question.lower()=="exit":
        break

    print("AI:",answer(question))