from langchain.schema import BaseMessage

memory_store: dict[str, list[BaseMessage]] = {}