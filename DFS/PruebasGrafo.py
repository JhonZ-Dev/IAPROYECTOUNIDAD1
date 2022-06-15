#----------------------IMPORTAREMOS LAS CLASES NECESARIAS-------------------# 
import unittest #Importamos la libreria unittest
import utils #Importamos la libreria utils
from ModuloGrafo import Grafo #Importamos la clase grafo 

#----------------------CLASE PRUEBAS-----------------------------------------#

class TestUtils(unittest.TestCase): #Creamos una clase para probar la libreria utils
    def test_dfs(self): #Creamos un metodo para probar el metodo dfs

        """
        Funcion destinada para comprobar la ruta del nodo
          return: True si el metodo dfs funciona correctamente
          metodo: dfs 
    
        """

        grafo = Grafo(20) #Instanciamos la clase grafo
        grafo.agregar_borde(0, 4) #Agregamos los bordes del grafo
        grafo.agregar_borde(4, 10)  #Agregamos los bordes del grafo
        grafo.agregar_borde(4, 11) #Agregamos los bordes del grafo
        grafo.agregar_borde(10, 16) #Agregamos los bordes del grafo
        grafo.agregar_borde(10, 17) #Agregamos los bordes del grafo
        grafo.agregar_borde(17, 19) #Agregamos los bordes del grafo

        #Segunda ruta posible para el nodo
        grafo.agregar_borde(1, 4) #Agregamos los bordes del grafo
        grafo.agregar_borde(1, 5) #Agregamos los bordes del grafo
        grafo.agregar_borde(5, 12) #Agregamos los bordes del grafo
        grafo.agregar_borde(12, 18) #Agregamos los bordes del grafo
        grafo.agregar_borde(18, 19) #Agregamos los bordes del grafo

        #Tercer ruta posible 
        grafo.agregar_borde(2, 6)   #Agregamos los bordes del grafo
        grafo.agregar_borde(2, 7)  #Agregamos los bordes del grafo
        grafo.agregar_borde(6, 13) #Agregamos los bordes del grafo
        grafo.agregar_borde(7, 13)  #Agregamos los bordes del grafo
        grafo.agregar_borde(13, 14) #Agregamos los bordes del grafo
        grafo.agregar_borde(13, 15) #Agregamos los bordes del grafo
        grafo.agregar_borde(14, 18) #Agregamos los bordes del grafo

        #Cuarta ruta posible

        grafo.agregar_borde(3, 8)   #Agregamos los bordes del grafo
        grafo.agregar_borde(3, 9)   #Agregamos los bordes del grafo
        grafo.agregar_borde(8, 15)  #Agregamos los bordes del grafo
        grafo.agregar_borde(9, 18)  #Agregamos los bordes del grafo
        self.assertEqual(grafo.dfs(0, 4),[0, 4]) #Comprobamos que el metodo dfs funciona correctamente y que el nodo 0 a 4 es el correcto

if __name__ == '__main__': #Creamos una clase para probar la libreria utils y ejecutamos el test
    unittest.main() #Llamamos al metodo main de la libreria unittest para probar la libreria utils
