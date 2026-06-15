import os

import redis
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnableConfig
from loguru import logger

REDIS_URL = "redis://127.0.0.1:26379"
# 创建redis客户端 decode_response设置为 True表示获取到的数据为字符串,设置为 False表示获取到的数据为字节
redis_clint = redis.Redis.from_url(REDIS_URL, decode_responses=True ,encoding = "utf-8")
# print(redis_clint.ping())
load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

#创建提示词模版
template = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])
def get_session_redis(session_id: str)-> RedisChatMessageHistory:
    """获取或者创建会话历史(使用redis)"""
    #创建Redis历史对象
    history = RedisChatMessageHistory(
        session_id=session_id,
        url=REDIS_URL,
    )
    return history

# 创建带历史的链
history_chain = RunnableWithMessageHistory(
    template | llm,
    get_session_redis,
    input_messages_key="question",
    history_messages_key="history"
)
# 配置
# session就是登录大模型的账各自用户,类似于手机号,邮箱
config = RunnableConfig(configurable = {"session_id": "user_001"})

#主循环
while True:
    print("\n" + "=" * 50)
    question = input("请输入问题:")
    if question.lower() in ["exit","quit","q"]:
        break
    response = history_chain.invoke({"question":question}, config)
    logger.info(f"AI回答:{response.content}")

    # 等同于redis-cli的save命令,强制写入dump.rdb
    redis_clint.save()
