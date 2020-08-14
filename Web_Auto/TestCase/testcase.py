import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
import unittest
from Business.Login import Login
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("finish")
    def test_001(self):
        log=Login()
        log.login("zhangying","zy18291767378")
        data=log.get_text("css",".loginfo")
        #self.assertEqual("zhangying您好，欢迎您来到iwebshop购物！[安全退出]",data)
        self.assertIn("zhangying",data)
    def test_002(self):
        log=Login()
        log.login("","")
        data=log.get_text("css",".invalid-msg")
        self.assertEqual("填写用户名或邮箱",data)
    def test_003(self):
        log=Login()
        log.login("zhangying","")
        data=log.get_text("css",".invalid-msg")
        self.assertEqual("填写密码",data)
    def test_004(self):
        log=Login()
        log.login("","zy18291767378")
        data=log.get_text("css",".invalid-msg")
        self.assertEqual("填写用户名或邮箱",data)
    def test_005(self):
        log=Login()
        log.login("zhangying","zy18291767378#")
        data=log.get_text("css",".prompt")
        self.assertIn("用户名和密码不匹配",data)
    def test_006(self):
        log=Login()
        log.login("zhangying#","zy18291767378")
        data=log.get_text("css",".prompt")
        self.assertIn("用户名和密码不匹配",data)
#if __name__=="__main__":
#    unittest.main()