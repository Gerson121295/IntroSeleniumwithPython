
# Reescribir una serie de metodos para un objeto el cual sera el que funcione para ejecutar las pruebas  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC # llamda a las expected conditions as(como) EC para que sea facil escribirla al llamarla


class GooglePage(object):
    def __init__(self, driver): # se incialiaza con donder init donder
        self._driver = driver #driver sera la forma mas facil para llamarlo por eso se iguala 
        self._url = 'https://google.com' #url a ingresar
        self.search_locator = 'q' # la barra de busqueda su identificador por nombre es q 

    @property #Propiedad que se utilizara en las pruebas, para busqueda
    def is_loaded(self): #Metodo verifica que el sitio web a cargado correctamente 
        #espera 10 seg. hasta que se cumpla la condicion esperada que es la presencia del elemento ubicado por su nombre q. (barra de busqueda)
        WebDriverWait(self._driver , 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True #esto retorna verdadero para indicar que la carga del sitio fue verdadera

    @property #propiedad para el termino de busqueda
    def keyword(self):
        input_field = self._driver.find_element_by_name('q') #en el campo donde se agrega estos terminos. identidicado por su nombre con "q" es la barra de busqueda de Google
        return input_field.get_attribute('value') #retorna obtener el atributo de input_field especificamente el valor

    #metodos con los que va a trabajar el Page Object
    #ingresar a la url
    def open(self): 
        self._driver.get(self._url)

    #para buscar los terminos, tiene como parametro sef y keyword    
    def type_search(self, keyword): 
        input_field = self._driver.find_element_by_name('q') # lo identificamos por su selector por nombre es "q" la barra de busqueda de google
        input_field.send_keys(keyword) #se envia la simulacion de las teclas (keyword)

    #hace el envio del termino de busqueda
    def click_submit(self): 
        button_submit = self._driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[1]/div/span/svg') #obtenemos el selector del boton de envio
        button_submit.click() #envia la busqueda

    #metodo Keyword para realizar la busqueda
    def search(self, keyword):  #parametros que recibe
        self.type_search(keyword) #llamda del metodo type_search(escrito anterior) y se le pasa el keyword
        self.click_submit  #LLama al metodo que ejecuta el envio


        #se añadieron la capa de abstraccion para las pruebas
