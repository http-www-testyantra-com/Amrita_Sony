import time

from Python_sony_training.tests import *
from Python_sony_training.page.home_page import Home_Page
from Python_sony_training.tests.common_call import invoke_browser

def test_2(driver):
    time.sleep(5)
    hp=Home_Page(driver)
    hp.getHeaderText("//span[@class='_1QZ6fC _3Lgyp8']",'xpath')
    hp.getText()
    # for select_header in all_header:
    #     print(select_header.text)
    print("test case2 runnig using driver")

test_2("https://www.flipkart.com/")