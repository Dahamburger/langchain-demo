import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#
# LCEL 是 LangChain 提供的一种声明式编程范式，用于构建和组合 LangChain 组件（如提示模板、模型、解析器等）。
# 它通过链式调用让代码更简洁、更易读。

load_dotenv(encoding="utf-8")
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}的助手"),
    ("user", "给我讲一个关于{thing}的冷笑话"),
])

parser = StrOutputParser()

llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 链式调用
chain = prompt | llm | parser
print(type(chain))
name = chain.get_name()
print(name)
result = chain.invoke({"role": "很有用", "thing": "python"})
print(result)
