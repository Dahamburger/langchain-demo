import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv(encoding="utf-8")

template = PromptTemplate(template="我是一个{role}工程师,问题:{question}", input_variables=["role", "question"])
from_template = template.format(role="python", question="写一个冒泡排序算法,只要代码")
print(from_template)

llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print(llm.invoke(from_template).content)
