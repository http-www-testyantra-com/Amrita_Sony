from selenium.webdriver.common.by import By

class Action_Check():
    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
      return  self.driver.title

    def getByType(self,locator_type):
        locator_type=locator_type.lower()
        if locator_type=='id':
            return By.ID
        elif locator_type=='name':
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        else:
            return By.LINK_TEXT

    def getElement(self,locator,locator_type):
        element=None
        locator_type=locator_type.lower()
        byType = self.getByType(locator_type)
        element = self.driver.find_element(byType, locator)

    def getElements(self,locator,locator_type):
        element=None
        locator_type=locator_type.lower()
        byType = self.getByType(locator_type)
        element = self.driver.find_elements(byType, locator)

    def getText(self,elements):
        for i in range(len(elements)):
            elements[i].text()



    def elementClick(self, locator, locator_type="id"):
            element = self.getElement(locator, locator_type)
            element.click()

    def sendKeys(self, data, locator, locator_type="id"):
         element = self.getElement(locator, locator_type)
         element.send_keys(data)







