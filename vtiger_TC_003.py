import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Vtiger_Invoice_Product():
    def Invoice_LastViewed_edit_Product(self):
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

        self.driver.find_element_by_name("Edit").click()
        time.sleep(5)

        select_product_category=self.driver.find_element_by_xpath("//Select[@name='productcategory']")
        sel=Select(select_product_category)

        sel.select_by_index(1)
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@title='Last Viewed']").click()
        self.driver.find_element_by_xpath("//a[text()='laptop']").click()

        actual_text=self.driver.find_element_by_xpath("//font[text()='Hardware']").text
        expected_text="Hardware"
        assert expected_text==actual_text, print("Not matching")
        print("Its edited and saved")

        self.driver.close()

vtiger2=Vtiger_Invoice_Product()
vtiger2.Invoice_LastViewed_edit_Product()