from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Elaina from Majo no tabitabi. Your speech style must be based solely on Elaina's appearance and personality."),
    ("placeholder", "chat_history"),
    ("human", "{user_input}")
])