import Datos # se importo el modulo Datos
import tarjeta_Veterinario
from Actualizar_datos_Actores import Actualizar_Propietario, Actualizar_Veterinario # Se importo los modulo que se encuentran dentro de la carpeta Actualizar_datos_Actores
import Asignacion_mascota # Modulo que nos ayuda a que el admin pueda asignar una mascota a un veterinario
import Ver_mascotas # modulo que permite visualizar las mascotas de un veterinario
class Administrador:
    def __init__(self):
        pass
    def Registrar_Veterinario(): # Metodo que se encarga de registrar un veterinario
        print("\nREGISTRAR VETERINARIO\n")
        while True:
            # solicitar id de veterinario a registrar
            id_veterinario = input("Ingresa ID del veterinario: ")
            if id_veterinario.isalpha() == True:
                print("Ingresa solo caracteres numericos")
            elif len(id_veterinario) != 10:
                print("Error, ingresa solo 10 digitos")
            elif id_veterinario in Datos.ides_veterinarios:
                print("Error, ese veterinario ya fue registrado exitosamente")
            else:
                break
        Datos.ides_veterinarios.append(id_veterinario) # almacenar el id de veterinario en la lista de los ides de todos los veterinarios
        while True:
            nombre_veterinario = input("Ingresa el nombre del veterinario: ")
            if nombre_veterinario.isalpha()==False:
                print("Error, ingresa un nombre correcto")
            else:
                break
        while True:
            apellido_veterinario = input("Ingresa el Apellido del veterinario: ")
            if apellido_veterinario.isalpha()==False:
                print("Error, ingresa un nombre correcto")
            else:
                break
            
        while True:
            arroa="@gmail.com"
            correo_veterinario=input("Ingresa el correo electronico del veterinario: ")
            if arroa not in correo_veterinario:
                print("Ingresa el @gmail.com")
            else:
                break
            
        while True:
            Direccion_veterinario = input("Ingresa la direccion de veterinario: ")
            if Direccion_veterinario.isnumeric()== True:
                print("Error, no ingreses numeros")
            else:
                break
        while True:
            telefono_veterinario = input("Ingresa el numero telefonico: ")
            if telefono_veterinario.isnumeric() == False:
                print("Error, ingresa solo numeros")
            elif len(telefono_veterinario)  != 10:
                print("Error, ingresa un numero telefonico valido, (de 10 digitos)")
            else:
                break
        print("\n   TARJETA PROFESIONAL \n")
        tarjeta_profesional_veterinario=tarjeta_Veterinario.tarjeta() # se almacena toda la información de la tarjeta en esta variable
        diccionario_veterinario={
            "Id": id_veterinario,
            "Nombre": nombre_veterinario,
            "Apellido": apellido_veterinario,
            "Correo": correo_veterinario,
            "Direccion": Direccion_veterinario,
            "Telefono": telefono_veterinario,
            "tarjeta Profesional":[tarjeta_profesional_veterinario],
            "Mascotas": 0
            
            
        }
        Datos.lista_Veterinarios.append(diccionario_veterinario) # agregar toda la informacion de registro del veterinario  la lista con todos los veterinarios
        print("\n VETERINARIO REGISTRADO EXITOSAMENTE\n")
        print(diccionario_veterinario)
    def Actualizar_Datos(): #METODO ACTUALIZAR DATOS
        print("""ACTORES
            1. Veterinario
            2. Propietario
        """)
        while True:
            actor_seleccionado = input("Ingresa el numero del actor que desea actualizar: ")
            if actor_seleccionado != "1" and actor_seleccionado != "2":
                    print("Error, ingresa una opcion valida (1,2)")
            else:
                break 
        if actor_seleccionado == "1":
            Actualizar_Veterinario.modificar_veterinario() # se hace el llamado del modulo Actualizar_Veterinario
        elif actor_seleccionado =="2":
            Actualizar_Propietario.modificar_propietario() # se hace llamdo de el modulo Actualizar_Propietario
            
    def asignacion_mascota(): # METODO ASIGNAR MASCOTA
        Asignacion_mascota.modificar_mascota() # llamar modulo que contiene la funcion que se encarga de asignar una mascota a un veterinario #FALTA POR ACABAR    LE CORRESPONDE A CAMILO
        
    def Ver_mascotas_Veteriario(): # METODO DE VISUALIZAR MASCOTAS DE VETERINARIO
        Ver_mascotas.ver_mascotas_V()
        
Administrador.Registrar_Veterinario()
            
            
        


