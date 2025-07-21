from fastapi import FastAPI

from models.pydantic_models import ChatRequest
from services.memory_store import memory_store
from graphs.generate_graph import graph

app = FastAPI()

@app.post("/chat/Elaina")
async def elaina_endpoint(req: ChatRequest):
    history = memory_store.get(req.session_id, [])

    final_state = await graph.ainvoke({
        "user_input": req.message,
        "chat_history": history
    })

    memory_store[req.session_id] = final_state["chat_history"]

    return {
        "emotional": final_state["emotional"],
        "response": final_state["response"]
    }