from agent.graph import graph


questions = [
    "Where is the FastAPI application created?",
    "Explain the VectorStore class.",
    "Find bugs in the authentication code.",
    "What is Python?"
]


for question in questions:

    print("\n" + "=" * 60)

    print("QUESTION:")
    print(question)

    result = graph.invoke({
        "question": question
    })

    print("\nINTENT:")
    print(result["intent"])

    print("\nANSWER:")
    print(result["answer"])