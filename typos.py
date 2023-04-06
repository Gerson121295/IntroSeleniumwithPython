
#Test: Texto del sitio web sea idéntico a uno que esperamos y cuenta cuantos intentos se hace para encontrarlo(se recarga la pagina)

from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
     self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
     driver = self.driver

     driver.implicitly_wait(50)
     driver.maximize_window()
     driver.get('https://the-internet.herokuapp.com/') #ir al sitio
     driver.find_element_by_link_text("Typos").click() #ir a la parte de Typos

    def test_find_typo(self):
        driver = self.driver

        paragraf_to_ckeck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)') #CSS Selector debido a que es un parrafo
        text_to_check = paragraf_to_ckeck.text #luego se extrae el texto que tiene debido a que no queremos hacer referencia a la etiqueta
        print(text_to_check) #mostramos el texto para validar que es correcto o validarlo con un assert

        tries = 1 #contara las veces en que intentamos para encontrar el texto correcto
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won,t."

        while text_to_check != correct_text: #mientras que el texto a verificar sea diferente al texto correcto, El navegador se refresca
            driver.refresh() #refresca el navegador
            paragraf_to_ckeck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')  #selector del parrafo 
            text_to_check = paragraf_to_ckeck.text   #luego se extrae el texto que tiene debido a que no queremos hacer referencia a la etiqueta
            tries += 1 #se suma los intentos
        else:
            found = True   #encontrado

        self.assertEqual(found, True)  #Evalua si found es true la prueba continua
        print(f"It took {tries} tries to find the typo")  #muestra en consola lo encontrado

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2) #, testRunner = HTMLTestRunner(output = 'report9', report_name = 'test_find_typo'))


