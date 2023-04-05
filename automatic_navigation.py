import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep


class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://google.com/') #ir a google para realizar una busqueda y automatizar el navegador

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q') #barra de busqueda de google
        search_field.clear() #limpiar si la barra de busqueda por si hubiera texto
        search_field.send_keys('platzi') #escribimos platzi
        search_field.submit() #enviamos

        driver.back() #Regresar a la pagina anterior
        sleep(3) #proviene de libreria time: no es recomendable agregar temporizador a las pruebas
        driver.forward() #Avanzar a la pagina posterior
        sleep(3)
        driver.refresh() #Actualizar la pagina
        sleep(3)


        # Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report4', report_name = 'test_browser_navigation'))
    
    #ejecuta: python automatic_navigation.py

