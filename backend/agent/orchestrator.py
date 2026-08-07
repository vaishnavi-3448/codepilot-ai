from agent.state import AgentState


class Orchestrator:

    def classify(self, state: AgentState):

        question = state["question"].lower()

        # Code explanation
        explanation_keywords = [
            "explain",
            "how does",
            "how do",
            "what does",
            "what is",
            "describe",
            "understand",
            "walk me through"
        ]

        if any(
            keyword in question
            for keyword in explanation_keywords
        ):
            return {
                "intent": "code_explanation"
            }

        # Code search
        search_keywords = [
            "where",
            "which file",
            "find",
            "locate",
            "location",
            "implemented",
            "defined",
            "created"
        ]

        if any(
            keyword in question
            for keyword in search_keywords
        ):
            return {
                "intent": "code_search"
            }

        # Everything else
        return {
            "intent": "general"
        }