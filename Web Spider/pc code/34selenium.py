from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #打开浏览器
driver.implicitly_wait(20)  #隐形等待时间
url='http://www.baidu.com'
driver.get(url)
time.sleep(0.5)
driver.maximize_window()  #最大化窗口
# print(driver.page_source)  #打印网页源码
time.sleep(0.5)
driver.find_element(By.ID,'kw').clear()  #清楚当前内容，当然目前没有内容
driver.find_element(By.ID,'kw').send_keys('python')  #输入信息
driver.find_element(By.CLASS_NAME,'bg.s_btn').click()  #点击
time.sleep(3)
driver.close()