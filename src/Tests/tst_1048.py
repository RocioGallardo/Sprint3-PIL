"""Test 1048"""
import unittest
import time
import re
from selenium.webdriver.common.by import By
from src.Functions.Function import Functions
from src.Functions.Inicializar import Inicializar
#from Pages.Thonet import Thonet as DataThonet
class Test_1048(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = Functions.abrir_navegador(self)
        self.driver.get(Inicializar.URL)

    def test_1048(self):
        Functions.get_json_file(self, "Thonet")
        
        """Inicio sesión"""
        iniciarSesion = Functions.get_elements(self, "IniciarSesion")
        self.assertTrue(iniciarSesion, "El elemento 'Iniciar sesión' no se encontró")
        iniciarSesion.click()
        print("Se redirige al formulario de inicio de sesión correctamente")
        
        inputEmail = Functions.get_elements(self, "InputEmail")
        self.assertTrue(inputEmail, "El elemento 'Input Email' no se encontró")
        self.assertTrue(inputEmail.is_enabled(), "El elemento inputEmail no está habilitado")
        inputEmail.send_keys(Inicializar.User)
        
        inputPassword = Functions.get_elements(self, "InputPassword")
        self.assertTrue(inputEmail, "El elemento 'Input Password' no se encontró")
        self.assertTrue(inputPassword.is_enabled(), "El elemento inputPassword no está habilitado")
        inputPassword.send_keys(Inicializar.Password)
        
        btnIngresar = Functions.get_elements(self, "BtnIngresar")
        self.assertTrue(inputEmail, "El elemento 'Botón ingresar' no se encontró")
        btnIngresar.click()
        print("Se inicia sesión correctamente")
        
        """Hago la búsqueda"""
        inputBuscador = Functions.get_elements(self, "InputBuscador")
        self.assertTrue(inputEmail, "El elemento 'Input Buscador' no se encontró")
        placeholder_value = inputBuscador.get_attribute("placeholder")
        self.assertEqual(placeholder_value, "Buscar productos, categorías y más...", "El atributo placeholder no coincide")
        self.assertTrue(inputBuscador.is_enabled(), "El elemento inputBuscador no está habilitado")
        inputBuscador.send_keys(Inicializar.ProductNameCorrect)
        btnBuscar = Functions.get_elements(self, "BtnBuscador")
        btnBuscar.click()
        print("Se realiza la búsqueda correctamente")
        
        """Valido búsqueda exitosa"""
        txtResultado = Functions.get_elements(self, "TxtResultado")
        txt = txtResultado.text
        match = re.search(r'\d+', txt)
        number = int(match.group())
        self.assertTrue(number > 0, "El resultado no es mayor que 0")
        # Encuentra todos los elementos con la clase "title"
        time.sleep(10)
        title_elements = self.driver.find_elements(By.XPATH, "//*[@id='contenido']/div[1]/div[2]/div[2]/div/ul/li/div/div/a/h2")
        for element in title_elements:
            text = element.text
            self.assertTrue(Inicializar.ProductNameCorrect in text, f"El elemento con texto '{text}' no contiene '{Inicializar.ProductNameCorrect}'.")
        print("Los resultados de la búsqueda son correctos")
        self.driver.save_screenshot('../Data/Evidencia/captura-tst_1048.png')
        pass


    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()