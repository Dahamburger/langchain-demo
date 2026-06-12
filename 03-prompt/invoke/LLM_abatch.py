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
    model="qwen3.7-max",
    model_provider="openai",
    api_key=QWEN_API_KEY,
    base_url=QWEN_BASE_URL
)
async def main():
    messages = [
        "redis是什么东西",
        "SpringBoot是什么",
        "mysql是什么"
    ]
    responses = await llm.abatch(messages)
    for q,r in zip(messages, responses):
        print(f'问题:{q} \n 回复:{r.content}\n')
    # for response in responses:
    #     print(response.content)
if __name__ == '__main__':
    asyncio.run(main())