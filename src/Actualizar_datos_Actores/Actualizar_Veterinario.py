import Datos as dt
def modificar_veterinario():
    while True:
        # solicitar id de veterinario a modificar
        veterinario_modificar = input("Ingresa ID del veterinario: ")
        if veterinario_modificar.isalpha() == True:
            print("Ingresa solo caracteres numericos")
        elif len(veterinario_modificar) != 10:
            print("Error, ingresa solo 10 digitos")
        elif veterinario_modificar not in dt.ides_veterinarios:
            print("Error, ese veterinario no existe")
        else:
            break
    # se recorrera la lista de los veterinarios
    for i in dt.lista_Veterinarios:
        # se verificara si el id de este veterinario es igual al que se ingreso
        if i["Id"]==veterinario_modificar: 
            # Datos a modificar

            while True:
                arroa="@gmail.com"
                nuevo_correo=input("Ingresa el correo electronico del veterinario: ")
                if arroa not in nuevo_correo:
                    print("Ingresa el @gmail.com")
                else:
                    break
                
            while True:
                nueva_direccion = input("Ingresa la direccion de veterinario: ")
                if nueva_direccion.isnumeric()== True:
                    print("Error, no ingreses numeros")
                else:
                    break
            while True:
                nuevo_telefono = input("Ingresa el numero telefonico: ")
                if nuevo_telefono.isnumeric() == False:
                    print("Error, ingresa solo numeros")
                elif len(nuevo_telefono)  != 10:
                    print("Error, ingresa un numero telefonico valido, (de 10 digitos)")
                else:
                    break
            i["Telefono"]=nuevo_telefono 
            i["Direccion"]= nueva_direccion
            i["Correo"]=nuevo_correo
                
            #solicitar eliminación de mascota
            while True:
                eliminar_mascota_v= input("Deseas eliminar una mascota del veterinario: ").lower()
                if eliminar_mascota_v != "si" and eliminar_mascota_v !="no":
                    print("Error, digita si/no")
                else:
                    break
            if eliminar_mascota_v == "si": # si desea eliminar una mascota
                if i["Mascotas"] == "" or i["Mascotas"]==0: # se verifica si tiene mascotas agregadas
                    print("Este Veterinario no tiene mascotas") # en caso de que no se muestra este mensaje
                    print("")
                else:# en caso de que si tenga mascotas agregadas
                    
                    print("Mascotas de veterinario")
                    print(i["Mascotas"])
                    print("")
                    while True:
                        id_mascota_eliminar=input("ingresa el id de la mascota a eliminar: ")
                        if id_mascota_eliminar not in i["Mascotas"]:
                            print("Error, esa mascota no se encuentra.")
                        else: 
                            break
                    i["Mascotas"].remove(id_mascota_eliminar)# gracias a la funcion remove puedo eliminar un valor especifico de una    clave
                    print("")
            else:
                pass
            print("Información actualizada")
            print("")
            print(i) # imprimira el diccionario de los datos del veterinario que se modifico
            
    print("")
    print(dt.lista_Veterinarios)
        
        