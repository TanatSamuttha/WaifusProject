from langchain.schema import AIMessage, HumanMessage

from models.pydantic_models import ChatState
from models.llm_models import llm, prompt

async def split_node(state: ChatState) -> ChatState:
    response = state.chat_history[-1].content.split("__________")
    emotional = response[0]
    message = response[1]

    return {
        "emotional": emotional,
        "response": message
    }