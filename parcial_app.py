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
    "6 - Jugador con la mayor cantidad de rebotes totales\n"\
    "7 - Jugador con el mayor porcentaje de tiros de campo\n"\
    "8 - Jugador con la mayor cantidad de asistencias totales\n"\
    "9 - Mostrar los jugadores que han promediado más puntos por partido\n"\
        "que el valor ingresado\n"\
    "10 - Mostrar los jugadores que han promediado más rebotes por partido\n"\
         "que el valor ingresado\n"\
    "11 - Mostrar los jugadores que han promediado más asistencias por partido\n"\
         "que el valor ingresado\n"\
    "12 - Jugador con la mayor cantidad de robos totales\n"\
    "13 - Jugador con la mayor cantidad de bloqueos totales\n"\
    "14 - Mostrar los jugadores que hayan tenido un porcentaje de tiros libres\n"\
         "superior al valor ingresado\n"\
    "15 - Mostrar el promedio de puntos por partido del equipo excluyendo\n"\
    "     al jugador con la menor cantidad de puntos por partido\n"\
    "16 - Jugador con la mayor cantidad de logros obtenidos\n"\
    "17 - \n"\
    "18 - Jugador con la mayor cantidad de temporadas jugadas\n"\
    "0 - SALIR\n"
    imprimir_dato(menu)


def menu_principal()->str:
    imprimir_menu()
    opcion = input("Seleccione opción: ")
    if re.match("[0-9]$|1[0-9]$",opcion):
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
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" | "13" | "14" | "15" | "16" | "17" | "18":
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
            lista_jugador_logros = obtener_nombre_y_logros_x_jugador(lista,patron_nombre)
            if lista_jugador_logros != []:
                dato = generar_data_hasta_clave_rango(lista_jugador_logros)
                nombre_archivo = "logros_de_jugador_{0}.csv".format(patron_nombre[:3])
        case "4":
            dato = mostrar_promedios_de_puntos_x_partido(lista)
            nombre_archivo = "promedio_puntos_por_partido_all_team.csv"
        case "5":
            patron_nombre = seleccionar_jugador_por_nombre()
            dato = obtener_jugador_salon_de_la_fama(lista,patron_nombre)
            nombre_archivo = "jugador_salon_de_la_fama.csv"
        case "6":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","rebotes_totales")
            nombre_archivo = "jugador_con_mayor_cant_rebotes_totales.csv"
        case "7":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","porcentaje_tiros_de_campo")
            nombre_archivo = "jugador_con_mayor_porcentaje_tiros_de_campo.csv"
        case "8":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","asistencias_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "9":
            valor = ingresar_y_validar_valor()
            lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,valor,"promedio_puntos_por_partido",True,"der")
            if lista_promedios != []:
                dato = generar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_puntos_por_partido_mayores_a_{0}.csv".format(valor)
        case "10":
            valor = ingresar_y_validar_valor()
            lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,valor,"rebotes_totales",True,"der")
            if lista_promedios != []:
                dato = generar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_rebotes_totales_mayores_a_{0}.csv".format(valor)
        case "11":
            valor = ingresar_y_validar_valor()
            lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,valor,"asistencias_totales",True,"der")
            if lista_promedios != []:
                dato = generar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_asistencias_totales_mayores_a_{0}.csv".format(valor)
        case "12":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","robos_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "13":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","bloqueos_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "14":
            valor = ingresar_y_validar_valor()
            lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,valor,"porcentaje_tiros_libres",True,"der")
            if lista_promedios != []:
                dato = generar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_libres_mayor_a_{0}.csv".format(valor)
        case "15":
            dato = mostrar_promedios_de_puntos_x_partido(lista,True)
            nombre_archivo = "promedio_puntos_por_partido_con_exclusion.csv"
        case "16":
            dato = mostrar_jugador_con_mayor_cant_logros(lista)
            nombre_archivo = "jugador_con_mayor_cant_logros.csv"
        case "17":
            valor = ingresar_y_validar_valor()
            lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,valor,"porcentaje_tiros_triples",True,"der")
            if lista_promedios != []:
                dato = generar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_triples_mayor_a_{0}.csv".format(valor)
        case "18":
            dato = obtener_mayor_menor_x_clave_estadistica(lista,"list_dict_num","temporadas")
            nombre_archivo = "jugador_con_mayor_cant_temporadas_jugadas.csv"
        case "19":
            pass
    if dato != "":
        imprimir_dato(dato)
        lista_nombre_dato.append(nombre_archivo)
        lista_nombre_dato.append(dato)
    if exportar == False and opcion_exportar == "2":
        consultar_exportar_archivo(lista_nombre_dato)
    return lista_nombre_dato


