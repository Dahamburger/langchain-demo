from langchain.tools import tool

@tool
def add (a,b):
    """计算两个数的和"""
    return a+b


result = add.invoke({"a":1,"b":2})
print(result)
