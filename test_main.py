from selenium import webdriver
import time

class alerrt:
    def alertpopu():
        driver = webdriver.Chrome(executable_path="C:\Selenium Browser driver\chromedriver.exe")
        driver.get("https://matches.tamilmatrimony.com/myhome")
        driver.find_element_by_id('MIDP').send_keys("rameshkumar.c.mts@gmail.com")
        driver.find_element_by_id('PASSWORD2').send_keys("kalaikathir")
        driver.find_element_by_xpath('//*[@value="LOGIN"]').click()
        driver.find_element_by_xpath('//*[contains(text(),"M7265703")]').click()
        time.sleep(6)
        driver.get("https://profile.tamilmatrimony.com/profiledetail/myprofile.php")
        driver.find_element_by_xpath('//*[@id="abotmembermenulink"]').click()
        time.sleep(6)
        # to find insta id.........
        txt = []
        txt = driver.find_element_by_xpath('//*[@id="DESCRIPTION1"]').text
        print(txt)
        text = txt.find("c.r.k.007")
        print(text)
        # if insta id is not present --it return -1..so it execuete below code
        if text == -1:
            driver.find_element_by_xpath('//*[@id="DESCRIPTION1"]').send_keys(" insta-c.r.k.007")
            driver.find_element_by_xpath('//*[@id="prdescsave"]').click()
        time.sleep(6)
        driver.close()

obj = alerrt
obj.alertpopu()
