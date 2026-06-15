import json
import os

import httpx
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv(encoding="utf-8")

@tool
def get_weather(loc):
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称。
                注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，
                则 loc 参数需要输入 'Beijing'/'shanghai'。
    :return: OpenWeather API 查询即时天气的结果。具体 URL 请求地址为:
             https://home.openweathermap.org/users/sign_in。
             返回结果对象类型为解析之后的 JSON 格式对象，并用字符串形式进行表示，
             其中包含了全部重要的天气信息。
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY 未设置")

    #step1 构造请求的url
    url = "https://api.openweathermap.org/data/2.5/weather"

    #step2 构造请求的参数
    params = {
        "q": loc,
        "appid": api_key,
        "units": "metric",
        "lang": "zh_cn",
    }
    #step3 发送请求
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    # print(response)

    #step4 解析响应内容为JSON格式 并序列化为字符串返回
    data = response.json()
    print(json.dumps(data))
    return json.dumps(data)
    # return response

#测试
if __name__ == '__main__':
    # get_weather.invoke("beijing")
    get_weather.invoke({"loc":"beijing"})
