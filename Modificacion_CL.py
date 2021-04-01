from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.niusushi.cl/")
driver.maximize_window()

# Rellenado de campos obligatorios: Nombre de Usuario, Correo (recibe cualquier correo que cumpla el formato), cualquier número de 8 digitos y password

driver.find_element_by_xpath('/html/body/div[1]/header-cart/div/div[1]/div/div[2]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/input[1]').send_keys('mail@gmail.com')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/input[2]').send_keys('holamundo1')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/form/button').click()
#Interfaz donde aparece "Cambiar Clave de Acceso"
driver.find_element_by_xpath('/html/body/div[3]/header-cart/div/div[1]/div/div[2]/div[1]').click()
#Cambio de contraseña
time.sleep(2)
driver.get("https://www.niusushi.cl/nueva-password")
time.sleep(2)
element = driver.find_element_by_css_selector("body > div.modal.fade.ng-isolate-scope.in > div > div > div > form > fieldset > div > input")
element.send_keys("holamundo2")
time.sleep(2)
element1 =driver.find_element_by_css_selector('body > div.modal.fade.ng-isolate-scope.in > div > div > div > form > fieldset > button')
element1.click()
time.sleep(5)
driver.quit()

