from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.filmin.es/")
driver.maximize_window()

#Boton entrar
driver.find_element_by_css_selector('body > div.layout__header > header > div.site-header--on-desktop.align-items-center > button.ml-3.Button.Button--sm.Button--light.Button--outline').click()
#Ingresar mail
time.sleep(3)
driver.find_element_by_css_selector('#login-username').send_keys('correo.prueba.martin@gmail.com')
#Ingresar contraseña
driver.find_element_by_css_selector('#login-password').send_keys('123456')
#Boton de ingreso
driver.find_element_by_css_selector('#modal-login > div.p-5.px-6\@md > form > button').click()
#Botón "Mas tarde": Si es que es un correo nuevo (primer inicio de sesion)
#driver.find_element_by_css_selector('#filmin-modal > div > div.c-modal__content > div.text-center.mt-4 > button').click()
#Icono de perfil
time.sleep(3)
driver.find_element_by_css_selector('#desktopMenuUserDropdown').click()
time.sleep(2)
#Configuracion
driver.find_element_by_css_selector('body > div.layout__header > header > div.site-header--on-desktop.align-items-center > div:nth-child(6) > div > div > div > a:nth-child(4)').click()
#Solicitar canmbio de contraseña
time.sleep(2)
driver.find_element_by_css_selector('body > main > div.o-grid.o-grid--large.mt-3.mb-5 > div:nth-child(3) > div > div:nth-child(2) > div.flex-shrink-0.text-right\@md > form > button').click()
#Al darle click a ese boton se despliega el mensaje "Te hemos enviado por correo el enlace para restablecer tu contraseña"