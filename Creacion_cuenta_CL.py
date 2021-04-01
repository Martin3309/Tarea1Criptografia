from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.niusushi.cl/")
driver.find_element_by_xpath('/html/body/div[1]/header-cart/div/div[1]/div/div[2]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[1]').send_keys('test')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[2]').send_keys('mail@gmail.com')
#Si o si exige 8 caracteres el numero de telefono
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div/div[2]/input').send_keys('46545645')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[3]').send_keys('holaaaa')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/button').click()

time.sleep(2)










