import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
# 创建一个JsonOutputParser
parser = JsonOutputParser()
messages = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个有用的助手"),
        ("human", "给我讲一个冷笑话,以json格式输出,q表示问题,a表示回答"),
    ]
).format()
# print(messages)
result = llm.invoke(messages)
print(result)
response = parser.invoke(result)
print(response)
