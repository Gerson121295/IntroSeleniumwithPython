# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HomePageTest(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    
  #  @classmethod # Decorador para que las distintas paginas corran en una sola pestaña

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver  #driver = self.driver para no estar escribiendo el codigo en los siguiente solo escribir driver
	    
        driver.get("http://demo.onestepcheckout.com/")   #ir al sitio para las pruebas
        driver.maximize_window() #decirle al navegoar que maximice la ventana porque puede que halla elementos responsivos
        driver.implicitly_wait(10) # esperamos 10 seg antes de realizar la siguiente accion

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_search_text_field(self):
         search_field = self.driver.find_element_by_id("search") #busca por id del elemento(barra buscar)
    
    def test_search_text_field_by_name(self): #va a buscar al elemento por su name
         search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self): #busca por el nombre de la clase
         search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self): #verificar que el boton de la barra de vusqueda este disponible
         button = self.driver.find_element_by_class_name("button")
         
    #cuenta cuantas imagenes hay de promocion en el banner
    def test_count_of_promo_banner_images(self):
         banner_list = self.driver.find_element_by_class_name("promos")
         banners = banner_list.find_element_by_tag_name("img")   #almacena la busqueda de los banners y los busca por sus etiquetas HTML(img)
         self.assertEqual(3, len(banners))  #-cuenta cuantas imagens hay

    #selector Xpath(no es recomendable usar) muy util cuando no se tiene un id, clase, name, etc. del elemento( clic derecho del elemento--> copy --> Copy Xpath)
    def test_vip_promo(self):
         vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img') #Xpath por medio de xml encuentra la imagen 

    #selector del carrito de compras por su CSS
    def test_shopping_cart(self):
         shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")



	# Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  
        # self - hace que al ejecutar una prueba se habra el navegador y se cierre por cada prueba. 
        #para que las pruebas se ejecuten de una vez sin cerrar el navegador se agrega debajo de class --> @classmethod y donde dice "self" se agrega "cls"

        