import asyncio
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage


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
async def main():
    messages = [
        SystemMessage("你是一个法律助手,只能回答和法律相关的问题,其他的一概不能回答"),
        HumanMessage("给我讲一个冷笑话"),
        # AIMessage("Cherry blossoms bloom...")
    ]
    response =await llm.ainvoke(messages)
    print(response.content)
if __name__ == '__main__':
    asyncio.run(main())