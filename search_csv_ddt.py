#consulta de los datos por archivo CSV

import csv, unittest #para los archivos CSV
#from ddt import ddt, data, unpack #installar en consola CMD o en visual studio code: pip install ddt
from ddt import ddt, data, unpack  #para usar datos que vamos a designar y desempaquetarlo de las duplas en las que estaran
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

#Funcion para consulta o leer nuestro archivo CSV
""" def get_data(file_name): #se pasa el nombre de archivos
    rows = [] #se crea una lista para indicar el numero de filas que hay
    with open(file_name, 'r') as data_file:  #abrir el archivo en modo lectura y se cierre al final 
        reader = csv.reader(data_file) #csv.reader se va a encargar de leer los datos del archivo
        next(reader, None) #Que pase a la siguiente fila de datos debido a que se omitira la cabecera

    for row in reader: #Esa fila en reader se va agrega a la lista de filas
        rows.append(row) # se va agrega a la lista de filas
    #return rows #retorna el valor de las filas
    return  list(reader) #para así reducir la complejidad algorítmica (en caso de que el csv sea bastante extenso)
 """
#para buena practica: Manejar el acceso a los archivos con el keyword "with" en la funcion get_dat() para que despues del leer el archivo se cierre
def get_data(file_name):
    rows = []
    data_file= open(file_name, 'r')
    reader= csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows


"""
Data del archivo CSV para las consultas
#Contiene los headers
 CategoryOrProduct,NumberOfProducts
#Contiene la data
music,5
denim,2
skirt,1
book,3 """

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver= self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('testdata.csv'))  #archivo: testdata.csv  #funcion para obtener los datos(get_data)
    #@data(('dress', 6), ('music', 5))
    @unpack #desempaquetar las duplas y puedan ser consultadas de forma individual
    def test_search_ddt(self, search_value, expected_count): #Parametros de la busqueda: self(por defecto), search_value(valor de la busqueda), expected_count(cantidad esperada a encontrar)
        driver= self.driver

        search_field= driver.find_element(By.NAME,'q') #identificamos la barra de busqueda por su name
        search_field.clear() #eliminar la barra de busqueda por si tienen un texto escrito
        search_field.send_keys(search_value) #Se escribe en la barra de busqueda(valor lo tiene el parametro de la busqueda) ya no se escribe el text
        search_field.submit() #se envia la busqueda

        #luego de realizar la busqueda (MUSIC"ejemplo") copiamos su Xpath del titulo del 1er resultado.
        #otra forma la definimos asi: //h2[@class= "product-name"]/a   #esta dentro de H2 dentro de Class y dentro de etiqueta "a" ahi esta el titulo
        products = driver.find_elements(By.XPATH,'//h2[@class= "product-name"]/a')
        #print(f'Found {len(products)} products') #Validamos lo que se encontro
        
        expected_count= int(expected_count) #cambiar su valor a entero para evitar error
        if expected_count>0: #evaluar al momento de mostrar los resultados  que expected_count sea >0
            self.assertEqual(expected_count, len(products)) #valida que expected_count se igual a la lista de productos
        else: #si no : da un mensaje de salida
            message= driver.find_elements(By.CLASS_NAME,'note-msg')
            self.assertEqual('Your search returns no results.', message) #valida que no halla el producto por medio del texto que sale del sitio al no haber producto despues de consultar
        print(f'Found {len(products)} products') #Publica los productos encontrados
        
     
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'test_search_ddt'))

        #Para correr nuestra prueba: nos ubicamos en la carpeta del archivo
        #y Ejecutamos python hello_word.py  

        #util para verificar en un login que el usuario y contraseña son correctos
