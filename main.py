# import pytest
#
#
# #@pytest.mark.smoke
#
# def test_firstprogram():
#     print("hell")
#
#


import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Practise(object):
    def test_browser(self):
        driver = webdriver.Chrome(executable_path="C:\Selenium Browser driver\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.find_element_by_css_selector("input[type='text']").send_keys("myname is billaaa ")
        driver.find_element_by_css_selector("input[type='text']").send_keys(Keys.ENTER)

        print(driver.title)


run = Practise()
run.test_browser()

def test_demo():
    print("My name is Billa")


