#导包
import requests

#定义接口地址（聚合数据网中的全国天气预报接口，根据其API文档确定测试用例（输入参数，返回预期结果）进行测试）
url="http://v.juhe.cn/weather/index"
#输入接口的参数（更改cityname查询不同城市的天气预报，key是获取到该接口时自己的key值）
para={"cityname":"西安","key":"0f5e15d089a4f5e7a85138f271f9412b"}
#发送请求，输入正确的接口地址和正确地参数
r=requests.get(url,para)
#打印状态码
print(r.status_code)
#获取json数据
res=r.json()
print(res)
print(res['reason'])

'''
#模拟错误的测试用例，输入错误的参数：正确的城市名，错误的key值
url="http://v.juhe.cn/weather/index"
para={"cityname":"西安","key":"0f5e15d089a4f5e7a85138f271f9412"}
r=requests.get(url,para)
print(r.status_code) 
 #输入错误的参数，状态码也返回200,要想看请求的结果是否正确，可通过json返回数据中的"error_code"参数值来判断
res=r.json()
print(res)
#可以通过'resultcode'， 'reason'，'error_code'这些参数的值作为实际结果与预期结果来进行判断
#所以只需要写好测试用例，根据测试用例的数据来测试就行
'''
