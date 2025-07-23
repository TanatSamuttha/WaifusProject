from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langchain.schema import BaseMessage, HumanMessage, AIMessage

from models.pydantic_models import ChatRequest, ChatHistoryRequest
from services.memory_store import memory_store, memory_query, update_memory
from services.database import insert_chat
from graphs.generate_graph import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/Elaina")
async def elaina_endpoint(req: ChatRequest):
    # print(memory_store)
    history = memory_store.get(req.session_id, [])

    final_state = await graph.ainvoke({
        "user_input": req.message,
        "chat_history": history
    })

    update_memory(req.session_id, final_state["chat_history"])

    insert_chat(req.session_id, req.message, final_state["response"])

    return {
        "emotional": final_state["emotional"],
        "response": final_state["response"]
    }

@app.post("/chat/Elaina/history")
def elaina_history_endpoint(req: ChatHistoryRequest):
    memory_query(req.session_id)

    mem = []
    for i in memory_store[req.session_id]:
        print(i)
        if i.type == "human":
            mem.append({
                "sender": "user",
                "message": str(i.content)
            })
        else:
            mem.append({
                "sender": "elaina",
                "message": str(i.content)
            })
    return {
        "response": mem
    }
    

app.mount("/", StaticFiles(directory="static", html=True), name="static")