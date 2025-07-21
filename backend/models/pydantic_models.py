from pydantic import BaseModel
from langchain.schema import BaseMessage

class ChatState(BaseModel):
    chat_history: list[BaseMessage]
    user_input: str
    response: str