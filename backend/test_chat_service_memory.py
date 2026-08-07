from services.memory import ConversationMemory


memory = ConversationMemory()


questions = [
    "Where is the FastAPI application created?",
    "Explain that file.",
    "What framework is being used?"
]


for question in questions:

    memory.add_user_message(
        question
    )

    print(
        f"\nUSER: {question}"
    )


    print("\nCURRENT HISTORY:")

    for message in memory.get_history():

        print(
            f"{message['role']}: "
            f"{message['content']}"
        )