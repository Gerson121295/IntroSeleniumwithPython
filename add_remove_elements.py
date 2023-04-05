
import unittest
from time import sleep
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddRemoveElementsTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/") 

        #driver.find_element_by_link_text('Add/Remove Elements').click()
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input("How many elements will you add?: ")) #Numero entero y Pregunta al usuario cuantos elementos van a agregar
        elements_removed = int(input("How many elements will you remove?: ")) #Numero entero y Pregunta al usuario cuantos elementos va a eliminar
        total_elements = elements_added - elements_removed  #total de elements

        #identifica donde esta el boton para agregar los elementos
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3) #espera de 3 seg

        #agregar los botones por medio de un for
        for i in range(elements_added): #elements_added: cantida de elementos que el usuario indico que se va a agregar
            add_button.click()  #al boton de agregar se le da clic todas estas veces

        #eliminar los botones por medio de un for
        for i in range(elements_removed):
            try: #para capturar los errores por si se quiere eliminar mas botones de lo que existen
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]') #boton de eliminar los elementos
                delete_button.click()  #clic al boton de eliminar
            except Exception as e: #en caso de un error muestra al usuario
                print("You're trying to delete more elements than existent")
                break  #salir del ciclo

        #Mostrar en consola lo que sucedio
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen") #hay {numero} de elementos en pantalla
        else:
            print("There are 0 elements on screen")

        sleep(3) #espera de 3 seg




        # Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report6', report_name = 'test_add_remove'))
#sin reporte comentar "#" antes de la , del 2 
        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python add_remove_elements.py 

