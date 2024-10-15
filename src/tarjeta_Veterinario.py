def tarjeta(): # aca ira toda la informacion que se necesitara solicitar al veterinario para la tarjeta profesional
    diccionario_tarjeta={
        "Nombre":"",
        "Nombre Titulo":"",
        "Nombre Especialidad":"",
        "Nombre instituto":"",
        "Año":""
    }
    nombre_veterinario=input("Ingresa el nombre del veterinario: ")
    while True: 
        especialidad=input("Ingresa la especialidad: ")
        if especialidad.isalpha()==False:
            print("Error, ingresa solo str")
        else:
            break
        
    while True: 
        nombre_instituto=input("Ingresa el nombre del instituto: ")
        if nombre_instituto.isalpha()==False:
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
    diccionario_tarjeta["Nombre"]= nombre_veterinario
    diccionario_tarjeta["Nombre Titulo"]=nombre_titulo
    diccionario_tarjeta["Nombre Especialidad"]=especialidad
    diccionario_tarjeta["Nombre instituto"]=nombre_instituto
    diccionario_tarjeta["Año"]= Año
    
    return diccionario_tarjeta