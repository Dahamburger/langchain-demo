import os
from typing import Annotated

from dotenv import load_dotenv
from openai.types.chat.chat_completion_message import Annotation
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(encoding="utf-8")
# 定义数据模型
# class NewsEvent(BaseModel):
#     # time: str = Field(description="新闻发生的时间")
#     person: str = Field(description="新闻涉及的人物")
#     event: str = Field(description="发生的具体事件")
#     region: str = Field(description="新闻发生所在的地区")

class NewsEvent(BaseModel):
    # time: str = Field(description="新闻发生的时间")
    person: Annotated[str, "新闻涉及的人物"]
    event: Annotated[str, "发生的具体事件"]
    region: Annotated[str, "新闻发生所在的地区"]

# 创建解析器
parser = PydanticOutputParser(pydantic_object=NewsEvent)
instructions = parser.get_format_instructions()

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的助手。{format_instructions}"),
    ("human", "{question}")
]).partial(format_instructions = instructions)

# 调用 LLM
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    # temperature=0.5
)
invoke = llm.invoke(prompt.format_prompt(question="今天是2023年5月1日,请给我一个关于2023年5月1日的新闻事件"))
print(type(invoke))
print(invoke.content)

