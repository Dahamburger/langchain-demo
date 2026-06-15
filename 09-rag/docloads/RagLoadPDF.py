from langchain_community.document_loaders import PyPDFLoader

file_path = "resource/demo.pdf"
loader = PyPDFLoader(
    file_path = file_path,
    extraction_mode = "plain"
)
docs = loader.load()
print(docs)