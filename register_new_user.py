# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    
  #  @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver  #driver = self.driver para no estar escribiendo el codigo en los siguiente solo escribir driver
	    
        driver.implicitly_wait(10) # esperamos 20 seg antes de realizar la siguiente accion
        driver.maximize_window() #decirle al navegoar que maximice la ventana porque puede que halla elementos responsivos
        driver.get("http://demo-store.seleniumacademy.com/")   #ir al sitio para las pruebas
  
  
	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    #def test_search_text_field(self):
    #    search_field = self.driver.find_element_by_id("search") #busca por id del elemento(barra buscar)
    
    def test_new_user(self):
         driver = self.driver #inspeccionar ACCOUNT como no tiene mucha info se copia su Xpath
         
         driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click() # busca ACCOUNT y da clic para que se despliegue ACCOUNT
         driver.find_element_by_link_text('Log In').click()  #Encuentre elemento por el texto que esta en su enlace: clic en Login
         
         create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')  #dentro buscamos Create an Account y copiamos su xpath debido a que no cuenta con mucha info solo tiene un span
        
        #validamos que el boton create an account este habilitado con assertions
         self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())  #valida si el boton este disponible y habilitado
         create_account_button.click() #luego de validar clic en el boton para crear un usuario

        #Verificacion para saber que si se esta en el sitio de creacion de cuenta. -Se hace por el titulo de la pestaña
         self.assertEqual('Create New Customer Account', driver.title)  #si el sitio (titulo de la pestaña) es igual a Create New Customer

        #variables para agregar datos para crear un usuario: Identifiacion de los elementos del formulario para interactuar
         first_name = driver.find_element_by_id('firstname')
         middle_name = driver.find_element_by_id('middlename')
         last_name = driver.find_element_by_id('lastname')
         email_address = driver.find_element_by_id('email_address')
         news_letter_subscription = driver.find_element_by_id('is_subscribed') # este boton es un check
         password = driver.find_element_by_id('password')
         confirm_password = driver.find_element_by_id('confirmation')
         submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button') #el boton de envio no tiene datos explicitos por lo que se toma por su Xpath

        #Verificar que los elementos del formulario esten habilitados
         self.assertTrue(first_name.is_enabled()  #firstname habilitado
         and middle_name.is_enabled()
         and last_name.is_enabled()
         and email_address.is_enabled()
         and news_letter_subscription.is_enabled()
         and password.is_enabled()
         and confirm_password.is_enabled()
         and submit_button.is_enabled()               
        )
    
        #Luego de verificar que los elementos esten habilitados se envian datos a los elementos del formulario
         first_name.send_keys('Test')
         driver.implicitly_wait(1)  #pausa 1 seg para ver como se envia los datos
         middle_name.send_keys('Test')
         driver.implicitly_wait(1)  #pausa 1 seg  para ver como se envia los datos
         last_name.send_keys('Test')
         driver.implicitly_wait(1)  #pausa 1 seg para ver como se envia los datos
         email_address.send_keys('Test@testingmail.com')
         driver.implicitly_wait(1)  #pausa 1 seg para ver como se envia los datos
         password.send_keys('Test')
         confirm_password.send_keys('Test')
         driver.implicitly_wait(1)  #pausa 1 seg para ver como se envia los datos
         news_letter_subscription.click()
         driver.implicitly_wait(1)  #pausa 1 seg para ver como se envia los datos
         submit_button.click()


	# Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'register_new_user'))

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  