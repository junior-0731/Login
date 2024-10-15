import Datos as dt # importare el modulo Datos para verificar las listas en este modulo
def modificar_propietario(): # funcion que actualiza los datos del propietario
    while True:
        propietario_modificar = input("Ingresa el ID del propietario: ") # solicitare el nombre del propietario
        if propietario_modificar not in dt.ides_propietarios: # si el id ingresado no se encuentra en la listra ides_propietarios, mostrar error
            print("No existe propietario con ese numero de ID")
        else:
            break
    for i in dt.lista_Propietarios: # recorrer la lista que contiene todos los propietarios
        if i["ID"]== propietario_modificar: # se accede a cada propietario y se compara su ID
            #Solicitar nuevos datos y control de excepciones
            while True:
                nueva_direccion = (input("Ingresa la direccion: "))
                if nueva_direccion.isnumeric()==True:
                    print("Error, no ingreses numeros")
                else:
                    break
                
            while True:
                nuevo_telefono = input("Ingresa el numero de telefono: ")
                if nuevo_telefono.isnumeric()== False:
                    print("No ingreses str")
                else:
                    break
            while True:
                arroa="@gmail.com"
                nuevo_correo=input("Ingresa el correo electronico del veterinario: ")
                if arroa not in nuevo_correo:
                    print("Ingresa el @gmail.com")
                else:
                    break
            #Reemplazar los valores de las claves
            i["Direccion"]=nueva_direccion
            i["Telefono"]=nuevo_telefono
            i["Correo"]= nuevo_correo
            print("\nInformación de Propietario Actualizada\n")
            print(i)
            
            
            
            

                    
                    
                    

            
            
            
