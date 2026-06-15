import os
import time

from arrow import now
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv(encoding="utf-8")

template = PromptTemplate.from_template(
    template = "现在的时间是:{time},问题:{question}",
    partial_variables={"time": now("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss")}
)
print(template.format(question="写一个冒泡排序算法,只要代码"))
time.sleep(2)
template = PromptTemplate.from_template(
    template = "现在的时间是:{time},问题:{question}",
    partial_variables={"time": now("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss")}
)
print(template.format(question="写一个冒泡排序算法,只要代码"))
print("*"*30)

template = PromptTemplate.from_template(template = "现在的时间是:{time},问题:{question}",)
template.partial_variables={"time": now("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss")}
print(template.format(question="你好"))

print("*"*30)

prompt_template = PromptTemplate(
    template="{foo},{bar}",
    input_variables=["foo", "bar"],
    partial_variables={"foo": "hello"}
)
print(prompt_template.format(bar="world", foo="lisi"))
# llm = init_chat_model(
#     model="qwen-plus",
#     model_provider="openai",
#     api_key=os.getenv("QWEN_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )
#
# print(llm.invoke(from_template).content)
