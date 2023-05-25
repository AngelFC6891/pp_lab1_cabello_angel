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
    "3 - Buscar un jugador por su nombre y mostrar sus logros\n"\
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
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                ejecutar_match_anidado(lista,opcion_seleccionada)
            case "20":
                exportar_csv(lista)
        continuar()


def ejecutar_match_anidado(lista:list,opcion:str,exportar:bool=False)->str:
    lista_nombre_dato = []
    dato = ""
    match opcion:
        case "1":
            dato = mostrar_todos_los_jugadores_y_su_posicion(lista)
        case "2":
            i_r = seleccionar_indice_rango(lista,"i")
            dato = mostrar_estadisticas_por_indice_rango(lista,i_r,"i")
            nombre_archivo = "estadisticas_de_jugador_indice_{0}.csv".format(i_r)
            caso = "2"
        case "3":
            caso = ""
            patron = seleccionar_jugador_por_nombre()
            lista_jugador_logros = mostrar_logros_por_nombre(lista,patron)
            if lista_jugador_logros != []:
                dato = generar_data_hasta_clave_rango(lista_jugador_logros)
                nombre_archivo = "logros_de_jugador_{0}.csv".format(patron[:3])
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "14":
            pass
        case "15":
            pass
    if dato != "":
        imprimir_dato(dato)
        lista_nombre_dato.append(nombre_archivo)
        lista_nombre_dato.append(dato)
    if exportar == False and caso == "2":
        consultar_guardar_archivo(lista_nombre_dato)
    return lista_nombre_dato


def consultar_guardar_archivo(lista:list):
    consulta = input("Desea exportar los resultados a csv (S/N): ")
    if re.match("^S$",consulta):
        guardar_archivo(lista[0],lista[1])


def mostrar_logros_por_nombre(lista:list,pattern:str)->list:
    lista_retorno = []
    if pattern != "":
        for i in range(len(lista)):
            diccio_nombre_logros = {}
            if re.search(r"{0}".format(pattern),lista[i]["nombre"]) or\
               re.search(r"{0}".format(pattern),lista[i]["nombre"].lower()):
                diccio_nombre_logros["nombre"] = lista[i]["nombre"]
                diccio_nombre_logros["logros"] = "/".join(lista[i]["logros"][:])
                lista_retorno.append(diccio_nombre_logros)
        if lista_retorno == []:
            imprimir_dato("No se encontraron coincidencias. Inténtelo nuevamente")
    return lista_retorno


def seleccionar_jugador_por_nombre()->str:
    nombre = input("Escribir nombre de jugador: ")
    patron = ""
    if re.match(r"^[A-Za-z ]{3}",nombre):
        patron = nombre
    else:
        imprimir_dato("Nombre inválido. Inténtelo nuevamente")
    return patron


def mostrar_todos_los_jugadores_y_su_posicion(lista:list)->str:
    dato = generar_data_hasta_clave_rango(lista,"posicion")
    lista_lineas = re.split("\n",dato)
    lista_datos = []
    for linea in lista_lineas:
        lista_datos.append(re.sub(","," - ",linea))
    dato = "\n".join(lista_datos[:])
    return dato


def seleccionar_indice_rango(lista:list,tipo:str)->int:
    if tipo == "r":
        indice_rango = input("Mostrar estadísticas hasta el jugador número (1-{0}): ".format(len(lista)))
    elif tipo == "i":
        indice_rango = input("Mostrar estadísticas del jugador número (1-{0}): ".format(len(lista)))
    if re.match("([0-9]+)$",indice_rango) and int(indice_rango) <= len(lista):
        indice_rango = int(indice_rango)
    else:
        indice_rango = -1
        imprimir_dato("Número inválido. Inténtelo nuevamente\n")
    return indice_rango


def mostrar_estadisticas_por_indice_rango(lista:list,index_range:int,tipo:str)->str:
    dato = ""
    lista_estadisticas = []
    if tipo == "r":
        for i in range(index_range):
            lista_estadisticas.append(lista[i]["estadisticas"])
    elif tipo == "i":
        lista_estadisticas.append(lista[index_range-1]["estadisticas"])
    nombres = generar_data_hasta_clave_rango(lista,"nombre",index_range)
    estadisticas = generar_data_hasta_clave_rango(lista_estadisticas)
    lista_nombres = re.split("\n",nombres)
    lista_estadisticas_aux = re.split("\n",estadisticas)
    if tipo == "i":
        lista_nombres[1:len(lista_nombres)-1] = []
    lista_nombres_estadisticas = []
    if len(lista_nombres) == len(lista_estadisticas_aux):
        for i in range(len(lista_nombres)):
            lista_nombres_estadisticas.append(f"{lista_nombres[i]},{lista_estadisticas_aux[i]}")
        dato = "\n".join(lista_nombres_estadisticas[:])
    return dato


def exportar_csv(lista:list):
    opcion = seleccionar_opcion_a_guardar()
    if opcion != "-1":
        lista_name_data = ejecutar_match_anidado(lista,opcion,True)
        if len(lista_name_data) < 2:
            imprimir_dato("Error. Archivo vacío o incompleto")
        else:
            guardar_archivo(lista_name_data[0],lista_name_data[1])


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
    

def generar_data_hasta_clave_rango(lista:list,clave:str=None,rango:int=None)->str:
    if rango == None:
        rango = len(lista)
    if rango >= 1:
        linea = generar_encabezado_hasta_clave(lista,clave)
        for i in range(rango):
            nueva_linea = generar_linea_hasta_clave(lista,i,clave)
            linea = "{0}\n{1}".format(linea,nueva_linea)
        return linea


def generar_linea_hasta_clave(lista:list,i:int,clave:str=None)->str:
    lista_claves = list(lista[i].keys())
    for j in range(len(lista_claves)):
        if j == 0:
            linea = "{0}".format(lista[i][lista_claves[j]])
        else:
            linea = "{0},{1}".format(linea,lista[i][lista_claves[j]])
        if clave != None and clave == lista_claves[j]:
            break
    return linea


def generar_encabezado_hasta_clave(lista:list,clave:str=None)->str:
    lista_encabezado = []
    for key in lista[0]:
        lista_encabezado.append(key.capitalize())
        if clave != None and clave.capitalize() in lista_encabezado:
            break
    if len(lista_encabezado) > 1:
        encabezado = ",".join(lista_encabezado[:])
    else:
        encabezado = lista_encabezado[0]
    return encabezado

lista_jugadores = []
try:
    lista_jugadores = leer_archivo("D:\PROGLAB\Ejercicios_PARCIAL_1°_CUATRI_pendrive\pp_lab1_cabello_angel\dt.json","jugadores")
except FileNotFoundError:
    print("\nError: No se encontró el archivo CSV en la ruta especificada\n")
if lista_jugadores != []:
    lista_jugadores_deepcopy = lista_jugadores[:]
    imprimir_dato("******LISTA DESCARGADA******\n")
    lanzar_app(lista_jugadores_deepcopy)