from langchain_community.document_loaders import CSVLoader

file_path = "resource/demo.csv"
loader = CSVLoader(file_path=file_path)
docs = loader.load()
print(docs)
