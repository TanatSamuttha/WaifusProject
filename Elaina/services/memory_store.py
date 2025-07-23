from langchain.schema import BaseMessage, HumanMessage, AIMessage

from services.database import query_chat

memory_store: list[BaseMessage] = []

async def memory_query(session_id: str):
    response = query_chat(session_id)

    memory_store.clear()

    for row in response:
        user_msg = row["user_message"]
        elaina_msg = row["elaina_message"]

        memory_store.append(HumanMessage(content=user_msg))
        memory_store.append(AIMessage(content=elaina_msg))