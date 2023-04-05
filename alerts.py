import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class CompraProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_remove_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q') ##barra de busqueda del producto tee(camisa)
        search_field.clear() #como buena práctica se recomienda limpiar los campos en la barra de busqueda

        search_field.send_keys('tee') #agrega el texto nombre del producto en la barra de busqueda
        search_field.submit() #se envia la peticion el formulario

        #Aparecen los resultados de busqueda
        driver.find_element_by_class_name('link-compare').click() #elemento de: Add to Compare le damos clic
        driver.find_element_by_link_text('Clear All').click() #luego de agregar el elemento para agregar: debemos darle clic en el enlace Clear List para eliminar la lista y aparesca la alerta(si va a eliminar la lista) #Encuentra al elemento por el texto del enlace, y de clic

        #creamos una variable para interactuar con el pop-up
        alert = driver.switch_to.alert  #alert = driver.switch_to_alert()  #la atencion del navegador se encuentre en el alert
        #vamos a extraer el texto que muestra
        alert_text = alert.text

        #vamos a verificar el texto de la alerta: copiar el texto de la alerta y lo valida
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept() #Clic en el boton Aceptar del alert

        # Indica al navegador que cierre las ventanas e inicios de sesion una vez terminadas las pruebas
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'report3', report_name = 'remove_alert'))




