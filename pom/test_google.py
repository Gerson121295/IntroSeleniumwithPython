import unittest
from selenium import webdriver
from google_page import GooglePage #importamos el archivo google_page
from pyunitreport import HTMLTestRunner

class GoogleTest(unittest.TestCase):

    @classmethod #decorador para en caso de que se quiera añadir nuevos casos de pruebas esos corran en una sola instancia del navegador(no se cierre el navegador, ejecute toda de una) 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    

    def test_search(self):
        google = GooglePage(self.driver) #igualamos para que solo usar google en las llamadas de GooglePage(self.driver) es mas facil solo escribir google
        google.open() #llamada y realize el metodo open()
        google.search('Python') #llamada y realize el metodo search() y se le agrega el keyword palabra a buscar que es Python

        self.assertEqual('Python', google.keyword) #verifica el Keyword que se esta utilizando con assert y lo comparamos con google.keyword 


        #def test_search(self):       
    @classmethod
    def tearDownClass(cls):
         cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'GoogleTest'))


    #ejecutamos el script: python test_google.py  # Realiza el test de entrar a google y busca el termino Python





