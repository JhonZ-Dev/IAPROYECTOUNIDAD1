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

    """
        Funcion creada para que el usuario puede digitar la ubicacion del robot,
       
    """
    estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0', 'D': '0', 'E': '0', 'F': '0','G': '0'} # estado objetivo
    costo = 0  # costo
    listaRes=['A','B','C','D','E','F', 'G'] # lista de ubicaciones
    
    print("Digite la ubicación del robot") #El usuario digita la ubicación del robot
    ubicacionRobot= input("") #Leeremos lo que el usuario digita
    while ubicacionRobot >='a': #Ciclo for para validar que solo digite mayusculas
        print("Error, vuelva a digita una letra mayúscula") #mensaje de error
        ubicacionRobot = input('Vuelva a ingresar la ubicación del robot ') #Volver a ingresar la ubicacion del robot