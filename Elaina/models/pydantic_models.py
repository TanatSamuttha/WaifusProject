from pydantic import BaseModel
from langchain.schema import BaseMessage
from typing import Optional

class ChatState(BaseModel):
    chat_history: list[BaseMessage]
    user_input: str
    emotional: Optional[str] = None
    response: Optional[str] = None

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatHistoryRequest(BaseModel):
    session_id: str