# def ordenar_jugadores_por_doble_key(lista:list,key_uno:str,key_dos:str,tipo_dato_uno:str,tipo_dato_dos:str,flag_uno:bool,flag_dos:bool):
#     lista_ordenada_key_uno = ordenar_bubble_sort(lista,tipo_dato_uno,key_uno,flag_uno)
#     lista_ordenada_key_dos = ordenar_bubble_sort(lista_ordenada_key_uno,tipo_dato_dos,key_dos,flag_dos)
#     return lista_ordenada_key_dos


def ingresar_y_validar_valor()->float:
    valor = input("Ingrese un valor entero mayor que 0: ")
    if re.match(r"[1-9]|[1-9]+\.[0-9][0-9]|[1-9][0-9]+|[1-9][0-9]+\.[0-9][0-9]",valor):
        valor = float(valor)
    else:
        imprimir_dato("Valor no válido. Inténtelo nuevamente")
        valor = -1
    return valor


def obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista:list,valor:float,key:str,menor_a_mayor:bool=True,izq_o_der:str="der")->list:
    lista_retorno = []
    if valor != -1:
        lista_estadisticas = obtener_estadistica_x_key_all_team(lista,key)
        ordenar_bubble_sort(lista_estadisticas,"list_dict_num",key)
        maximo = lista_estadisticas[len(lista_estadisticas)-1][key]
        if valor < maximo:
            lista_retorno = ordenar_quick_sort_reducida(lista_estadisticas,valor,key,menor_a_mayor,izq_o_der)
        else:
            imprimir_dato("El valor ingresado supera el máximo {0}. Inténtelo nuevamente".format(maximo))
    return lista_retorno


def ordenar_quick_sort_reducida(lista:list,valor:int,key:str,menor_a_mayor:bool=True,izq_o_der:str="der")->list:
    lista_retorno = []
    lista_izquierda = []
    lista_derecha = []
    pivot = valor
    for diccio in lista:
        if (menor_a_mayor == True and diccio[key] > pivot) or\
            (menor_a_mayor == False and diccio[key] < pivot):
            lista_derecha.append(diccio)
        elif (menor_a_mayor == True and diccio[key] < pivot) or\
                (menor_a_mayor == False and diccio[key] > pivot):
            lista_izquierda.append(diccio)
    if izq_o_der == "izq":
        lista_retorno.extend(lista_izquierda)
    elif izq_o_der == "der":
        lista_retorno.extend(lista_derecha)
    return lista_retorno


def mostrar_jugador_con_mayor_cant_logros(lista:list)->str:
    lista_ordenada_x_cant_logros = ordenar_x_cantidad_de_logros(lista)
    ultimo_indice = len(lista_ordenada_x_cant_logros)-1
    dato = "\nEl jugador con MAYOR cantidad de logros es: {0}, con {1} logros\n{2}".format(
        lista_ordenada_x_cant_logros[ultimo_indice]["nombre"],
        len(lista_ordenada_x_cant_logros[ultimo_indice]["logros"]),
        "\n".join(lista_ordenada_x_cant_logros[ultimo_indice]["logros"][:]))
    return dato


def ordenar_x_cantidad_de_logros(lista:list)->list:
    lista_copia = lista[:]
    ordenar_bubble_sort(lista_copia,"list_dict_len_key","logros")
    return lista_copia


def obtener_mayor_menor_x_clave_estadistica(lista:list,tipo_dato:str,key:str,max_min:str="mayor")->str:
    lista_estadisticas = obtener_nombre_y_todas_las_estadisticas(lista)
    ordenar_bubble_sort(lista_estadisticas,tipo_dato,key)
    if max_min == "mayor":
        jugador = lista_estadisticas[len(lista_estadisticas)-1]
    elif max_min == "menor":
        jugador = lista_estadisticas[0]
    key = re.sub("_"," ",key)
    if re.search(r"^porc",key) or re.search(r"^prom",key):
        subtring = "{0} {1}".format(max_min.upper(),key)
    else:
        subtring = "{0} cantidad de {1}".format(max_min.upper(),key)
    dato = "El jugador con {0} es: {1}, con: {2}".format(subtring,jugador["nombre"],jugador[re.sub(" ","_",key)])
    return dato


