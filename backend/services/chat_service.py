from agent.graph import graph
from services.memory import ConversationMemory


class ChatService:

    def __init__(self):

        self.memory = ConversationMemory()

    def ask(self, question: str):

        history = self.memory.get_history()

        result = graph.invoke({
            "question": question,
            "chat_history": history
        })

        answer = result.get(
            "answer",
            ""
        )

        self.memory.add_user_message(
            question
        )

        self.memory.add_assistant_message(
            answer
        )

        return {
            "answer": answer,
            "sources": result.get(
                "sources",
                []
            ),
            "history": self.memory.get_history()
        }

    def clear_memory(self):

        self.memory.clear()