from langchain_community.document_loaders import Docx2txtLoader

file_path = "resource/demo.docx"
loader = Docx2txtLoader(file_path=file_path)
docs = loader.load()
print(docs)
