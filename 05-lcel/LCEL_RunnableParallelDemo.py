from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableParallel
from loguru import logger

load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

parser = StrOutputParser()

template1 = ChatPromptTemplate.from_messages([("system", "你是一个只是渊博的计算机专家"), ("user", "请用中文描述一下{topic},简短一点")])
template2 = ChatPromptTemplate.from_messages([("system", "你是一个只是渊博的计算机专家"), ("user", "请用英文描述一下{topic},简短一点")])

chain1 = template1 | llm | parser
chain2 = template2 | llm | parser

parallel_chain = RunnableParallel({
    "chinese": chain1,
    "english": chain2
    })
result = parallel_chain.invoke({"topic": "机器学习"})
logger.info(result)


