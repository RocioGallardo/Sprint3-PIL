from Functions.Inicializar import Inicializar

#import os
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import WebDriverWait
#import string
import pytest
#import unittest
import json
#from test.test_tomllib.test_data import json_path



class Functions(Inicializar):
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        if navegador == "CHROME":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            return self.driver
    def _init_(self):
        self.json_GetFieldBy = None
        self.json_ValueToFind = None
        
    def get_json_file(self, file):
        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                return self.json_strings
        except FileNotFoundError:
                print("get_json_file: " + json_path)
                self.json_strings = False
                Functions.tearDown(self)
                pytest.skip("get_json_file: No se encontro el Archivo " + file)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para este TC")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError:
                self.msj = "get_entity: No se encontro la key a la cual se hace referencia: " + entity
                Functions.tearDown(self, "fail")
                pytest.skip(self.msj)
                #self.driver.close()
    def get_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "xpath":
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                        #elements = self.driver.find_element_by_xpath(self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "class":
                    elements = self.driver.find_element_by_class_name(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements
            except AttributeError:
                self.msj = ("get_elements AttributeError: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except NoSuchElementException:
                self.msj = ("get_elements NoSuchElementException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                self.msj = ("get_elements TimeoutException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except UnexpectedAlertPresentException as e:
                self.msj = "get_elements: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self)
                #self.driver.close()

    def tearDown(self):
                self.driver.quit()