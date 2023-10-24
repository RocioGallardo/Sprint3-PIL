"""Test 1049"""
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
        inputBuscador.send_keys(Inicializar.ProductNameIncorrect)
        btnBuscar = Functions.get_elements(self, "BtnBuscador")
        btnBuscar.click()
        print("Se realiza la búsqueda correctamente")
        
        
        """Valido búsqueda con datos incorrectos - sin resultados"""
        txtResultado = Functions.get_elements(self, "TxtResultado")
        txtR = txtResultado.text
        match = re.search(r'\d+', txtR)
        number = int(match.group())
        self.assertEqual(number, 0, "El resultado debería ser 0")
        txtSinResultado = Functions.get_elements(self, "TxtSinResultados")
        txtSR = txtSinResultado.text
        self.assertEqual(txtSR, "¡Lo sentimos! No se encontraron productos disponibles por el momento.", "El texto no coincide con : ¡Lo sentimos! No se encontraron productos disponibles por el momento.")
        print("El resultado de la búsqueda es correcto")
        self.driver.save_screenshot('../Data/Evidencia/captura-tst_1049.png')
        pass


    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()