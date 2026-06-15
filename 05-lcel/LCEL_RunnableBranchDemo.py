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

template_korean = ChatPromptTemplate.from_messages([("system", "你是一个韩语翻译家"), ("user", "{query}"), ])
template_japan = ChatPromptTemplate.from_messages([("system", "你是一个日语翻译家"), ("user", "{query}"), ])
template_english = ChatPromptTemplate.from_messages([("system", "你是一个英语翻译家"), ("user", "{query}"), ])

def determine_language(inputs):
    """判断语言类型"""
    query = inputs["query"]
    if "日语" in query:
        return "japan"
    elif "韩语" in query:
        return "korean"
    else:
        return "english"
chain = RunnableBranch(
     (lambda inputs: determine_language(inputs) == "japan", template_japan | llm | parser),
     (lambda inputs: determine_language(inputs) == "korean", template_korean | llm | parser),
     (template_english | llm | parser)
 )

test_queries = [
    {"query": "请你用韩语翻译这句话:'见到你很高兴'"},
    {"query": "请你用日语翻译这句话:'见到你很高兴'"},
    {"query": "请你用英语翻译这句话:'见到你很高兴'"}
]

for query in test_queries:
    result = chain.invoke(query)
    print(result)
