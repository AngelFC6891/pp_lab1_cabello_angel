import re
import json
import pprint

'''
Tema: EXAMEN PARCIAL 1° CUATRIMESTRE

Apellido: Cabello
Nombre: Ángel Fabián
'''

def imprimir_dato(string:str):
    print(string)


def imprimir_menu():
    menu = "\n1° EXAMEN PARCIAL 1° CUATRI.\n"\
    "1 - Mostrar todos los jugadores del Dream Team\n"\
    "2 - Mostrar estadísticas de un jugador\n"\
    "3 - \n"\
    "4 - \n"\
    "0 - SALIR\n"
    imprimir_dato(menu)


def menu_principal()->str:
    imprimir_menu()
    opcion = input("Seleccione opción: ")
    if re.match("[0-4]$",opcion):
        return opcion
    else:
        print(-1)


def continuar():
    input("\nPresione enter para continuar")


def lanzar_app(lista:list):
    while True:
        opcion_seleccionada = menu_principal()
        match opcion_seleccionada:
            case "0":
                break
            case "1" | "2" | "3":
                ejecutar_match_anidado(lista,opcion_seleccionada)
            case "3":
                exportar_csv(lista)
        continuar()


def ejecutar_match_anidado(lista:list,opcion:str,archivar:bool=False)->str:
    dato = ""
    match opcion:
        case "1":
            dato = generar_data_x_clave_rango(lista,"posicion")
            lista_lineas = re.split("\n",dato)
            lista_datos = []
            for linea in lista_lineas:
                lista_datos.append(re.sub(","," - ",linea))
            dato = "\n".join(lista_datos[:])
        case "2":
            pass
        case "3":
            pass
    imprimir_dato(dato)
    return dato


def exportar_csv(lista:list):
    opcion = seleccionar_opcion_a_guardar()
    if opcion != "-1":
        new_data = ejecutar_match_anidado(lista,opcion,True)
        guardar_archivo(new_data)


def seleccionar_opcion_a_guardar()->str:
    opcion = input("Seleccione opción a guardar (1-4): ")
    if re.match("[1-4]$",opcion):
        retorno = opcion
    else:
        imprimir_dato("Opción inválida. Inténtelo nuevamente")
        retorno = "-1"
    return retorno


def leer_archivo(name_file:str,clave:str)->list:
    lista_retorno = []
    with open(name_file,"r") as file:
        diccio_datos = json.load(file)
        lista_retorno = diccio_datos[clave]
    return lista_retorno


def guardar_archivo(name_file:str,new_data:str)->bool:
    with open(name_file,"w+") as file:
        bytes = file.write(new_data)
    if bytes == 0:
        imprimir_dato("Error al crear el archivo: {0}".format(name_file))
        resultado = False
    else:
        imprimir_dato("Se creó el archivo: {0}".format(name_file))
        resultado = True
    return resultado
    

def generar_data_x_clave_rango(lista:list,key:str=None,rango:int=None)->str:
    if rango == None:
        rango = len(lista)
    linea = ""
    for i in range(rango):
        if i == 0:
            linea = generar_encabezado_x_key(lista,key)
        else:
            nueva_linea = generar_linea(lista,i,key)
            linea = "{0}\n{1}".format(linea,nueva_linea)
    return linea


def generar_linea(lista:list,i:int,key:str=None)->str:
    linea = ""
    if key == None and key != "estadistica" and key != "logros":
        linea = "{0}".format(lista[i]["nombre"])
        for clave in lista[i]:
            if clave != "nombre":
                linea = "{0},{1}".format(linea,lista[i][clave])
    elif key == "nombre":
        linea = "{0}".format(lista[i][key])
    elif key == "estadisticas":
        lista_values = []
        for clave in lista[i][key]:
            lista_values.append(clave)
        linea = ",".join(lista_values[:])
    else:
        linea = "{0}".format(lista[i]["nombre"])
        if key in lista[i]:
            linea = "{0},{1}".format(linea,lista[i][key])
    return linea


def generar_encabezado_x_key(lista:list,key:str=None)->str:
    lista_encabezado = []
    if key == None and key != "estadistica" and key != "logros":
        for clave in lista[0]:
            lista_encabezado.append(clave.capitalize())
    elif key == "nombre":
        lista_encabezado.append(key.capitalize())
    elif key == "estadistica":
        lista_encabezado = list(lista[1][key].keys())
    else:
        lista_encabezado.append("Nombre")
        lista_encabezado.append(key.capitalize())
    encabezado = ",".join(lista_encabezado[:])
    return encabezado


def listar_x_patron(lista:list,patron:str):
    lista_resultado = []
    patron = r"({0})".format(patron)
    for elemento in lista:
        if not re.search(patron,elemento["clave"]):
            lista_resultado.append(elemento)
    return lista_resultado


lista_jugadores = leer_archivo("D:\Archivos\Textos\Académicos\Tecnicatura en Programación\(1) Primer Cuatrimestre\ProgLab I\Ejercicios\Ejercicios_PARCIAL_1°_CUATRI\dt.json","jugadores")
lista_jugadores_deepcopy = lista_jugadores[:]
if lista_jugadores_deepcopy != []:
    imprimir_dato("******LISTA DESCARGADA******\n")
    lanzar_app(lista_jugadores_deepcopy)