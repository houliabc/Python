from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #打开浏览器
driver.implicitly_wait(20)  #隐形等待时间
url='https://passport2.chaoxing.com/login?fid=12&refer=http%3A%2F%2Fi.mooc.chaoxing.com%2Fspace%2Findex%3Ft%3D1731986025808&space=2'
driver.get(url)
time.sleep(0.5)
driver.maximize_window()  #最大化窗口
# print(driver.page_source)  #打印网页源码
time.sleep(0.5)
driver.find_element(By.CLASS_NAME,'ipt-tel').send_keys('13538971422')
driver.find_element(By.CLASS_NAME,'ipt-pwd').send_keys('tm1048EAQ')
driver.find_element(By.CLASS_NAME,'btn-big-blue.margin-btm24').click()
time.sleep(3)
driver.get('https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=204576813&clazzid=103318042&cpi=278536521&enc=4f7740b5d8259d7ff128fe6d0dd13012&t=1731987272176&pageHeader=8&v=0')
time.sleep(1)
driver.close()  #关闭当前窗口
time.sleep(1)
driver.quit()  #关闭浏览器