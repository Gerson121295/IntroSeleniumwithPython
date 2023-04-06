
import unittest 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from prettytable import PrettyTable #instalar en el proyecto: pip install prettytable - #para trabajar con tablas: permite mostrar la tabla


class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Sortable Data Tables").click()

   # def test_sort_tables(self):
    def test_table(self):
        driver = self.driver
        rows = []  #fila para almacenar los datos
        ptable = PrettyTable()
        for i in range(5):  #5 es la cantidad de elements que tiene la tabla
            header = driver.find_element( #iterar por cada uno de los headers
                By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]/span') #header se ubica en el LastName y copia el xpath #se sustituye el numero con el que se indica el nodo y se agrega la variable iteradora
            for j in range(4): #4 filas se van a estar recorriendo de los datos del header
                row = driver.find_element(
                    By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]') #filas de los campo: se coloca en el primer campo (apellido) y se copia su xpath y se modifica: tr[1]/td[1] con el que se indica el nodo y se agrega la variable iteradora
                    #driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]') #version anterior
                rows.append(row.text) #agrega el dato a la fila de la tabla extrallendo el texto de row.text   # append se utiliza para agregar un nuevo elemento al final de un campo de texto existente. 
            ptable.add_column(header.text, rows) #añade las columnas a la tabla
            rows.clear()

        print(ptable) #muestra la tabla en consola


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)


#Test para trabajar con tablas.
