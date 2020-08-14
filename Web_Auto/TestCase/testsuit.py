import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
import unittest
from TestCase.testcase import Test
from Commonlib.HTMLTestRunner import HTMLTestRunner
class SuitTest(unittest.TestCase):
    def test_suit(self):
        mysuit=unittest.TestSuite()
        case_list=['test_001','test_002','test_003','test_004','test_005']
        for case in case_list:
            mysuit.addTest(Test(case))
        #unittest.TextTestRunner(verbosity=2).run(mysuit)
        with open('report.html','wb') as f:
            HTMLTestRunner(
                stream=f,
                title='第一个测试报告',
                description='实现iwebshop前台登陆功能的web自动化测试',
                verbosity=2).run(mysuit)
if __name__ == "__main__":
    unittest.main()
