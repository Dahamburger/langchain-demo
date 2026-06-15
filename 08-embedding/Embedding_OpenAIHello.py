import os

from dashscope import api_key
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(encoding="utf-8")

input_test = "出租房"
clent = OpenAI(
    api_key = os.getenv("QWEN_API_KEY"),
    base_url = os.getenv("QWEN_BASE_URL")
)
completion = clent.embeddings.create(model="text-embedding-v4", input=input_test)
print("文本向量：", completion.data[0].embedding, sep='')