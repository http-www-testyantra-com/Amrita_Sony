# Scenario 14
# 1.	Open browser
# 2.	Enter URL(bluestone)
# 3.	move to Gold coins
# 4.	Select 1 Gm
# 5.	Verify 1Gm Coin is displaying or not
# 6.	close Browser
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Bluestone1():
    def blustone_1gram_GoldCoin(self):
        # Opening the browser
        self.driver=webdriver.Chrome()
        # wait 2sec
        time.sleep(2)
        # open the bluestone website
        self.driver.get("https://www.bluestone.com/")
        # Maximise the bluestone window
        self.driver.maximize_window()
        # provide the wait implicitly
        self.driver.implicitly_wait(5)
        time.sleep(2)
        ele=self.driver.find_element_by_xpath("//a[text()='Coins ']")
        act=ActionChains(self.driver)
        time.sleep(5)
        act.move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//span[text()='1 gram'])[1]").click()
        # c=lambda xpath,driver:driver.find_element_by_xpath(xpath).click()
        # c("(//span[@data-p='silver-coins-weight-10gms,m'])[1]",driver)
        # driver.find_element(By.XPATH,"(//span[text()='1 gram'])[1]").click()

        actual_ele=self.driver.find_element_by_xpath("//h1[text()='1 gram 24 KT Gold Coin']").text
        expected_ele='1 gram 24 KT Gold Coin'

        assert actual_ele==expected_ele, print("invalid product")
        print("valid product")
goldCoin=Bluestone1()
goldCoin.blustone_1gram_GoldCoin()