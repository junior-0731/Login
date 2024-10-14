#Todas las clases principales
import Datos as dt
class Mascota:
    def __init__(self, nombre_mascota="",color="", especie="", raza="",propi = {}):
        self.nombre_mascota= nombre_mascota
        self.color = color
        self.especie= especie
        self.raza = raza
        self.propi = propi
        
    def registrar_Mascota(self):
        id_mascota= "121" # se debe generar de manera random
        if id_mascota in dt.ides_mascotas:
            print(f"La mascota {self.nombre_mascota} ya fue registrada")
        else:
            diccionario_mascota ={
                "ID":id_mascota,
                "Nombre":f"{self.nombre_mascota}",
                "Color": f"{self.color}",
                "Especie": f"{self.especie}",
                "Raza": f"{self.raza}",
                "Propietario":self.propi['ID']
            }

            dt.ides_mascotas.append(id_mascota)
            self.propi['Mascota'] = diccionario_mascota["ID"]
            dt.lista_Propietarios.append(self.propi)
            dt.lista_Mascotas.append(diccionario_mascota)
class Propietario:
    
    def __init__(self,id_Propietario = '',nombre_Propietario = '',apellidos_Propietario = '',direccion_Propietario = '',telefono_Propietario = '',correo_Propietario = '',mascota = {}):
        self.id_Propietario = id_Propietario
        self.nombre_Propietario = nombre_Propietario
        self.apellidos_Propietarios = apellidos_Propietario
        self.direccion_Propietario = direccion_Propietario
        self.telefono_Propietario = telefono_Propietario
        self.correo_Propietario = correo_Propietario
        self.mascota = mascota
    def registrar_Propietario(self):
        diccionaro_Propietario = {
            'ID':self.id_Propietario,
            'Nombres':self.nombre_Propietario,
            'Apellidos': self.apellidos_Propietarios,
            'Direccion':self.direccion_Propietario,
            'Telefono':self.telefono_Propietario,
            'Correo':self.correo_Propietario,
            'MascotaS': self.mascota['ID']
        }
        return diccionaro_Propietario

opcion = input('ELIGE UNA OPCION: ').upper()

if opcion == 'A':
    mascota1= Mascota('Lucas','Rojo','Perro','Pastor')
    propietario1 = Propietario("1313", "juan", "herrera", "urrao", "313132", "cdsfdsd",mascota={'ID':'123','Nombre':mascota1.nombre_mascota,'Color':mascota1.color,'Especie':mascota1.especie,'Raza':mascota1.raza})
    
    mascota1= Mascota('Lucas','Rojo','Perro','Pastor',propi={'ID':propietario1.id_Propietario,'Nombre':propietario1.nombre_Propietario,'Direccion':propietario1.direccion_Propietario,'Telefono':propietario1.telefono_Propietario,'Correo':propietario1.correo_Propietario})
    mascota1.registrar_Mascota()
    propietario1.registrar_Propietario()
    
elif opcion == 'B':
    propietario1 = Propietario("1313", "edier", "Guerra","Medeliin", "1313", "qdcsc")
    mascota1= Mascota("lucas", "red", "perro", "pastor", propi={"ID":propietario1.id_Propietario, "Nombre":propietario1.nombre_Propietario, "Apellidos":propietario1.apellidos_Propietarios, "Direccion":propietario1.direccion_Propietario, "Telefono":propietario1.telefono_Propietario,"Correo": propietario1.correo_Propietario})
    propietario1 = Propietario(id_Propietario="1313", nombre_Propietario="edier", apellidos_Propietario="Guerra",direccion_Propietario="Medeliin", telefono_Propietario="1313",correo_Propietario="qdcsc",mascota={"Nombre":mascota1.nombre_mascota, "Color":mascota1.color, "Especie": mascota1.especie,"Raza": mascota1.raza})
    mascota1.registrar_Mascota()

print(dt.lista_Propietarios)
print("")

print(dt.lista_Mascotas)