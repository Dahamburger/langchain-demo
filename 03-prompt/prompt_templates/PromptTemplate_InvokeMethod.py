import os
import time

from arrow import now
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv(encoding="utf-8")

template = PromptTemplate.from_template("现在的时间是:{time},问题:{question}")
invoke = template.invoke({
     "time":now("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss"),
     "question":"写一个冒泡排序算法,只要代码"
})

print(invoke)
print(type(invoke))

print(invoke.to_string())
print(invoke.to_messages())


