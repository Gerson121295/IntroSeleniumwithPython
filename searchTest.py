        # Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
#from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class SearchTest(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    
  #  @classmethod # Decorador para que las distintas paginas corran en una sola pestaña

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver  #driver = self.driver para no estar escribiendo el codigo en los siguiente solo escribir driver
	    
        driver.implicitly_wait(10) # esperamos 20 seg antes de realizar la siguiente accion
        driver.maximize_window() #decirle al navegoar que maximice la ventana porque puede que halla elementos responsivos
        driver.get("http://demo-store.seleniumacademy.com/")   #ir al sitio para las pruebas
  

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice

    def test_search_tee(self):  #buscando un camisa
         driver = self.driver
         search_field = driver.find_element_by_name('q')
         search_field.clear()  #limpia el campo de busqueda en caso de halla un texto

         search_field.send_keys('tee')  #escribe en la barra de busqueda, tee(camisa)
         search_field.submit() #envie la busqueda

    def test_search_salt_shaker(self): #otra busqueda(un salero)
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()  #limpia el campo de busqueda en caso de halla un texto

        search_field.send_keys('salt shaker')  #escribe en la barra de busqueda, tee(camisa)
        search_field.submit() #envie la busqueda


        #lISTAR los productos en una variable llamada products
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')  #ir al sitio en la busqueda buscar "salt shaker" y clic derecho copy y copiar Xpath(forma rapida de optener la lista de elementos es por su Xpath)
        self.assertEqual(1, len(products))  #indica si la cantidad de productos es 1 o no

	# Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2)   #, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  