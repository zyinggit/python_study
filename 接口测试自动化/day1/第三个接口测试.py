import requests

url="http://v.juhe.cn/weather/geo"

#根据GPS坐标查询天气，API文档中说明用get/post请求方式，这里用post,文档中说明输入参数必填四项
para={"lon":"116.39277","lat":"39.933748","dtype":"json","key":"0f5e15d089a4f5e7a85138f271f9412b"}
r=requests.post(url,para)
res=r.json()
print(res)
print(res["reason"])

'''
para1={"lon":"116.33","lat":"39.933748","dtype":"json","key":"0f5e15d089a4f5e7a85138f271f94"}
r1=requests.post(url,para1)#构造错误的数据，
#每个测试用例，只需一个错误，其他参数正确,具体根据接口文档设置
res1=r1.json()
print(res1)
'''