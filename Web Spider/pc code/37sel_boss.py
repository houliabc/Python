from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver=webdriver.Chrome()  #打开浏览器
driver.implicitly_wait(20)  #隐形等待时间
url='https://www.zhipin.com/shenzhen/'
driver.get(url)
time.sleep(1)
# driver.maximize_window()  #最大化窗口
# time.sleep(0.5)

driver.find_element(By.CLASS_NAME,'ipt-search').send_keys("爬虫\n")
time.sleep(3)

job=driver.find_elements(By.CLASS_NAME,'job-name')
area=driver.find_elements(By.CLASS_NAME,'job-area')
salary=driver.find_elements(By.CLASS_NAME,'salary')
li=driver.find_elements(By.CLASS_NAME,'tag-list')
# print(driver.page_source)
# li=re.findall('<ul .*?class="tag-list"><li .*?>(.*?)</li>.*？<li .*?>(.*?)</li></ul>',driver.page_source,re.S)
# pp
# for i in li:
#     print(i.text)
# level=driver.find_elements(By.CLASS_NAME,'')

for i in range(len(job)):
    print(job[i].text,area[i].text,salary[i].text,li[i].text,'\n',"-"*30)

time.sleep(1)
driver.quit()