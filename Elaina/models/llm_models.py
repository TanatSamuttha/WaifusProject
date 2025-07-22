from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

from services.config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", google_api_key = GOOGLE_API_KEY)
with open("prompts/prompt.txt", "r", encoding="utf-8") as f:
    system_message = f.read()
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("placeholder", "{chat_history}"),
    ("human", "{user_input}")
])