#Script para que recargue todas las veces hasta que aparezca galery(porque no aparce) y contamos cuantos le tomo a selenium

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pyunitreport import HTMLTestRunner

class DisappearElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_disappear_element(self):
        driver = self.driver
        
        #ingresar a cada uno de los elementos
        options = [] # lista vacia, para las que aparacen en el menu
        menu = 5 # cuantas opciones tiene el menu del sitio(tiene 5)
        tries = 1 # Cuantos intentos le lleva a selenium, siempre comienza en 1 ya que al ingresar se toma como un intento
        
        # Ciclo While para medir cual es la longitud de opciones
        while len(options) < 5: # mientras options sea menor de 5  se ejecutara el siguiente codigo
            options.clear() # Limpiar lista Options limpiar los valores de la lista

            for i in range(menu): # para iterar dentro de las opciones
                try:
                    
                    #tenemos que iterar por cada uno de los elementos pero natural tiene el numero del div dode se encuentra
                    # y el elemento de la lista no podemos hacer referencia siempre al numero uno [1]
                    # por lo que debemos cambiarlo por la viariable iterable [{i +1}] es + 1 por que i comoneza en cero
                    # se pone f para que reconozca i    ////*[@id="content"]/div/ul/li[1]/a   // i+1 porque i comienza desde el 0 los botones comienzan desde el 1 no del 0
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i +1}]/a')  #xpath de Home
                    options.append(option_name.text) # agregar en la lista de opciones el valor que se valla mostrando
                    print (options)
                except:  #la exepcion que pueda ocurrir cuando se este iterando cada uno de los elemento
                    print (f"option number {i + 1} is not found")
                    tries += 1 # sumamos 1 a los intentos
                    driver.refresh()
            print((f"Finished in  {tries}")) # imprimimos cuantos intentos llevo 

        # Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report7', report_name = 'test_disappear_element'))
