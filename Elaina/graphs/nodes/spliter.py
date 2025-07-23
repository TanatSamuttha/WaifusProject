from langchain.schema import AIMessage, HumanMessage

from models.pydantic_models import ChatState
from models.llm_models import llm, prompt

async def split_node(state: ChatState) -> ChatState:
    response = state.chat_history[-1].content.split("__________")
    print(response)

    # เพื่อความผิดพลาด
    emotional = "Normal"
    message = response[0]

    if len(response) == 2:
        emotional = response[0]
        message = response[1]
    else:
        print("no emo")

    return {
        "emotional": emotional,
        "response": message
    }