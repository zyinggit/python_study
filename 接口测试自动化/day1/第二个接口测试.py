import requests

'''
url="http://v.juhe.cn/weather/uni"
#查询天气种类及标识列表，根据API文档，只需输入一个参数
para={"key":"0f5e15d089a4f5e7a85138f271f9412b"}
r=requests.get(url,para)
res=r.json()
print(res)
print(res['reason'])
'''

#构造错误的测试用例，输入错误的key值
url="http://v.juhe.cn/weather/uni"
para={"key":"0f5e15d089a4f5e7a85138f271f941"}
r=requests.get(url,para)
res=r.json()
print(res)



