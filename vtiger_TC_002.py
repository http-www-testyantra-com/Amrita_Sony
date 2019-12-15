import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Vtiger_Invoice():
    def Invoice_LastViewed_edit_Campaignname(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8888/index.php")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element_by_name("user_name").send_keys("admin")
        self.driver.find_element_by_name("user_password").send_keys("manager", Keys.ENTER)

        time.sleep(5)
        click_more = self.driver.find_element_by_xpath("//a[text()='More']")
        act = ActionChains(self.driver)
        act.move_to_element(click_more).perform()

        self.driver.find_element_by_name("Invoice").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//img[@title='Last Viewed']").click()
        self.driver.find_element_by_xpath("//a[text()='laptop']").click()
        time.sleep(5)

        self.driver.find_element_by_name("Edit").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(//input[@class='detailedViewTextBox'])[7]").send_keys("Dell")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        self.driver.close()
vtiger_edit=Vtiger_Invoice()
vtiger_edit.Invoice_LastViewed_edit_Campaignname()