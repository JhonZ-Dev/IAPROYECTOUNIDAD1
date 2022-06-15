from ModuloHectareas import ingresoUsuarioDatos #Importar la función ingresoUsuarioDatos
import unittest #Importar el modulo unittest
class TestRobot(unittest.TestCase): #   Definir la clase TestRobot
    
    def test_ingresoUsuarioDatos(self): #   Definir la función test_ingresoUsuarioDatos
        """
        Funcion destinada a hacer las pruebas unitarias para comparar si el ingreso de los
        datos del usuario es correcto
        """
        #self.assertEqual(ingresoUsuarioDatos(), 'A') #   Comparar el resultado de la función ingresoUsuarioDatos con el valor esperado
        self.assertEqual(ingresoUsuarioDatos(), ingresoUsuarioDatos()) #   Comparar el resultado de la función ingresoUsuarioDatos con el valor esperado


if __name__ == '__main__': #   Definir la función main
    #   Ejecutar el modulo unittest
    unittest.main() #   Llamar a la función main