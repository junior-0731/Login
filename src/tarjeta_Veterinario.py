def tarjeta(): # aca ira toda la informacion que se necesitara solicitar al veterinario para la tarjeta profesional
    diccionario_tarjeta={
        "Nombre Especialidad":"",
        "Año":"",
        "Nombre Titulo":"",
        "Nombre Completo":""
    }
    while True: 
        especialidad=input("Ingresa la especialidad: ")
        if especialidad.isalpha()==False:
            print("Error, ingresa solo str")
        else:
            break
    while True: 
        Año=input("Ingresa el año de certificación: ")
        if Año.isnumeric()==False:
            print("Error, ingresa solo numeros")
        else:
            break
    while True: 
        nombre_titulo=input("Ingresa el titulo: ")
        if nombre_titulo.isalpha()==False:
            print("Error, ingresa solo str")
        else:
            break
    nombre_completo=input("Ingresa el nombre completo: ")
    diccionario_tarjeta["Nombre Especialidad"]=especialidad
    diccionario_tarjeta["Año"]= Año
    diccionario_tarjeta["Nombre Titulo"]=nombre_titulo
    diccionario_tarjeta["Nombre Completo"]= nombre_completo
    
    return diccionario_tarjeta