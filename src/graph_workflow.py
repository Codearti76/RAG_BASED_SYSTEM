from langgraph.graph import StateGraph

from src.rag_pipeline import run_rag
from src.hitl import escalate_to_human

# ✅ Simple dict state (no custom class)

from typing import TypedDict

class GraphState(TypedDict):
    query: str
    answer: str
    confidence: float

# 🧩 Node 1: Process
def process_node(state):
    print("DEBUG STATE:", state)

    # ✅ fallback fix
    if not state:
        raise ValueError("State is empty - LangGraph issue")

    query = state.get("query")

    if not query:
        raise ValueError("Query missing in state")

    result = run_rag(query)
    return {**state, **result}


# 🧩 Decision
def decide_node(state):
    if state.get("confidence", 0) < 0.5:
        return "hitl"
    return "end"


# 🧩 HITL
def hitl_node(state):
    result = escalate_to_human(state["query"])
    return {**state, **result}


# 🏗️ Build Graph
builder = StateGraph(GraphState)

builder.add_node("process", process_node)
builder.add_node("hitl", hitl_node)

# ✅ Correct flow
builder.set_entry_point("process")

builder.add_conditional_edges(
    "process",
    decide_node,
    {
        "hitl": "hitl",
        "end": "__end__"
    }
)

graph = builder.compile()


# 🚀 Run Graph (FIX HERE)
def run_graph(query):
    state = {"query": query}

    result = graph.invoke(
        state,
        config={"configurable": {"thread_id": "1"}}
    )

    return result