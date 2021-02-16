import time
from selenium import webdriver
import selenium

driver = webdriver.Chrome(executable_path="C:\Selenium Browser driver\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
driver.find_element_by_css_selector("input[value='radio2']").click()
driver.find_element_by_css_selector("option[value='option1']").click()




driver.find_elements_by_id("")






