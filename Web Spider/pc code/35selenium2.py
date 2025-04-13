from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #打开浏览器
driver.implicitly_wait(20)  #隐形等待时间
url='https://news.baidu.com/'
driver.get(url)
time.sleep(0.5)
driver.maximize_window()  #最大化窗口
# print(driver.page_source)  #打印网页源码
time.sleep(0.5)
driver.find_element(By.CLASS_NAME,'a3').click()  #点击
time.sleep(3)
ww=driver.window_handles  #捕获当前所有窗口，返回的是列表
driver.switch_to.window(ww[0])    #跳转到目前的第一个网页
time.sleep(3)
driver.close()  #关闭当前窗口
time.sleep(1)
driver.quit()  #关闭浏览器