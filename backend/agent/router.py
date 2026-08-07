from agent.state import AgentState


def route_question(state: AgentState):

    intent = state.get(
        "intent",
        "general"
    )

    if intent == "code_search":
        return "code_search"

    if intent == "code_explanation":
        return "code_explanation"

    if intent == "bug_detection":
        return "bug_detection"

    return "general"