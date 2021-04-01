from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.filmin.es/")
driver.maximize_window()

#Boton entrar
driver.find_element_by_css_selector('body > div.layout__header > header > div.site-header--on-desktop.align-items-center > button.ml-3.Button.Button--sm.Button--light.Button--outline').click()
time.sleep(3)
#No recuerdas tu contraseña
driver.find_element_by_css_selector('#modal-login > div.p-5.px-6\@md > form > div.form-group.mb-4 > button').click()
time.sleep(2)
#Ingresar email para recuperacion de contraseña
driver.find_element_by_css_selector('#email').send_keys('correo.prueba.martin@gmail.com')
#Boton de envio de email
driver.find_element_by_css_selector('#reset-form-submit').click()