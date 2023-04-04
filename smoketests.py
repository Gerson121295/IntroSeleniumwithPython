

#Test Suit de archivos: assertions.py y searchTest.py

from unittest import TestLoader, TestSuite
#from pyunitreport import HTMLTestRunner #para generar el reporte
from HtmlTestRunner import HTMLTestRunner  #pip install html-testRunner
#importa los archivos que contiene las pruebas
from assertions import AssertionsTest
from searchTest import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTest)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])



#Generar el reporte
kwargs = {
    "output":'smoke-test-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)


##ejecuta todos los casos de prueba del primer archivo luego ejecuta las del 2do. archivo.



