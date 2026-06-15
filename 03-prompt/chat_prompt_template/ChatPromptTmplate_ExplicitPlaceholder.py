from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# template = ChatPromptTemplate(
#     [
#         {"role": "system", "content": "你是一个很有用的助手"},
#         {"role": "user", "content": "给我讲一个关于{thing}的冷笑话"},
#     ]
# )


# MessagesPlaceholder 占位符  显示占位
template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个很有用的助手"),
        MessagesPlaceholder("memory"),
        ("user", "你叫什么名字"),
    ]
)
print(type(template))
format_prompt = template.invoke({"memory": [{"role": "system", "content": "你叫小王"}]})
# format_prompt = template.invoke({"memory": [HumanMessage("我叫小王"), AIMessage("你好小王")]})
print(format_prompt.to_string())
print(type(format_prompt))
