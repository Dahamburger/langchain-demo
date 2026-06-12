from langchain_ollama.chat_models import ChatOllama


model = "qwen3.5:9b"
llm = ChatOllama(base_url="http://127.0.0.1:11434", model=model, reasoning=False)
response = llm.invoke("你好")
# response = llm.stream("帮我讲述一下langchain")
# for chunk in response:
#     print(chunk.content, end="")
print(response.content)
