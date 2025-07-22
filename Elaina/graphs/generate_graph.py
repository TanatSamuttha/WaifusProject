from langgraph.graph import StateGraph,START,END

from models.pydantic_models import ChatState
from graphs.nodes.generate_chat import chat_node
from graphs.nodes.spliter import split_node

builder = StateGraph(ChatState)
builder.add_node("chat", chat_node)
builder.add_node("spliter", split_node)
builder.add_edge(START, "chat")
builder.add_edge("chat", "spliter")
builder.add_edge("spliter", END)

graph = builder.compile()