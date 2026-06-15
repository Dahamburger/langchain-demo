from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda
from loguru import logger
load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def debug_print(x):
    logger.info(f"中间结果:{x}")
    return {"input": x}


parser = StrOutputParser()

template1 = ChatPromptTemplate.from_messages([("system", "你是一个只是渊博的计算机专家"), ("user", "请用中文描述一下{topic},简短一点")])
template2 = ChatPromptTemplate.from_messages([("system", "你是一个翻译家,把下面内容翻译成英文"), ("user", "{input}")])

chain1 = template1 | llm | parser
chain2 = template2 | llm | parser

runnable_lambda = RunnableLambda(debug_print)
# full_chain = chain1 | debug_print | chain2
full_chain = chain1 | runnable_lambda | chain2
result = full_chain.invoke({"topic": "机器学习"})
logger.info(f"最终结果:{result}")


