from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langchain.schema import BaseMessage, HumanMessage, AIMessage

from models.pydantic_models import ChatRequest, ChatHistoryRequest
from services.memory_store import memory_store, memory_query
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
    print("ok")
    final_state = await graph.ainvoke({
        "user_input": req.message,
        "chat_history": memory_store
    })

    global memory_store = final_state["chat_history"]

    insert_chat(req.session_id, req.message, final_state["response"])

    return {
        "emotional": final_state["emotional"],
        "response": final_state["response"]
    }

@app.post("/chat/Elaina/history")
async def elaina_history_endpoint(req: ChatHistoryRequest):
    memory_query(req.session_id)

    mem = []
    for i in memory_store:
        if i.type() == HumanMessage:
            mem.append({
                "sender": "user",
                "message": str(i.content)
            })
        else:
            mem.append({
                "sender": "elaina",
                "message": str(i.content)
            })
    return mem
    

app.mount("/", StaticFiles(directory="static", html=True), name="static")