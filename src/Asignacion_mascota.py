import Datos as dt # importare el modulo Datos para verificar las listas en este modulo
def asignar():
    print("""\n BUSCAR \n
        1. POR ID DE PROPIETARIO
        2. POR ID MASCOTA""") # metodos de busqueda
    while True: # Control de excepciones
        metodo_Buscar = input("Ingresa Opcion de busqueda: ")
        if metodo_Buscar != "1" and metodo_Buscar !="2": 
            print("Ingresa una opcion valida (1,2)")
        else:
            break
    if metodo_Buscar == "1": # si selecciona opcion 1
        pass #  FALTA CONTINUAR 
    