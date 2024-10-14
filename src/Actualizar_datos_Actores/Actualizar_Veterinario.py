import tarjeta_Veterinario
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
            while True:
                mod_tarjeta_profesional= input("Desea agregar otra tarjeta profesional si/no: ").lower()
                if mod_tarjeta_profesional != "si" and mod_tarjeta_profesional != "no":
                    print("Error, ingresa si/no")
                else:
                    break
            if mod_tarjeta_profesional =="si":  
                print("\n   TARJETA PROFESIONAL \n")
                nueva_tarjeta_profesional_veterinario = tarjeta_Veterinario.tarjeta() # se llama la funcion tarjeta del modulo tarjeta_veterinario
                i["Telefono"]=nuevo_telefono 
                i["Direccion"]= nueva_direccion
                i["Correo"]=nuevo_correo
                i["tarjeta Profesional"].append(nueva_tarjeta_profesional_veterinario)
            else:
                i["Telefono"]=nuevo_telefono 
                i["Direccion"]= nueva_direccion
                i["Correo"]=nuevo_correo
            
            print("Información actualizada")
            print("")
            print(i) # imprimira el diccionario de los datos del veterinario que se modifico
            
    print("")
    print(dt.lista_Veterinarios)
        
        