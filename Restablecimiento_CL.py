from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.niusushi.cl/")
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[1]/header-cart/div/div[1]/div/div[2]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset/input').send_keys('mail@gmail.com')
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset/button').click()
time.sleep(2)