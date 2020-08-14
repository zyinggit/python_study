import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from Commonlib.commonlib import Common
class Login(Common):
    def login(self,user,pwd):
        self.open_url("http://localhost/iwebshop/index.php?controller=site&action=index")
        self.click("css",".loginfo > a:nth-child(1)")
        self.input_data("name","login_info",user)
        self.input_data("name","password",pwd)
        self.click("class_name","submit_login")
if __name__=="__main__":
    log=Login()
    log.login("zhangying","zy18291767378")