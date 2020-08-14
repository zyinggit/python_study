# 导包
import requests
import re
#接口地址
url2 = "http://192.168.103.106:1080/webtours/nav.pl?in=home"
s = requests.session()# 为了保持和下一个接口建立相同的连接通道
res = s.get(url2)
# print(res.text)

#正则匹配，(.+?)是需要匹配的值，括号内的值表明是匹配的数据有多位，name=userSession value=是需要匹配的数据左侧的值，>是需要匹配的数据右侧的值
usersession = re.findall(r'name=userSession value=(.+?)>',res.text)
print(usersession)
# para2 ={"in":"home"}
# 接口地址
url ="http://192.168.103.106:1080/webtours/login.pl"
para ={"userSession":usersession[0],"username":"jojo","password":"bean","login.x":"54","login.y":"11","login":"Login","JSFormSubmit":"off"}
r = s.post(url,data=para)
# 发送post请求
# r = requests.post(url,data=para)
print(r.text)