'''
import requests
#城市空气质量接口
url="http://web.juhe.cn:8080/environment/air/cityair"
para={"city":"上海","key":"1c5890d370c96d568851f1d0bbe6a0db "}
r=requests.get(url,para)
res=r.json()
print(res)
'''
import requests
import unittest
class Test_CityPM(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    def test_001(self):
        #城市空气PM2.5指数接口
        url="http://web.juhe.cn:8080/environment/air/cityair"
        para={"city":"上海","key":"1c5890d370c96d568851f1d0bbe6a0db "}
        r=requests.get(url,para)
        res=r.json()
        print(res)
if __name__ =="__main__":
    unittest.main()