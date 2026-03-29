import os
from dotenv import load_dotenv
from langchain import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-5.3-codex",
    api_key = os.getenv("OPENAI_API_KEY"),     
    streaming = True,
    max_tokens = 7500,
    temperature = 0.2,    # focused but slightly flexible for UI creativity
)

llm_chat = ChatOpenAI(
    model = "gpt-4.1-nano",
    api_key = os.getenv("OPENAI_API_KEY"),
        max_tokens = 600,
        temperature = 0,  # always returns exactly "react" or "node" — no randomness
)