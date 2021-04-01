from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.filmin.es/")
driver.maximize_window()

#Boton entrar
driver.find_element_by_css_selector('body > div.layout__header > header > div.site-header--on-desktop.align-items-center > button.ml-3.Button.Button--sm.Button--light.Button--outline').click()
time.sleep(3)
#Boton REGISTRATE
driver.find_element_by_css_selector('#modal-login > div.px-5.px-6\@md.pb-4 > div > button').click()
time.sleep(2)
#Email, acepta cualquiera
driver.find_element_by_css_selector('#email').send_keys('correo.prueba.martin@gmail.com')
#Elige nombre de usuario (no se puede repetir)
driver.find_element_by_css_selector('#username').send_keys('martinprueba')
#Contraseña
driver.find_element_by_css_selector('#password').send_keys('123456')
#Boton crear cuenta
driver.find_element_by_css_selector('#modal-register > div.p-5.px-6\@md > form > div.mb-3 > button > span').click()
#Si es la primera vez iniciando la cuenta, boton "mas tarde"
time.sleep(2)
driver.find_element_by_css_selector('#filmin-modal > div > div.c-modal__content > div.text-center.mt-4 > button').click()