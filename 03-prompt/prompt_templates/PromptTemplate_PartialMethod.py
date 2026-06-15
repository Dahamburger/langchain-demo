import os
import time

from arrow import now
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv(encoding="utf-8")

template = PromptTemplate.from_template("现在的时间是:{time},问题:{question}")

# partial 部分模板 返回值是一个<class 'langchain_core.prompts.prompt.PromptTemplate'>
partial = template.partial(time=now("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss"))

print(partial)
print(type(partial))

partial_format = partial.format(question="写一个冒泡排序算法,只要代码")
print(partial_format)
print(type(partial_format))



