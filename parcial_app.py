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
    menu = "\n1° EXAMEN PARCIAL 1° CUATRIMESTRE - DREAM TEAM\n\n"\
    "1 - Mostrar todos los jugadores del Dream Team\n"\
    "2 - Mostrar estadísticas de un jugador\n"\
    "3 - Buscar un jugador por su nombre y mostrar sus logros\n"\
    "4 - Mostrar promedio de puntos por partido de todo el Dream Team\n"\
    "5 - Mostrar si es Miembro del Salón de la Fama del Baloncesto\n"\
    "0 - SALIR\n"
    imprimir_dato(menu)


def menu_principal()->str:
    imprimir_menu()
    opcion = input("Seleccione opción: ")
    if re.match("[0-9]$",opcion):
        pass
    else:
        print("Opción inválida. Inténtelo nuevamente")
        opcion = -1
    return opcion


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
    nombre_archivo = ""
    opcion_exportar = ""
    match opcion:
        case "1":
            dato = obtener_todos_los_jugadores_y_su_posicion(lista)
        case "2":
            i_r = seleccionar_indice_rango(lista,"i")
            dato = obtener_estadisticas_por_indice_rango(lista,i_r,"i")
            nombre_archivo = "estadisticas_de_jugador_indice_{0}.csv".format(i_r)
            opcion_exportar = opcion
        case "3":
            patron_nombre = seleccionar_jugador_por_nombre()
            lista_jugador_logros = obtener_logros_por_nombre(lista,patron_nombre)
            if lista_jugador_logros != []:
                dato = generar_data_hasta_clave_rango(lista_jugador_logros)
                nombre_archivo = "logros_de_jugador_{0}.csv".format(patron_nombre[:3])
        case "4":
            lista_promedios_de_puntos_x_partido = obtener_estadistica_x_key_all_team(lista,"promedio_puntos_por_partido")
            ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,"list_dict_str","nombre")
            promedio_total = calcular_promedio(lista_promedios_de_puntos_x_partido,"promedio_puntos_por_partido")
            dato = generar_data_hasta_clave_rango(lista_promedios_de_puntos_x_partido)
            nombre_archivo = "promedio_puntos_por_partido_all_team.csv"
            imprimir_dato("Promedio total de puntos por partido de todo el Dream Team: {0:.2f}".format(promedio_total))
        case "5":
            patron_nombre = seleccionar_jugador_por_nombre()
            dato = obtener_jugador_salon_de_la_fama(lista,patron_nombre)
            nombre_archivo = "jugador_salon_de_la_fama.csv"
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
    if exportar == False and opcion_exportar == "2":
        consultar_exportar_archivo(lista_nombre_dato)
    return lista_nombre_dato


def obtener_nombre_y_todas_las_estadisticas(lista:list)->list:
    lista_nombre_y_estadisticas = []
    for i in range(len(lista)):
        diccio_auxiliar = {}
        diccio_auxiliar["nombre"] = lista[i]["nombre"]
        for key in lista[i]["estadisticas"]:
            diccio_auxiliar[key] = lista[i]["estadisticas"][key]
        lista_nombre_y_estadisticas.append(diccio_auxiliar)
    return lista_nombre_y_estadisticas


def obtener_estadistica_x_key_all_team(lista:list,key:str):
    lista_estadisticas = obtener_nombre_y_todas_las_estadisticas(lista)
    for i in range(len(lista_estadisticas)):
        diccio_aux = {}
        diccio_aux["nombre"] = lista_estadisticas[i]["nombre"]
        diccio_aux[key] = lista_estadisticas[i][key]
        lista_estadisticas[i] = diccio_aux
    return lista_estadisticas


def calcular_promedio(lista:list,key:str)->float:
    contador = 0
    acumulador = 0
    for diccio in lista:
        if key in diccio and (type(diccio[key]) == int or type(diccio[key]) == float):
            acumulador += diccio[key]
            contador += 1
    if contador > 0:
        promedio = acumulador / contador
    else:
        promedio = -1
    return promedio


def ordenar_bubble_sort(lista:list,tipo_dato:str,key:str,flag_orden:bool=True):
    rango = len(lista) 
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango -= 1
        for i in range(rango):
            if  flag_orden == False and retornar_tipo_dato(lista,tipo_dato,key,i) < retornar_tipo_dato(lista,tipo_dato,key,i+1) \
             or flag_orden == True and retornar_tipo_dato(lista,tipo_dato,key,i) > retornar_tipo_dato(lista,tipo_dato,key,i+1):
                lista[i],lista[i+1] = lista[i+1],lista[i]
                flag_swap = True


def retornar_tipo_dato(lista:list,tipo_dato:str,key:str,i:int):
    if tipo_dato == "list_dict_str":
        dato = lista[i][key][0]
    elif tipo_dato == "":
        pass
    return dato


def consultar_exportar_archivo(lista:list):
    consulta = input("Desea exportar los resultados a .csv (S/N): ")
    if re.match("^S$",consulta):
        guardar_archivo(lista[0],lista[1])
    elif re.match("^N$|[\w]",consulta):
        imprimir_dato("Se omitió creación de archivo")


def obtener_jugador_salon_de_la_fama(lista:list,pattern:str)->str:
    lista_logros_jugador = obtener_logros_por_nombre(lista,pattern)
    patron = "Salon de la Fama"
    flag_pertenece = False
    if re.search(r"{0}|{1}".format(patron,patron.lower()),lista_logros_jugador[0]["logros"]):
        flag_pertenece = True
    if flag_pertenece == True:
        mensaje = "{0} es Miembro del {1}".format(lista_logros_jugador[0]["nombre"],patron)
    else:
        mensaje = "{0} NO es Miembro del {1} del Baloncesto".format(lista_logros_jugador[0]["nombre"],patron)
    return mensaje


def obtener_logros_por_nombre(lista:list,pattern:str)->list:
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


def obtener_todos_los_jugadores_y_su_posicion(lista:list)->str:
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


def obtener_estadisticas_por_indice_rango(lista:list,index_range:int,tipo:str)->str:
    dato = ""
    lista_estadisticas = obtener_nombre_y_todas_las_estadisticas(lista)
    if tipo == "r":
        lista_estadisticas = lista_estadisticas[:index_range]
    elif tipo == "i":
        lista_estadisticas = lista_estadisticas[index_range-1:][0:1]
    dato = generar_data_hasta_clave_rango(lista_estadisticas)
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
    lista_jugadores = leer_archivo("D:\Archivos\Textos\Académicos\Tecnicatura en Programación\(1) Primer Cuatrimestre\ProgLab I\Ejercicios\Ejercicios_PARCIAL_1°_CUATRI\pp_lab1_cabello_angel\dt.json","jugadores")
except FileNotFoundError:
    print("\nError: No se encontró el archivo CSV en la ruta especificada\n")
if lista_jugadores != []:
    lista_jugadores_deepcopy = lista_jugadores[:]
    imprimir_dato("******LISTA DESCARGADA******\n")
    lanzar_app(lista_jugadores_deepcopy)

