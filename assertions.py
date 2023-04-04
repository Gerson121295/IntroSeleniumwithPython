
        # Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
#from pyunitreport import HTMLTestRunner  #instalar pip install html-testRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException   #sirve como una excepcion para los exception al validar la presencia de un elemento
from selenium.webdriver.common.by import By #para llamar a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    
  #  @classmethod # Decorador para que las distintas paginas corran en una sola pestaña

     def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver  #driver = self.driver para no estar escribiendo el codigo en los siguiente solo escribir driver
	    
        driver.implicitly_wait(10) # esperamos 20 seg antes de realizar la siguiente accion
        driver.maximize_window() #decirle al navegoar que maximice la ventana porque puede que halla elementos responsivos
        driver.get("http://demo-store.seleniumacademy.com/")   #ir al sitio para las pruebas
  

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
 
    #Metodo para los Assertions
    #Valida si la barra de busqueda esta presente
     def test_search_field(self):
         #print('Searching the search bar')
         self.assertTrue(self.is_element_present(By.NAME, 'q'))

    #validar la presencia de los lenguajes del sitio
     def test_language_option(self):
         self.assertTrue(self.is_element_present(By.ID, 'select-language')) #era: select-language



	# Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
     def tearDown(self):
        self.driver.quit()

     def is_element_present(self, how, what):  # is_element_present: permite encontrar los elementos de acuerdo a estos parametros, how(indica el tipo de selector) y what(el valor que tiene)
          try:
             self.driver.find_element(by = how, value = what)
          except NoSuchElementException as variable:
               return False        
          return True


if __name__ == "__main__":
	unittest.main(verbosity = 2)   #, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  

