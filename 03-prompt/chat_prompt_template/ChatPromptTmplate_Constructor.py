from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate(
#     [
#         {"role": "system", "content": "你是一个很有用的助手"},
#         {"role": "user", "content": "给我讲一个关于{thing}的冷笑话"},
#     ]
# )

template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}的助手"),
        ("user", "给我讲一个关于{thing}的冷笑话"),
    ]
)
print(type(template))
# format_prompt = template.format_messages(role ="很有用",thing="python")
format_prompt = template.format_messages(**{"role": "很有用", "thing": "python"}) # <class 'list'>
# format_prompt = template.invoke({"role": "很有用", "thing": "python"}) #<class 'langchain_core.prompt_values.ChatPromptValue'>
# format_prompt = template.format(**{"role": "很有用", "thing": "python"}) #<class 'str'>
print(format_prompt)
print(type(format_prompt))
