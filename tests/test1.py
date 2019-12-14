import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Python_sony_training.page.home_page import *
from Python_sony_training.tests.common_call import invoke_browser


# def invoke_browser(func):
#     def inner(url):
#         driver=webdriver.Chrome()
#         driver.get(url)
#         driver.implicitly_wait(5)
#         driver.maximize_window()
#         driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
#         func(driver)
#         driver.close()
#     return inner

@invoke_browser
def test_1(driver):
    hp = Home_Page(driver)
    hp.getTextMobiles("//input[@type='text']","xpath")

test_1("https://www.flipkart.com/")