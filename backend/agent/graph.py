from langgraph.graph import StateGraph, START, END

from agent.state import AgentState
from agent.orchestrator import Orchestrator
from agent.router import route_question

from agent.nodes import (
    code_search_agent,
    code_explanation_agent,
    bug_detection_agent,
    general_agent
)


orchestrator = Orchestrator()


def classify_question(
    state: AgentState
):

    return orchestrator.classify(
        state
    )


graph_builder = StateGraph(
    AgentState
)


graph_builder.add_node(
    "orchestrator",
    classify_question
)

graph_builder.add_node(
    "code_search",
    code_search_agent
)

graph_builder.add_node(
    "code_explanation",
    code_explanation_agent
)

graph_builder.add_node(
    "bug_detection",
    bug_detection_agent
)

graph_builder.add_node(
    "general",
    general_agent
)


graph_builder.add_edge(
    START,
    "orchestrator"
)


graph_builder.add_conditional_edges(
    "orchestrator",
    route_question,
    {
        "code_search": "code_search",
        "code_explanation": "code_explanation",
        "bug_detection": "bug_detection",
        "general": "general"
    }
)


graph_builder.add_edge(
    "code_search",
    END
)

graph_builder.add_edge(
    "code_explanation",
    END
)

graph_builder.add_edge(
    "bug_detection",
    END
)

graph_builder.add_edge(
    "general",
    END
)


graph = graph_builder.compile()