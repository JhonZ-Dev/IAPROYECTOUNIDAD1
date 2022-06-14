from queue import Queue # Importa la clase Queue de la libreria queue
import unittest # Importa el modulo unittest
import networkx as nx # Importa el modulo networkx
import matplotlib.pyplot as plt # Importa el modulo matplotlib.pyplot

class Grafo:
    def __init__(self, numeros_de_nodos, nodo_dirigido=True): # Definir la función __init__ para el grafo de tipo Grafo
        """
        Inicializa el grafo con un número de nodos y una variable booleana que indica si el grafo es dirigido o no

        Args:
            numeros_de_nodos (__tipo__): Número de nodos del grafo
            nodo_dirigido (bool, optional): Indica si el grafo es dirigido o no
            
            Retorna:
            __tipo__: Número de nodos del grafo
        """
        self.m_num_of_nodes = numeros_de_nodos # Asigna el número de nodos del grafo
        self.m_nodos = range(self.m_num_of_nodes) # Asigna el rango de nodos del grafo
        self.m_nodo_dirigido = nodo_dirigido # Asigna el valor de la variable nodo_dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos} # Asigna la lista de adyacencia del grafo


    #----------------------------Funciones para agregar el bordes al nodo--------------------

    def agregar_borde(self, nodo1, nodo2, peso_nodo=1):
        """
        Funcion destnada para agregar un borde al grafo

        Args:
            nodo1 (__tipo__): Nodo 1 del border
            nodo2 (__tipo__): Nodo 2 del border
            peso_nodo (__tipo__, optional): Peso del border
                
                Retorna:    __tipo__: Nodo 1 del border.
                Retorna:    __tipo__: Nodo 2 del border.
                Retorna:    __tipo__: Peso del border.
            """
 
        self.m_lista_adyacencia[nodo1].add((nodo2, peso_nodo)) # Agrega el borde al nodo1 en la lista de adyacencia del grafo con el nodo2 y el peso del border
        if not self.m_nodo_dirigido:# Si el grafo no es dirigido se agrega el borde al nodo2 en la lista de adyacencia del grafo con el nodo1 y el peso del border
            self.m_lista_adyacencia[nodo2].add((nodo1, peso_nodo)) # Agrega el borde al nodo2 en la lista de adyacencia del grafo con el nodo1 y el peso del border y lo agrega al nodo1

    #----------------------------Funciones para la lista adyecencia de la funcion al nodo--------------------
    def lista_adyacencia(self):
        """
        Una lista de adyacencia es un tipo de representación gráfica en código, consiste en llaves que representan cada nodo, y un colocar de valores
        para cada uno de ellos que contienen nodos que están conectados al nodo clave con un 
        borde.

        Args:            
            Retorna:    __tipo__: Lista de adyacencia del grafo en forma de diccionario con los nodos y sus bordes.
          """  
        for key in self.m_lista_adyacencia.keys(): # Recorre la lista de adyacencia del grafo y asigna los nodos y sus bordes a un diccionario con llaves y valores de nodos y bordes	
            print("nodo:    ", key, ": ", self.m_lista_adyacencia[key])   # Imprime el nodo y sus bordes en la lista de adyacencia del grafo


    #----------------------------Funcion para la busqueda en aplitud (DFS)--------------------
    def dfs(self, comienzo, objetivo, camino=[], nodo_visitado=set()):
        """
        Funcion destnada para la busqueda en profundidad (DFS)
            
            Args: 
                comienzo (__tipo__): Nodo inicial de la busqueda
                objetivo (__tipo__): Nodo final de la busqueda
                camino (__tipo__, optional): Camino que se va agusarando en la busqueda
                nodo_visitado (__tipo__, optional): Nodos que ya fueron visitados en la busqueda
                    
                    Retorna:    __tipo__: Camino que se va agusarando en la busqueda
                    Retorna:    __tipo__: Nodos que ya fueron visitados en la busqueda
        """
        camino.append(comienzo) # Agrega el nodo inicial al camino que se va agusarando en la busqueda en la funcion dfs de tipo lista de nodos y se lo asigna a la variable camino de tipo lista de nodos
        nodo_visitado.add(comienzo)  # Agrega el nodo inicial al nodo_visitado de tipo set de nodos y se lo asigna a la variable nodo_visitado de tipo set de nodos
        if comienzo == objetivo: # Si el nodo inicial es el nodo final se retorna el camino que se va agusarando en la busqueda
            return camino # Retorna el camino que se va agusarando en la busqueda 
        for (nodos_no_visitados, weight) in self.m_lista_adyacencia[comienzo]:# Recorre la lista de adyacencia del grafo y asigna los nodos no visitados y los pesos de los bordes a un diccionario con llaves y valores de nodos y bordes
            if nodos_no_visitados not in nodo_visitado:# Si el nodo no fue visitado se lo agrega al nodo_visitado de tipo set de nodos y se lo asigna a la variable nodo_visitado de tipo set de nodos
                resultado = self.dfs(nodos_no_visitados, objetivo, camino, nodo_visitado) # Llama a la funcion dfs de tipo lista de nodos y se lo asigna a la variable resultado de tipo lista de nodos
                if resultado is not None: # Si el resultado de la funcion dfs de tipo lista de nodos no es nulo se retorna el resultado de la funcion dfs de tipo lista de nodos
                    return resultado # Retorna el resultado de la funcion dfs de tipo lista de nodos
        camino.pop() # Elimina el ultimo nodo del camino que se va agusarando en la busqueda en la funcion dfs de tipo lista de nodos y se lo asigna a la variable camino de tipo lista de nodos
        return None # Retorna nulo si el resultado de la funcion dfs de tipo lista de nodos es nulo
    

