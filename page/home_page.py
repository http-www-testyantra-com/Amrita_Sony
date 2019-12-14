from Python_sony_training.base.base_methods import *
from Python_sony_training import *

class Home_Page(Action_Check):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def getTextMobiles(self,locator, locator_type='xpath'):
        Action_Check.getElement(locator, locator_type)

    def getHeaderText(self,locator,locator_type='xpath'):
         Action_Check.getElements(locator,locator_type)
