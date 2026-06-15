from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# template = ChatPromptTemplate(
#     [
#         {"role": "system", "content": "你是一个很有用的助手"},
#         {"role": "user", "content": "给我讲一个关于{thing}的冷笑话"},
#     ]
# )


template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个很有用的助手"),
        ("placeholder", "{memory}"),
        ("user", "你叫什么名字")
    ]
)
# MessagesPlaceholder 占位符  显示占位
print(type(template))
format_prompt = template.invoke({"memory": [{"role": "system", "content": "我叫小王"}]})
print(format_prompt.to_string())
print(type(format_prompt))
