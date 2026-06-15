from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch

 
load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

parser = StrOutputParser()

template1 = ChatPromptTemplate.from_messages([("system", "你是一个很有用的助手"), ("user", "{question}")])
template2 = ChatPromptTemplate.from_messages([("system", "你是一个英语翻译家,请把下面的这段话翻译成英文"), ("user", "{input}")])


chain1 = template1 | llm | parser
chain2 = template2 | llm | parser

full_chain = chain1 | (lambda x: {"input": x}) | chain2
result = full_chain.stream({"question": "告诉我langchain是什么东西"})
for chunk in result:
    print(chunk, end="")

