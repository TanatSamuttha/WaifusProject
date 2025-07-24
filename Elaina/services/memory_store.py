from langchain.schema import BaseMessage, HumanMessage, AIMessage

from services.database import query_chat

memory_store: dict[str, list[BaseMessage]] = {}

def memory_query(session_id: str):
    response = query_chat(session_id)
    if session_id not in memory_store:
        memory_store[session_id] = []
    else:
        memory_store[session_id].clear()

    for row in response:
        user_msg = row["user_message"]
        elaina_msg = row["elaina_message"]
        emotional = row["emotional"]

        memory_store[session_id].append(HumanMessage(content=user_msg))
        memory_store[session_id].append(AIMessage(content=(emotional+"__________"+elaina_msg)))

def update_memory(session_id: str, chat_history):
    # print(type(chat_history[0]))
    global memory_store
    memory_store[session_id] = chat_history
    # print(memory_store[session_id])