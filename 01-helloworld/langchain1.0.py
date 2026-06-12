import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(encoding="utf-8")
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_BASE_URL = os.getenv("QWEN_BASE_URL")
# print(QWEN_API_KEY, QWEN_BASE_URL)

llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=QWEN_API_KEY,
    base_url=QWEN_BASE_URL
)
response = llm.invoke("你好")
print(response)