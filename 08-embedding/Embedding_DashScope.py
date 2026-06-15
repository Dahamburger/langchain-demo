from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
import os
load_dotenv()
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    # other params...
    dashscope_api_key= os.getenv("QWEN_API_KEY"),
)

text = "This is a test document."

query_result = embeddings.embed_query(text)
print("文本向量长度：", len(query_result), sep='')

doc_results = embeddings.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')