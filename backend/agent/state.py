from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict, total=False):

    question: str

    intent: str

    answer: str

    sources: List[Dict[str, Any]]

    chat_history: List[Dict[str, str]]