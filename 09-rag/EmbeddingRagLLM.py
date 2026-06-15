import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv(encoding="utf-8")
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

prompt_template = """
    请用一下文本提供的内容来回答问题,仅使用提供的文本内容回答
    如果文本中没有,就回答:"抱歉,提供的文本没有这个信息"
    
    文本内容:
    {context}
    
    问题:
    {question}
    
    回答:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# 初始化向量模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    dashscope_api_key=os.getenv("QWEN_API_KEY"),
)

# 加载文档
file_path = "resource/java开发手册.docx"
documents = Docx2txtLoader(file_path=file_path).load()
print(documents)

# # 分割文档
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30, length_function=len)
# split_documents = text_splitter.split_documents(documents)
# print(f"分割文档数量:{len(split_documents)}")
#
# # 创建向量存储
# # 连接到redis并存入向量(自动调用embeddings 嵌入)
# Redis.from_documents()
