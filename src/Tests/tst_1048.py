from Functions.Functions import Functions
import unittest
import time
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium import webdriver
#from selenium.webdriver.common.by import By
from Functions.Inicializar import Inicializar

#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions as EC
##from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
#from selenium.common.exceptions import NoSuchWindowException
#from selenium.common.exceptions import TimeoutException

#from Pages.Thonet_login import Login as thonetLogin
#import selenium


class Test_1048(unittest.TestCase, Functions):


    def setUp(self):
        self.driver = Functions.abrir_navegador(self)
        self.driver.get(Inicializar.URL)

    def test_1048(self):
#        Functions.get_elements(self, "Email").send_keys("unmail")
#        self.driver.find_element(By.ID, thonetLogin.txt_email_id).send_keys("unmail@gmail.com")
#        self.assertIn("Registrarte - Spotify", self.driver.title)
        Functions.get_json_file(self, "Thonet_login")
        time.sleep(5)
        iniciar_sesion = Functions.get_elements(self, "IniciarSesion")
        time.sleep(5)
        iniciar_sesion.click()
        time.sleep(10)

#        Functions.get_entity(self, "IniciarSesion")
#        iniciar_sesion = Functions.get_elements(self, "IniciarSesion")
#        iniciar_sesion.click()
#        time.sleep(5)
        #Cierro cookies
        #button_exit_cookies = self.driver.find_element(By.ID, 'onetrust-close-btn-container')
        #button_exit_cookies.click()
        #Email
        #email = "siousaf_flqxs33@cikue.com"
        #input_email = self.driver.find_element(By.ID, "email")
        #input_email.send_keys(email)
        #time.sleep(1)
        #Password
        #input_password.send_keys("Contrasenia12!@")
        #input_password = self.driver.find_element(By.ID, "password")
        #time.sleep(1)
        #Apodo
        #input_displayname.send_keys("Ro")
        #input_displayname = self.driver.find_element(By.ID, "displayname")
        #time.sleep(1)
        #Día
        #input_day = self.driver.find_element(By.ID, "day")
        #input_day.send_keys("25")
        #time.sleep(1)
        #Mes
        #dropdown_month = Select(self.driver.find_element(By.ID, "month"))
        #dropdown_month.select_by_value("04")
        #time.sleep(1)
        #Año
        #input_year = self.driver.find_element(By.ID, "year")
        #input_year.send_keys("1995")
        #time.sleep(1)
        #Gender
        #radio_button_female = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/form/fieldset/div/div[2]/label')
        #radio_button_female.click()
        #time.sleep(1)
        #Checkbox mensajes marketing
        #checkbox_marketing = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/form/div[5]/div/label')
        #checkbox_marketing.click()
        #time.sleep(1)
        #Checkbox compartir datos
        #checkbox_share = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/form/div[6]/div/label/span[1]')
        #checkbox_share.click()
        #time.sleep(1)
        #Registrar
        #button_register = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/form/div[7]/div/button/span[1]')
        #logging.info(button_register)
        #button_register.click()
        #time.sleep(10)
        #Screen
        #self.driver.save_screenshot('../Data/Evidencia/captura.png')
        #time.sleep(3)
        
        pass


    def tearDown(self):
        pass
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()