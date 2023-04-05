
#En Dinamic Controls del sitio: tenemos para escribir datos y se puede deshabilitar o habilitar por un boton, Al habiliat tenemos que esperar para escribir en el. Por lo que las esperas son fundamentales.

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #para las esperas
from selenium.webdriver.support import expected_conditions as EC


class Dynamic_controls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/') #ir al sitio
        driver.find_element_by_link_text("Dynamic Controls").click() #ir a la parte de Dynamic Controls

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]") #copiar el selector del checkbox y asignarlo a la variable checkbox
        checkbox.click()  #clic en checkbox

        #boton de remover: no hay mucha info disponible para su selector se hace por Copy Selector(selector de Css)
        remove_add_buttom = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_buttom.click() #clic en remove_add_buttom esto hara que desparezca el checkbox, entonces debemos esperar a darle clic en el boton

        #Luego de dar clic en remove_add_button debemos espera para volver a dar clic por lo que lo hacemos con una condicion Esperada
        #Esperar 15 seg hasta que se ejecute la condicion Esperada, el elemento pueda ser clicleable se dice cuale es el elemento por su selectorCSS al checkbox(tipo de selector y selector) 
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_buttom.click()#Luego de esperar clic en remove_add_button y debe aparecer el checkbox nuevamente

        #Boton de habilitar y desabilitar el text area
        enable_desable_buttom = driver.find_element_by_css_selector("#input-example > button") #identificado por su selectorCSS
        enable_desable_buttom.click() #CLic en el boton

        #Luego de darle clic en el boton de enable_desable_buttom debemos esperar a que carque y halla habilitado el text area
        #espera explicita de 15 seg, hasta que se cumpla la condicion Esperada llamada EC hasta que el elemento este habilitado o sea cliclable, se indica al elemento por su selector CSS
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#input-example > button")))
        
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]") #ya esta habilitado se puede enviar texto al mismo
        text_area.send_keys('Platzi') #se envia el texto

        enable_desable_buttom.click()  #clic para deshabilitar el text_area


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report8', report_name = 'test_dynamic_controls'))

