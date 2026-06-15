import json
import os

import dashscope
from dotenv import load_dotenv

load_dotenv()
# print("DashScope API Key: ", os.getenv("QWEN_API_KEY"))
input_text = "你好"
resp = dashscope.MultiModalEmbedding.call(
    model="tongyi-embedding-vision-plus",
    input=[{"text": input_text}],
    api_key=os.getenv("QWEN_API_KEY")
)
print(resp.status_code)
# 处理模型返回结果，提取关键信息并格式化输出
if resp.status_code == 200:
    result = {
        "status_code": resp.status_code,
        "request_id": getattr(resp, "request_id", ""),
        "code": getattr(resp, "code", ""),
        "message": getattr(resp, "message", ""),
        "output": resp.output,
        "usage": resp.usage
    }
    print(json.dumps(result, ensure_ascii=False, indent=4))

print("==============================")
print()