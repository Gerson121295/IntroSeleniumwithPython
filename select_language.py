# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select #Modulo para manejar elementos dropdown (elegir las opciones que aparecen)
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class LanguageOptions(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    
  #  @classmethod # Decorador para que las distintas paginas corran en una sola pestaña

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver  #driver = self.driver para no estar escribiendo el codigo en los siguiente solo escribir driver
	    
        driver.implicitly_wait(7) # esperamos 20 seg antes de realizar la siguiente accion
        driver.maximize_window() #decirle al navegoar que maximice la ventana porque puede que halla elementos responsivos
        driver.get("http://demo-store.seleniumacademy.com/")   #ir al sitio para las pruebas
  
	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
   # def test_search_text_field(self):
    #     search_field = self.driver.find_element_by_id("search") #busca por id del elemento(barra buscar)
 
    def test_select_language(self): #para elegit los idiomas que estan en el sitio web en el dropdown de idiomas(English, French, German)
        options = ['English', 'French', 'German'] #Listas con el nombre de las etiquetas, igual de orden como el del sitio
        act_options = []#Lista vacia, para almacenar las opciones al momento de revisar

        #Acceder a los elementos de la lista

        select_language = Select(self.driver.find_element_by_id('select-language'))

        #Validar si estan disponibles las opciones del dropdown

        self.assertEqual(3, len(select_language.options))#Esto nos permite ingresar a las opciones del dropdown, hay 3 opciones y se compara con la longitud de la lista de opciones

        for option in select_language.options:#Bucle para recorrer los elementos del dropdown
            act_options.append(option.text) # Agregar(con append) las opciones a la lista vacia. Se añade el texto de la opcion

        #Comparacion de listas expuestas y activas sean identicas
        self.assertListEqual(options, act_options)

        #Validar idioma por default
        self.assertEqual('English', select_language.first_selected_option.text) #Verificar que la palabra ingles esta por default

        #Seleccionar idioma del dropdown
        select_language.select_by_visible_text('German') #Seleccionar por el texto visible

        #Verificar que se cambio el idioma en el sitio por medio de la url
        self.assertTrue('store=german' in self.driver.current_url)

        #Elegir un idioma mediante al indice
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0) #elija al idioma por su indice, valor 0 ingles


# Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report2', report_name = 'test_select_language'))  #por defecto hay una carpeta reports en esta se crea la carpeta report2 que tiene el repote de la prueba

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  

#al ejecutarlo El navegador debe ingresar al sitio web, verificar los assert asignados, Elegir el idioma ingles, despues el aleman y luego volver al idioma ingles

