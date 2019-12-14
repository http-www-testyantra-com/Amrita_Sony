from selenium import webdriver


def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        func(driver)
        driver.close()
    return inner
