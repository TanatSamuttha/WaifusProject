from langchain.schema import AIMessage, HumanMessage

from models.pydantic_models import ChatState
from models.llm_models import llm, prompt

async def chat_node(state: ChatState) -> ChatState:
    messages = prompt.format_messages(
        chat_history = state.chat_history,
        user_input = state.user_input
    )

    response = await llm.ainvoke(messages)

    updated_history = state.chat_history+[
        HumanMessage(content=state.user_input),
        AIMessage(content=response.content)
    ]

    return {
        "user_input": state.user_input,
        "chat_history": updated_history
    }