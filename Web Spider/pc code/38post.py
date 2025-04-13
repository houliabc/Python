import requests
import re
from bs4 import BeautifulSoup
url="http://cc.szpt.edu.cn/"
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
res=requests.get(url)
pwd = input('请输入密码：')
a=re.findall('<input .*? id="__VIEWSTATE".*? value="(.*?)".*?',res.text,re.S)[0]
b=re.findall('<input .*? id="__VIEWSTATEGENERATOR".*? value="(.*?)".*?',res.text,re.S)[0]
c=re.findall('<input .*? id="__EVENTVALIDATION".*? value="(.*?)".*?',res.text,re.S)[0]
dt={"TextBoxTeacherName":"刘杰0494",
    "ButtonLogin":"登录",
    "__VIEWSTATE":a,
    "__VIEWSTATEGENERATOR":b,
    "__EVENTVALIDATION":c,
    "TextBoxPassword":pwd}
sss=requests.Session()  #开启session会话
sss.post(url,headers=hd,data=dt)

#有了session之后就畅通无阻了
url_next="http://cc.szpt.edu.cn/IpListStudent.aspx?StudentID=87675"
html=sss.get(url_next)
# print(html.text)

#(包括序号，IP地址和登录时间)方法1：直接
# li=re.findall('<td align="center">.*?>(.*?)<.*?<td align="center"><font .*?>(.*?)</font>.*?<span.*?>(.*?)</span>',html.text,re.S)
# for i in li:
#     for j in i:
#         print(j.strip(),end=' ')
#     print()
#(包括序号，IP地址和登录时间)方法2：间接
li=re.findall('<tr onmouseover=.*?>(.*?)</tr>',html.text,re.S)
for i in li:
    i=re.findall('<font color="#003399">(.*?)</font>',i,re.S)
    no=i[0].strip()
    ip=i[1].strip()
    time=re.findall('<span.*?>(.*?)</span>',i[2].strip(),re.S)[0]
    print(no,ip,time)