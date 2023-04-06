

#Prueba Consultar datos sin agregar archivo csv: 

import csv, unittest
#from ddt import ddt, data, unpack #installar en consola CMD o en visual studio code: pip install ddt
from ddt import ddt, data, unpack  #para usar datos que vamos a designar y desempaquetarlo de las duplas en las que estaran
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver= self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(('dress', 6), ('music', 5))
    @unpack #desempaquetar las duplas y puedan ser consultadas de forma individual
    def test_search_ddt(self, search_value, expected_count): #Parametros de la busqueda: self(por defecto), search_value(valor de la busqueda), expected_count(cantidad esperada a encontrar)
        driver= self.driver

        search_field= driver.find_element(By.NAME,'q') #identificamos la barra de busqueda por su name
        search_field.clear() #eliminar la barra de busqueda por si tienen un texto escrito
        search_field.send_keys(search_value) #Se escribe en la barra de busqueda(valor lo tiene el parametro de la busqueda) ya no se escribe el text
        search_field.submit() #se envia la busqueda

        #luego de realizar la busqueda (MUSIC"ejemplo") copiamos su Xpath del titulo del 1er resultado.
        #otra forma la definimos asi: //h2[@class= "product-name"]/a   #esta dentro de H2 dentro de Class y dentro de etiqueta "a" ahi esta el titulo
        products = driver.find_elements(By.XPATH,'//h2[@class= "product-name"]/a')

        #se imprime el texto de los productos
        for product in products:
            print(product.text)
        self.assertEqual(expected_count, len(products))
     
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2) 