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
                              for i in range (0,7): #Ciclo for para mostrar la lista de ubicaciones
                                   if ubicacionRobot == listaRes[i]: #Si la ubicacion del robot es igual a la lista de ubicaciones
                                        pass #No hacemos nada
                                   else:#Si no es igual a la lista de ubicaciones
                                        hectareasRes = int(input( "Digite el estado de la hectarea: " + listaRes[i]))
                                        while hectareasRes != 1 and hectareasRes != 0:
                                             print("Error, vuelva a digita un valor entre 0 y 1" + listaRes[i])
                                             hectareasRes = int(input( "Digite el estado de la hectarea: " + listaRes[i]))
                                        if hectareasRes == 1:
                                             print("El área no está regaga")
                                             print("Procediendo a recolectar las hectareas")
                                             print("*** PROCESANDO...........*******") 
                                             print("|******************************|")#Simulando un pequeño sistema
                                             print("|****RECOLECTANDO MANZANAS*****|")#Simulando un pequeño sistema
                                             print("|******************************|")#Simulando un pequeño sistema
                                             print("") #Espacio
                                             print("Hectareas totalmente recolectadas")#Hectareas recolectadas
                                             print("El estado objetivo es:")#printiamos el estado del objetivo
                                             print(estadoObjetivo)#Objetivo
                                             costo+=1#Como cumple la opcion, aumenta el costo
                                             print("El valor del costo es:  ")#mostramos el costo
                                             print(costo)#mostramos el costo

                                        else:  #caso contrario, si todo no esta correcto
                                             print("Hectareas regadas") #mostramos la hectareas
                                             print("El costo se mantiene igual " + str(costo)) #Concatenamos el valor del costo
                                             if hectareasRes == 0:
                                                  print("***La hectarea no está recolectada")
                                                  print("*DIRIGIENDOSE A LA HECTAREA ")
                                                  print("El costo se mantiene igual " + str(costo))             
                    break #Cerramos el ciclo while
               except ValueError: #Mostramos la excepcion
                    print("Error, Ingrese un valor numérico") #Mostramos un mensaje     
                                       
                                       