def obtener_nombre_y_todas_las_estadisticas(lista:list)->list:
    lista_nombre_y_estadisticas = []
    for i in range(len(lista)):
        diccio_auxiliar = {}
        diccio_auxiliar["nombre"] = lista[i]["nombre"]
        for key in lista[i]["estadisticas"]:
            diccio_auxiliar[key] = lista[i]["estadisticas"][key]
        lista_nombre_y_estadisticas.append(diccio_auxiliar)
    return lista_nombre_y_estadisticas


def mostrar_promedios_de_puntos_x_partido(lista:list,exclusion:bool=False)->str:
    lista_promedios_de_puntos_x_partido = obtener_estadistica_x_key_all_team(lista,"promedio_puntos_por_partido")
    if exclusion == True:
        ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,"list_dict_num","promedio_puntos_por_partido")
        diccio_excluido = lista_promedios_de_puntos_x_partido[0]
        lista_promedios_de_puntos_x_partido.pop(0)
        imprimir_dato("Excluido: {},{}".format(diccio_excluido["nombre"],diccio_excluido["promedio_puntos_por_partido"]))
    else:
        ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,"list_dict_str","nombre")
    promedio_total = calcular_promedio(lista_promedios_de_puntos_x_partido,"promedio_puntos_por_partido")
    dato = generar_data_hasta_clave_rango(lista_promedios_de_puntos_x_partido)
    dato = "Promedio total de puntos por partido de todo el Dream Team: {0:.2f}\n{1}".format(promedio_total,dato)
    return dato


def obtener_estadistica_x_key_all_team(lista:list,key:str)->list:
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


def ordenar_bubble_sort(lista:list,tipo_dato:str,key:str,flag_orden:bool=True)->None:
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


def retornar_tipo_dato(lista:list,tipo_dato:str,key:str,i:int)->None:
    if tipo_dato == "list_dict_str":
        dato = lista[i][key][0]
    elif tipo_dato == "list_dict_num":
        dato = lista[i][key]
    elif tipo_dato == "list_dict_len_key":
        dato = len(lista[i][key])
    return dato


def consultar_exportar_archivo(lista:list):
    consulta = input("Desea exportar los resultados a .csv (S/N): ")
    if re.match("^S$",consulta):
        guardar_archivo(lista[0],lista[1])
    elif re.match("^N$|[\w]",consulta):
        imprimir_dato("Se omitió creación de archivo")


def obtener_jugador_salon_de_la_fama(lista:list,pattern:str)->str:
    lista_logros_jugador = obtener_nombre_y_logros_all_dream_team(lista,pattern)
    patron = "Salon de la Fama"
    flag_pertenece = False
    if re.search(r"{0}|{1}".format(patron,patron.lower()),lista_logros_jugador[0]["logros"]):
        flag_pertenece = True
    if flag_pertenece == True:
        mensaje = "{0} es Miembro del {1}".format(lista_logros_jugador[0]["nombre"],patron)
    else:
        mensaje = "{0} NO es Miembro del {1} del Baloncesto".format(lista_logros_jugador[0]["nombre"],patron)
    return mensaje


def obtener_nombre_y_logros_x_jugador(lista:list,pattern:str)->list:
    lista_nombre_logros = obtener_nombre_y_logros_all_dream_team(lista)
    lista_retorno = []
    for diccio in lista_nombre_logros:
        if re.search(r"{0}".format(pattern),diccio["nombre"]) or\
            re.search(r"{0}".format(pattern),diccio["nombre"].lower()):
            lista_retorno.append(diccio)
        else:
            imprimir_dato("No se encontraron coincidencias. Inténtelo nuevamente")
    return lista_retorno


def obtener_nombre_y_logros_all_dream_team(lista:list)->list:
    lista_retorno = []
    for i in range(len(lista)):
        diccio_nombre_logros = {}
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


def exportar_csv(lista:list)->None:
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
    print("\nError: No se encontró el archivo .json en la ruta especificada\n")
if lista_jugadores != []:
    lista_jugadores_deepcopy = lista_jugadores[:]
    imprimir_dato("******LISTA CARGADA******\n")
    lanzar_app(lista_jugadores_deepcopy)

