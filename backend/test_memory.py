from services.memory import ConversationMemory


memory = ConversationMemory()


memory.add_user_message(
    "Where is the FastAPI application created?"
)

memory.add_assistant_message(
    "The FastAPI application is created in backend/main.py."
)

memory.add_user_message(
    "Explain that file."
)


print("\nCONVERSATION HISTORY")
print("=" * 60)

for message in memory.get_history():

    print(
        f"{message['role'].upper()}: "
        f"{message['content']}"
    )