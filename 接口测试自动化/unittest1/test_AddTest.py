import requests
import unittest
class Test_Add(unittest.TestCase):
    def setUp(self):
        print("begin")
    def tearDown(self):
        print("end")
    def test_001(self):
        a=1
        b=1
        self.assertEqual(2,a+b)
        print("test1.......")
    def test_002(self):
        a=2
        b=1
        self.assertEqual(3,a+b)
        print("test2.......")
    def test_003(self):
        a=2
        b=4
        self.assertEqual(6,a+b)
        print("test3.......")
   
if __name__ == '___main___':
    unittest.main()

