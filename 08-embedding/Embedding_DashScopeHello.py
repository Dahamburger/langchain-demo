import os

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
import dashscope

load_dotenv()
# print(os.getenv("QWEN_API_KEY"))
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    # other params...
    dashscope_api_key= os.getenv("QWEN_API_KEY"),
)

text = "This is a test document."
# resp = dashscope.TextEmbedding.call(
#     model="text-embedding-v4",
#     input=text,
#     api_key=os.getenv("QWEN_API_KEY")
# )
# if resp.status_code == 200:
#     print(resp)


query_result = embeddings.embed_query(text)
print("文本向量：", query_result, sep='')
print("文本向量长度：", len(query_result), sep='')

# doc_results = embeddings.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ])
# print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')