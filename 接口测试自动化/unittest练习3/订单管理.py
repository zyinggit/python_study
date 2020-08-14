'''
import requests
import unittest

class Test_Orders(unittest.TestCase):
    def test_001(self):
        url="http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
        r=requests.post(url)
        res=r.json()
        print(res)
if __name__ == '__main__':
    unittest.main()
'''
# 导包
import requests
import unittest
class Test_Order(unittest.TestCase):
    def test01(self):
        url ="http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
        r = requests.post(url)
        r.encoding = 'gbk'
        res = r.json()
        #print(res)
        self.assertEqual(res["company"],"韵达快递")
        # 判断是否签收
        print(res["data"])
        print(res["data"][0])
        print(res["data"][0]["context"])
        self.assertIn("已签收",res["data"][0]["context"])

if __name__ == '__main__':
    unittest.main()