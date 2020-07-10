from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)
        self.driver.find_element_by_class_name('Ckrof').click()
        sleep(5)

InstaBot('jenn.seibert', pw)
