from langchain_community.document_loaders import JSONLoader
file_path = "resource/demo.json"
loader = JSONLoader(file_path=file_path,jq_schema = ".",text_content= False)
docs = loader.load()
print(docs)