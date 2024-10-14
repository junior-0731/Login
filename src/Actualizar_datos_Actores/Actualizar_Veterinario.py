import Datos as dt # se importara el modulo donde se encontrara toda la información
def modificar_veterinario():
    while True:
        # solicitar id de veterinario a modificar
        veterinario_modificar = input("Ingresa el del veterinario: ")
        if veterinario_modificar.isalpha() == True:
            print("Ingresa solo caracteres numericos")
        elif len(veterinario_modificar) != 10:
            print("Error, ingresa solo 10 digitos")
        elif veterinario_modificar in dt.ides_veterinarios:
            print("Error, ese veterinario ya fue registrado exitosamente")
        else:
            break
    for i in dt.lista_Veterinarios:
        for j in i.values():
            print(j)