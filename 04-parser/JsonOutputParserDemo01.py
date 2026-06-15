import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(encoding="utf-8")
# 定义数据模型
class NewsEvent(BaseModel):
    time: str = Field(description="新闻发生的时间")
    person: str = Field(description="新闻涉及的人物")
    event: str = Field(description="发生的具体事件")

# 创建解析器
parser = PydanticOutputParser(pydantic_object=NewsEvent)
instructions = parser.get_format_instructions()

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的助手。{format_instructions}"),
    ("human", "{question}")
])

# 调用 LLM
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# chain = prompt | llm | parser
invoke = llm.invoke(prompt.format(format_instructions = instructions, question="帮我讲解一下小米汽车最近的的舆论事件"))
# print(invoke)
parser_invoke = parser.invoke(invoke)

print(parser_invoke)

# result = chain.invoke({"question": "小米汽车最近的的舆论时间"})
# result 直接是一个 NewsEvent 对象，而不是字典

