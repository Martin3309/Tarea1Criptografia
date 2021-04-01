from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

for n in range(0,100):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.niusushi.cl/")
    driver.maximize_window()
    # Rellenado de campos obligatorios: Nombre de Usuario, Correo (recibe cualquier correo que cumpla el formato), cualquier número de 8 digitos y password
    driver.find_element_by_xpath('/html/body/div[1]/header-cart/div/div[1]/div/div[2]/div[1]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/input[1]').send_keys('correo.prueba.martin@gmail.com')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/input[2]').send_keys('123456')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/button').click()
    time.sleep(2)
    driver.quit()
