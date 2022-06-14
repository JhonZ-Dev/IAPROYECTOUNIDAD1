def mensajeUsuario():
     """
     Funcion que muestra un mensaje al usuario
     mandamos como variable a estado objetivo
     y el valor del costo
     finalemente se muestr el mensaje al usuario
     """

     estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0', 'D': '0', 'E': '0', 'F': '0','G': '0'} # estado objetivo
  
     costo = 0 # costo
     # se muestra el mensaje al usuario
     print(""" 
     *****Estimado usuario, existen siete ubicaciones (Hectareas de plantación)*******  
         |-------------------------*****Hectarea_1 = 'A'*****-------------------------|
         |-------------------------*****Hectarea_2 = 'B'*****-------------------------|
         |-------------------------*****Hectarea_3 = 'C'*****-------------------------|
         |-------------------------*****Hectarea_4 = 'D'*****-------------------------|
         |-------------------------*****Hectarea_5 = 'E'*****-------------------------|
         |-------------------------*****Hectarea_6 = 'F'*****-------------------------|
         |-------------------------*****Hectarea_7 = 'G'*****-------------------------|
         |-------------------------*****Hectarea_8 = 'H'*****-------------------------|
     """) # se muestra el mensaje al usuario. 



def ingresoUsuarioDatos():
     estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0', 'D': '0', 'E': '0', 'F': '0','G': '0'} # estado objetivo
     costo = 0  # costo
     listaRes=['A','B','C','D','E','F', 'G'] # lista de ubicaciones
    
     print("Digite la ubicación del robot") #El usuario digita la ubicación del robot
     ubicacionRobot= input("") #Leeremos lo que el usuario digita
     while ubicacionRobot >='a': #Ciclo for para validar que solo digite mayusculas
          print("Error, vuelva a digita una letra mayúscula") #mensaje de error
          ubicacionRobot = input('Vuelva a ingresar la ubicación del robot ') #Volver a ingresar la ubicacion del robot

     if ubicacionRobot == 'A': #Si la ubicacion del robot es A
          print('La ubicación del robot es: A')#Mostramos donde se encuentra el robtot
          while True: #Ciclo while para validar que el usuario digite una letra de la lista
               try: #Intentar validar que el usuario digite una letra de la lista
                    hectarea = int(input("Estado de la hectarea")) #Le pedimos al usuario el estado
                    if hectarea == 1:#Si el estado es 1
                         if hectarea == 1: #Si hectarea es igual a 1
                              estadoObjetivo['A'] = '0' #Entonces cambiamos de estado
                         #Informa que está recolectando las manzanas
                              print("|******************************|")#Simulando un pequeño sistema
                              print("|****RECOLECTANDO MANZANAS*****|")#Simulando un pequeño sistema
                              print("|******************************|")#Simulando un pequeño sistema
                              print("")#Simulando un pequeño sistema
                              print("")#Simulando un pequeño sistema
                              print("")#Simulando un pequeño sistema
                              print("|******************************|")#Simulando un pequeño sistema
                              print("|****MANZANAS RECOLECTADAS*****|")#Simulando un pequeño sistema
                              print("|******************************|")#Simulando un pequeño sistema
                              #AUMENTAMOS EL VALOR DEL COSTO
                              costo+= 1
                              #Mostramos el valor del costo
                              print("El valor del costo =1    "   + str(costo)) #Simulando un pequeño sistema
                              print("|******************************|")#Simulando un pequeño sistema
                              print("|****HECTAREA 1 RECOLECTADA*****|")#Simulando un pequeño sistema
                              print("|******************************|")#Simulando un pequeño sistemat   