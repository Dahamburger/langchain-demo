from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1.准备文本
content = (
"在RAG准备阶段，LangChain通过文档加载器对各种格式的文档进行加载，转换为LangChain中的文档对象。"
"对文档对象进行分割，根据分割规则，分割成文档片段。"
"将文档片段通过文本嵌入模型组件，转换为向量，通过向量数据库组件，保存到向量数据库。"
"在RAG的使用阶段，用户首先提出问题，使用文本嵌入模型组件，将提问文本转换为向量数据，通过向量数据库检索器组件，进行相似性检索，返回关联的文本片段。"
"将相关的文档片段内容渲染到提示词模板中，作为提问问题的上下文传递给大模型，在上下文里做“阅读-理解-整合-生成”，最后把整理好的答案返回给用户。"
)

# 2.定义递归文本分割器
# 使用RecursiveCharacterTextSplitter创建文本分割器，设置块大小为100，重叠长度为30，
# length_function=len就是指定使用 Python 内置的len()函数来计算文本长度，也是这个分割器的默认值
# 比如，print(len("大模型RAG技术")) # 输出8，因为统计的是字符个数（中文字符、字母、符号各算1个）
# 遵循“重叠后向前取有效内容、且不生成过小碎片”的核心分割逻辑，不会让最后一个片段的有效内容只剩扣除重叠后的少量字符
# 原始文本->split_text->第一次分割成字符串块->creat_documents->对字符串块二次分割->内容有可能丢失
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30, length_function=len)

# 3.分割文本
# 将原始文本分割成多个文本块
splitter_text = text_splitter.split_text(content)
# print(type(splitter_text))

# 4.手动转成document对象
# 将切割后的文本转换为文档对象列表
# splitter_documents = text_splitter.create_documents(splitter_text)
splitter_documents = [Document(page_content=text)for text in splitter_text]

print(f"原始文本大小:{len(content)}")
print(f"文本分割数量:{len(splitter_documents)}")
for splitter_document in splitter_documents:
    print(f"文档大小:{len(splitter_document.page_content)},文档内容:{splitter_document.page_content}")

