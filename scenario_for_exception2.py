import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost/login.do")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()
time.sleep(5)
driver.find_element_by_xpath("(//div[@class='label'])[2]").click()
driver.find_element_by_xpath("(//div[@class='checkbox inactive'])[1]")
driver.find_element_by_xpath("(//div[@class='label'])[1]").click()