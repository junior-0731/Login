import Datos as dt # se importara el modulo para verificar la existencia de el id
def ver_mascotas_V(): # funcion que busca las mascotas de un veterinario
    while True:
        veterinario_Buscar=input("Ingresa el id del veterinario: ")
        if veterinario_Buscar not in dt.ides_veterinarios:
            print("Ese veterinario no ha sido Registrado")
        else:
            break
    for i in dt.lista_Veterinarios: # Recorrer la lista de los veterinarios
        if i["ID"]==veterinario_Buscar: # Si el id es igual al que fue ingresado se mostraran las mascotas
            if i["Mascotas"]==[]: # si la lista esta vacia se muestra que no hay mascotas asignadas
                print("\n El veterinario aun no tiene mascotas asignadas\n")
            else: # de lo contrario se muestran los id de las mascotas
                print("\n MASCOTAS DEL VETERINARIO")
                print(i["Mascotas"]) 
            
            
    