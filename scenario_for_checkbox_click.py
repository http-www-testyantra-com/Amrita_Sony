import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/login.do")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()
time.sleep(5)

try:
    sel=driver.find_element_by_xpath("//td[@class='listtblcolheader_submit_tt']")
    sel1=Select(sel)
    sel1.select_by_visible_text("fhdf")
except:
    print("UnexpectedTagNameException")

