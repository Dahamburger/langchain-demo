import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import ChatMessage
from langchain_core.output_parsers import JsonOutputParser, JsonOutputKeyToolsParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from QueryWeatherTool import get_weather

load_dotenv(encoding="utf-8")

llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

llm_bind_tools = llm.bind_tools([get_weather])

#创建解析器用于提取工具调用结果中的JSON数据
# parser = JsonOutputKeyToolsParser(key_name="get_weather.name",first_tool_only= True)

#构建工具调用链
# get_weather_chain = llm_bind_tools | parser | get_weather
get_weather_chain = llm_bind_tools
weather_json = get_weather_chain.invoke("请问今天上海天气怎么样")
# print(weather_json)

output_template = ChatPromptTemplate.from_template("""
你将收到一段 JSON 格式的天气数据{weather_json}，请用简洁自然的方式将其转述给用户。
以下是天气 JSON 数据：
请将其转换为中文天气描述，例如：
“北京现在天气：多云，气温 28℃，体感有点闷热（约 32℃），湿度 75%，微风（东南风 2 米/秒），
能见度很好，大约 10 公里。建议穿短袖短裤。适合做户外运动。”
""")

output_parser = StrOutputParser()

#构建最终输出链:提示词模版->工具调用链->解析器->输出解析器
output_chain = output_template | llm | output_parser
final_chain = get_weather_chain | (lambda x: {"weather_json": x}) | output_chain
result = final_chain.invoke("深圳今天天气如何?")
print(result)
