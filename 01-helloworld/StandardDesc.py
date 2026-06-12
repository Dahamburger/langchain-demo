import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
# 配置日志
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv(encoding="utf-8")

def init_llm():
    QWEN_API_KEY = os.getenv("QWEN_API_KEY")
    # QWEN_BASE_URL = os.getenv("QWEN_BASE_URL")
    if not QWEN_API_KEY:
        raise ValueError("环境变量apikey没有设置,请前往设置")

    llm = init_chat_model(
        model="qwen-plus",
        model_provider="openai",
        api_key=QWEN_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    return llm
def main():
    try:
        llm = init_llm()
        question = "你是谁"
        response = llm.invoke(question)
        logging.info(f"问题:{ question}")
        logging.info(f"回复:{ response}")
        print("*"*30)
        print("=========以下是流式输出=========")
        responseStream = llm.stream(question)
        for chunk in responseStream:
            print(chunk.content, end="")
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()