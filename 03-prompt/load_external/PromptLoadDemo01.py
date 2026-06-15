from langchain_core.prompts import load_prompt

prompt = load_prompt(path="prompt.json", encoding="utf-8")
# format_template = prompt.format(name = "小王",what = "小王子")
format_template = prompt.invoke({"name": "小王", "what": "小王子"})
print(format_template)
