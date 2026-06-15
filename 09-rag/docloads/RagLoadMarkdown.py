from langchain_community.document_loaders import TextLoader

file_path = "resource/demo.md"
encoding = "utf-8"
loader = TextLoader(file_path, encoding)
docs = loader.load()
print(docs)
