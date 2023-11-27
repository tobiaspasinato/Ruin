def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except:
        print(f"Error al leer el archivo {nombre_archivo}")
        return False

def guardar_archivo(nombre_archivo, contenido):
    print(nombre_archivo, contenido)
    try:
        archivo = open(nombre_archivo, "a")
        print(archivo)
        archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al intentar crear el archivo")
        return False

def generar_csv(nombre_ruta : str, lista_personajes : list):
    if len(lista_personajes) > 0:
        contenido = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        for personaje in lista_personajes:
            contenido = contenido + f"{personaje['nombre']},{personaje['identidad']},{personaje['empresa']},{personaje['altura']},{personaje['peso']},{personaje['genero']},{personaje['color_ojos']},{personaje['color_pelo']},{personaje['fuerza']},{personaje['inteligencia']}\n"
        guardar_archivo(nombre_ruta, contenido)
    else:
        return False

def leer_csv(nombre_ruta) -> list:
    lista = []
    contenido = leer_archivo(nombre_ruta)
    if not contenido:
        return False
    contenido = contenido.split("\n")
    cabecera = contenido[0].split(",")
    for elemento in contenido[1:-1]:
        dicc = {}
        personaje = elemento.split(",")
        for indice in range(len(cabecera)):
            dicc[cabecera[indice]] = personaje[indice]
        lista.append(dicc)
    return lista