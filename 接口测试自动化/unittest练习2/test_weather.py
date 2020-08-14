import requests
import unittest
class Test_weather(unittest.TestCase):
    def setUp(self):
        print("start!")
    def tearDown(self):
        print("finish!")
    
    def test_001(self):
        url="http://v.juhe.cn/weather/geo"
        #根据GPS坐标查询天气，API文档中说明用get/post请求方式，这里用post,文档中说明输入参数必填四项
        para={"lon":"116.39277","lat":"39.933748","dtype":"json","key":"0f5e15d089a4f5e7a85138f271f9412b"}
        r=requests.post(url,para)
        res=r.json()
        value2="successed!"
        self.assertEqual(res["reason"],value2)
        print("test001......")

    def test_002(self):
        #定义接口地址（聚合数据网中的全国天气预报接口，根据其API文档确定测试用例（输入参数，返回预期结果）进行测试）
        url="http://v.juhe.cn/weather/index"
        #输入接口的参数（更改cityname查询不同城市的天气预报，key是获取到该接口时自己的key值）
        para={"cityname":"北京","key":"0f5e15d089a4f5e7a85138f271f9412b"}
        #发送请求，输入正确的接口地址和正确地参数
        r=requests.get(url,para)
        #获取json数据
        res=r.json()
        value3="successed!"
        self.assertEqual(res["reason"],value3)
        print("test002......")
  
if __name__ == "__main__":
    unittest.main()