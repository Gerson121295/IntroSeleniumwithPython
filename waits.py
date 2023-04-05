
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

#Herramienta para seleccionar hacer referencia a elementos de la web a traves sus selectores: no para identificarlos sino para interacturar
from selenium.webdriver.common.by import By

#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

#Importar esperas explicitas y las definimos como "as" EC para no escribir su nombre completo en el codigo cada vez que las llamemos
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://demo-store.seleniumacademy.com/')

    def test_account_link(self): #Cuentas del enlace del sitio

        #(self.driver, 3)Esperar 3 segundos hasta que se cumpla la condicion dada: lambda, llamada s: encuentra un elemento por su id(referencia menu de seleccion de idiomas), 
        # obtiene su atributo y longitud de los elementos que hay en este"cuantos elementos hay"(get_attribute('length')) luego igualarlo a 3 porque hay 3 idiomas 
        WebDriverWait(self.driver, 3).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Hacer referencia al enlace donde estan las cuentas guadado en account, Espera 3 seg. hasta que se cumpla la condicion esperada llamada EC(expert condicion)  haciendo referencia
        #a la visibilidad del elemento que se esta ubicando por medio del text que tiene
        account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()  #clic en account


    def test_create_new_customer(self): #Creacion de nuevo usuario

        #Encontrar el elemento por el texto del enlace luego hacer clic
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Hacer referencia a la cuenta: espera 3 seg. hasta que se cumpla la siguiente condicion, EC identificar elemento visible por el texto que tiene Se envian los argumentos (tipo de selecto y texto que tiene el sitio web)
        my_account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click() #luego de evaluar dar clic

        #Referencia a crear una cuenta: espera 2 seg hasta que se cumpla la condicion esperada EC un elemento pueda ser clickeable, vamos a poder hacer clic y se identifica por el texto y se envia los argumentos(tipo de selecto y texto que tiene el boton)
        create_account_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click() #luego de evaluar dar clic

        #Verificacion de estado de pagina web: espera 5 seg, hasta que se cumpla la condicion esperada: EC verifica que el sitio web en su titulo tenga el texto
        WebDriverWait(self.driver, 5).until(EC.title_contains('Create New Customer Account'))

        # Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report5', report_name = 'test_account_link'))
    
    #ejecuta: python waits.py
    
    #valida las opciones de los idiomas.
    #Poder entrar a la seccion de cuentas
    #Y poder ingresar al menu de creacion de una cuenta

