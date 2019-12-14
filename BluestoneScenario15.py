# Scenario 15
# 1.	Open browser
# 2.	Enter URL(bluestone)
# 3.	move to Gold coins
# 4.	 Go to plain gold coins and Select 2 Gm
# 5.	Verify 2Gm Coin is displaying or not.
# 6.	close Browser

# Opening the browser
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

class Bluestone():
    def blustone_2gram_GoldCoin(self):
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
        click_coin=self.driver.find_element_by_xpath("//a[text()='Coins ']")
        act=ActionChains(self.driver)
        time.sleep(5)
        act.move_to_element(click_coin).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//span[text()='2 gram'])[1]").click()

        actual_ele = self.driver.find_element_by_xpath("//h1[text()='2 gram 24 KT Gold Coin']").text
        expected_ele = '2 gram 24 KT Gold Coin'

        assert actual_ele == expected_ele, print("invalid product")
        print("valid product")

goldCoin=Bluestone()
goldCoin.blustone_2gram_GoldCoin()


