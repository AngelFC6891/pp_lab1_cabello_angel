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
    "    que el valor ingresado\n"\
    "10 - Mostrar los jugadores que han promediado más rebotes por partido\n"\
    "     que el valor ingresado\n"\
    "11 - Mostrar los jugadores que han promediado más asistencias por partido\n"\
    "     que el valor ingresado\n"\
    "12 - Jugador con la mayor cantidad de robos totales\n"\
    "13 - Jugador con la mayor cantidad de bloqueos totales\n"\
    "14 - Mostrar los jugadores que hayan tenido un porcentaje de tiros libres\n"\
    "     superior al valor ingresado\n"\
    "15 - Mostrar el promedio de puntos por partido del equipo excluyendo\n"\
    "     al jugador con la menor cantidad de puntos por partido\n"\
    "16 - Jugador con la mayor cantidad de logros obtenidos\n"\
    "17 - Mostrar los jugadores que hayan tenido un porcentaje de tiros triples\n"\
    "     superior al valor ingresado\n"\
    "18 - Jugador con la mayor cantidad de temporadas jugadas\n"\
    "19 - Mostrar los jugadores, ordenados por posición en la cancha, que hayan\n"\
    "     tenido un porcentaje de tiros de campo superior al valor ingresado\n"\
    "20 - BONUS !!! Mostrar la posición de cada jugador en los siguientes rankings:\n"\
    "               Puntos, Rebotes, Asistencias y Robos\n"\
    "21 - Exportar a .csv\n"\
    "0 - SALIR\n"
    imprimir_dato(menu)


def menu_principal()->str:
    imprimir_menu()
    opcion = input("Seleccione opción: ")
    if re.match(r"[0-9]$|1[0-9]$|2[0-1]$",opcion):
        pass
    else:
        print("Opción inválida. Inténtelo nuevamente")
        opcion = "-1"
    return opcion


def continuar():
    input("\nPresione enter para continuar")


def lanzar_app(lista:list):
    while True:
        opcion_seleccionada = menu_principal()
        match opcion_seleccionada:
            case "0":
                break
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" |\
                  "12" | "13" | "14" | "15" | "16" | "17" | "18" | "19" | "20":
                ejecutar_match_anidado(lista,opcion_seleccionada)
            case "21":
                exportar_csv(lista)
        continuar()


def ejecutar_match_anidado(lista:list,opcion:str,exportar:bool=False)->str:
    lista_nombre_dato = []
    dato = ""
    nombre_archivo = ""
    opcion_exportar = ""
    imprimir_con_formato = False
    match opcion:
        case "1":
            dato = mostrar_data_hasta_clave_rango(lista,"posicion")
        case "2":
            i_r = seleccionar_indice_rango(lista,"i")
            if i_r != -1:
                dato = mostrar_estadisticas_por_indice_rango(lista,i_r,"i")
                imprimir_con_formato = consultar_imprimir_con_formato()
                nombre_archivo = "estadisticas_de_jugador_indice_{0}.csv".format(i_r)
                opcion_exportar = opcion
        case "3":
            patron_nombre = seleccionar_jugador_por_nombre()
            if patron_nombre != "":
                lista_jugador_logros = obtener_nombre_y_logros_x_jugador(lista,patron_nombre)
                dato = mostrar_data_hasta_clave_rango(lista_jugador_logros)
                imprimir_con_formato = consultar_imprimir_con_formato()
                nombre_archivo = "logros_de_jugador_{0}.csv".format(patron_nombre[:3])
        case "4":
            dato = mostrar_promedios_de_puntos_x_partido(lista)
            nombre_archivo = "promedio_puntos_por_partido_all_team.csv"
        case "5":
            patron_nombre = seleccionar_jugador_por_nombre()
            if patron_nombre != "":
                dato = mostrar_jugador_salon_de_la_fama(lista,patron_nombre)
                nombre_archivo = "jugador_salon_de_la_fama.csv"
        case "6":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","rebotes_totales")
            nombre_archivo = "jugador_con_mayor_cant_rebotes_totales.csv"
        case "7":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","porcentaje_tiros_de_campo")
            nombre_archivo = "jugador_con_mayor_porcentaje_tiros_de_campo.csv"
        case "8":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","asistencias_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "9":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                            valor,
                                                                                            "promedio_puntos_por_partido",
                                                                                            True,
                                                                                            "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_puntos_por_partido_mayores_a_{0}.csv".format(valor)
        case "10":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "rebotes_totales",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_rebotes_totales_mayores_a_{0}.csv".format(valor)
        case "11":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "asistencias_totales",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_asistencias_totales_mayores_a_{0}.csv".format(valor)
        case "12":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","robos_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "13":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","bloqueos_totales")
            nombre_archivo = "jugador_con_mayor_cant_asistencias_totales.csv"
        case "14":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "porcentaje_tiros_libres",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_libres_mayor_a_{0}.csv".format(valor)
        case "15":
            dato = mostrar_promedios_de_puntos_x_partido(lista,True)
            nombre_archivo = "promedio_puntos_por_partido_con_exclusion.csv"
        case "16":
            dato = mostrar_jugador_con_mayor_cant_logros(lista)
            nombre_archivo = "jugador_con_mayor_cant_logros.csv"
        case "17":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "porcentaje_tiros_triples",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_triples_mayor_a_{0}.csv".format(valor)
        case "18":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","temporadas")
            nombre_archivo = "jugador_con_mayor_cant_temporadas_jugadas.csv"
        case "19":
            valor = ingresar_y_validar_valor()
            if valor != -1.0:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "porcentaje_tiros_de_campo",
                                                                                        True,
                                                                                        "der",
                                                                                        "posicion")
                lista_reordenada = obtener_lista_ordenada_x_key_estadistica_y_key_jugador(lista_promedios,
                                                                                        "porcentaje_tiros_de_campo",
                                                                                        "posicion",
                                                                                        "list_dict_num",
                                                                                        "list_dict_str",
                                                                                        True,
                                                                                        True)
                dato = mostrar_data_hasta_clave_rango(lista_reordenada)
                nombre_archivo = "posiciones_A_Z_promedios_tiros_de_campo_mayor_a_{0}.csv".format(valor)
        case "20":
            lista_jugadores_rankeados = obtener_todos_los_ranking_por_jugador(lista)
            dato = mostrar_data_hasta_clave_rango(lista_jugadores_rankeados)
            nombre_archivo = "jugadores_rankeados.csv"
            opcion_exportar = opcion

    if dato != "":
        if imprimir_con_formato == False:
            imprimir_dato(dato)
        else:
            imprimir_dato_con_formato(dato)
        lista_nombre_dato.append(nombre_archivo)
        lista_nombre_dato.append(dato)
    if exportar == False and opcion_exportar == "2" or opcion_exportar == "20":
        consultar_exportar_archivo(lista_nombre_dato)
    return lista_nombre_dato


def imprimir_dato_con_formato(string:str)->str:
    lista_lineas = re.split("\n",string)
    lista_encabezados = re.split(",",lista_lineas[0])
    dato_retorno = ""
    lista_datos_formateados = []
    for i in range(1,len(lista_lineas)):
        lista_datos = re.split(",",lista_lineas[i])
        dato_formateado = ""
        for j in range(len(lista_datos)):
            dato = "{0}: {1}".format(lista_encabezados[j],lista_datos[j])
            dato_formateado = "{0}{1}\n".format(dato_formateado,dato)
        lista_datos_formateados.append(dato_formateado)
    dato_retorno = "\n".join(lista_datos_formateados[:])
    imprimir_dato(dato_retorno)


def consultar_imprimir_con_formato()->bool:
    consulta = input("Desea desea imprimir datos con formato? (S/N): ")
    flag_consulta = True
    if re.match("^S$",consulta):
        pass
    else:
        imprimir_dato("Se omitió opción de imprimir datos con formato\n")
        flag_consulta = False
    return flag_consulta


def obtener_lista_ordenada_x_key_estadistica_y_key_jugador(lista:list,
                                                           key_uno:str,
                                                           key_dos:str,
                                                           tipo_dato_uno:str,
                                                           tipo_dato_dos:str,
                                                           flag_uno:bool,
                                                           flag_dos:bool)->list:
    ordenar_bubble_sort(lista,
                        tipo_dato_uno,
                        key_uno,
                        flag_uno)
    ordenar_bubble_sort(lista,
                        tipo_dato_dos,
                        key_dos,
                        flag_dos)
    return lista


def obtener_todos_los_ranking_por_jugador(lista:list)->list:
    lista_estadisticas = obtener_nombre_key_y_todas_las_estadisticas(lista)
    lista_claves = ["puntos_totales","rebotes_totales","asistencias_totales","robos_totales"]
    lista_retorno = []
    for clave in lista_claves:
        ordenar_bubble_sort(lista_estadisticas,"list_dict_num",clave,False)
        ranking = 0
        if lista_retorno == []:
            for diccio in lista_estadisticas:
                ranking += 1
                diccio_aux = {}
                diccio_aux["nombre"] = diccio["nombre"]
                diccio_aux[re.sub("_totales","",clave)] = ranking
                lista_retorno.append(diccio_aux)
        else:
            for diccio in lista_estadisticas:
                ranking += 1
                for dictionary in lista_retorno:
                    if dictionary["nombre"] == diccio["nombre"]:
                        dictionary[re.sub("_totales","",clave)] = ranking
                        break
    return lista_retorno


def ingresar_y_validar_valor()->float:
    valor = input("Ingrese un valor mayor que 0: ")
    if re.match(r"[1-9]|[1-9]+\.[0-9][0-9]|[1-9][0-9]+|[1-9][0-9]+\.[0-9][0-9]",valor):
        valor = float(valor)
    else:
        imprimir_dato("Valor no válido. Inténtelo nuevamente")
        valor = -1.0
    return valor


def obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista:list,
                                                              valor:float,
                                                              key_estadistica:str,
                                                              menor_a_mayor:bool=True,
                                                              izq_o_der:str="der",
                                                              key:str=None)->list:
    lista_retorno = []
    lista_estadisticas = obtener_estadistica_x_key_all_dream_team(lista,key_estadistica,key)
    ordenar_bubble_sort(lista_estadisticas,"list_dict_num",key_estadistica)
    maximo = lista_estadisticas[len(lista_estadisticas)-1][key_estadistica]
    if valor < maximo:
        lista_retorno = ordenar_quick_sort_reducida(lista_estadisticas,
                                                    valor,
                                                    key_estadistica,
                                                    menor_a_mayor,
                                                    izq_o_der)
    else:
        imprimir_dato("El valor ingresado supera el máximo {0}. Inténtelo nuevamente".format(maximo))
    return lista_retorno


def ordenar_quick_sort_reducida(lista:list,
                                valor:int,
                                key:str,
                                menor_a_mayor:bool=True,
                                izq_o_der:str="der")->list:
    lista_retorno = []
    lista_izquierda = []
    lista_derecha = []
    pivot = valor
    for diccio in lista:
        if menor_a_mayor == True and diccio[key] > pivot or\
           menor_a_mayor == False and diccio[key] < pivot:
            lista_derecha.append(diccio)
        elif menor_a_mayor == True and diccio[key] < pivot or\
             menor_a_mayor == False and diccio[key] > pivot:
            lista_izquierda.append(diccio)
    if izq_o_der == "izq":
        lista_retorno.extend(lista_izquierda)
    elif izq_o_der == "der":
        lista_retorno.extend(lista_derecha)
    return lista_retorno


def mostrar_jugador_con_mayor_cant_logros(lista:list)->str:
    lista_ordenada_x_cant_logros = ordenar_x_cantidad_de_logros(lista)
    ultimo_indice = len(lista_ordenada_x_cant_logros) - 1
    dato = "\nEl jugador con MAYOR cantidad de logros es: {0}, con {1} logros\n{2}".format(
        lista_ordenada_x_cant_logros[ultimo_indice]["nombre"],
        len(lista_ordenada_x_cant_logros[ultimo_indice]["logros"]),
        "\n".join(lista_ordenada_x_cant_logros[ultimo_indice]["logros"][:]))
    return dato


def ordenar_x_cantidad_de_logros(lista:list)->list:
    lista_copia = lista[:]
    ordenar_bubble_sort(lista_copia,"list_dict_len_key","logros")
    return lista_copia


def mostrar_mayor_menor_x_clave_estadistica(lista:list,
                                            tipo_dato:str,
                                            key:str,
                                            max_min:str="mayor")->str:
    lista_estadisticas = obtener_nombre_key_y_todas_las_estadisticas(lista)
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


def obtener_nombre_key_y_todas_las_estadisticas(lista:list,key:str=None)->list:
    lista_nombre_y_estadisticas = []
    for i in range(len(lista)):
        diccio_auxiliar = {}
        diccio_auxiliar["nombre"] = lista[i]["nombre"]
        if key != None:
            diccio_auxiliar[key] = lista[i][key]
        for clave in lista[i]["estadisticas"]:
            diccio_auxiliar[clave] = lista[i]["estadisticas"][clave]
        lista_nombre_y_estadisticas.append(diccio_auxiliar)
    return lista_nombre_y_estadisticas


def obtener_estadistica_x_key_all_dream_team(lista:list,key_estadistica:str,key:str=None)->list:
    lista_estadisticas = obtener_nombre_key_y_todas_las_estadisticas(lista,key)
    lista_retorno = []
    for i in range(len(lista_estadisticas)):
        diccio_aux = {}
        diccio_aux["nombre"] = lista_estadisticas[i]["nombre"]
        if key != None:
            diccio_aux[key] = lista_estadisticas[i][key]
        diccio_aux[key_estadistica] = lista_estadisticas[i][key_estadistica]
        lista_retorno.append(diccio_aux)
    return lista_retorno


def mostrar_promedios_de_puntos_x_partido(lista:list,exclusion:bool=False)->str:
    lista_promedios_de_puntos_x_partido = obtener_estadistica_x_key_all_dream_team(lista,"promedio_puntos_por_partido")
    dato = ""
    dato_excluido = ""
    if exclusion == True:
        ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,"list_dict_num","promedio_puntos_por_partido")
        diccio_excluido = lista_promedios_de_puntos_x_partido[0]
        lista_promedios_de_puntos_x_partido.pop(0)
        dato_excluido = "Excluido: {0},{1}\n".format(diccio_excluido["nombre"],diccio_excluido["promedio_puntos_por_partido"])
    else:
        ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,"list_dict_str","nombre")
    promedio_total = calcular_promedio(lista_promedios_de_puntos_x_partido,"promedio_puntos_por_partido")
    dato = mostrar_data_hasta_clave_rango(lista_promedios_de_puntos_x_partido)
    dato = "{0}Promedio total de puntos por partido de todo el Dream Team: {1:.2f}\n{2}".format(dato_excluido,promedio_total,dato)
    return dato


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


def ordenar_bubble_sort(lista:list,
                        tipo_dato:str,
                        key:str,
                        flag_orden:bool=True)->None:
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


def retornar_tipo_dato(lista:list,
                       tipo_dato:str,
                       key:str,
                       i:int)->None:
    if tipo_dato == "list_dict_str":
        dato = lista[i][key][0]
    elif tipo_dato == "list_dict_num":
        dato = lista[i][key]
    elif tipo_dato == "list_dict_len_key":
        dato = len(lista[i][key])
    return dato


def consultar_exportar_archivo(lista:list):
    consulta = input("Desea exportar los resultados a .csv? (S/N): ")
    if re.match("^S$",consulta):
        guardar_archivo(lista[0],lista[1])
    else:
        imprimir_dato("Se omitió creación de archivo")


def mostrar_jugador_salon_de_la_fama(lista:list,pattern:str)->str:
    dato = ""
    lista_logros_jugador = obtener_nombre_y_logros_x_jugador(lista,pattern)
    if lista_logros_jugador != []:
        patron = "Salon de la Fama"
        flag_pertenece = False
        if re.search(r"{0}|{1}".format(patron,patron.lower()),lista_logros_jugador[0]["logros"]):
            flag_pertenece = True
        if flag_pertenece == True:
            dato = "{0} es Miembro del {1}".format(lista_logros_jugador[0]["nombre"],patron)
        else:
            dato = "{0} NO es Miembro del {1} del Baloncesto".format(lista_logros_jugador[0]["nombre"],patron)
    return dato


def obtener_nombre_y_logros_x_jugador(lista:list,pattern:str)->list:
    lista_nombre_logros = obtener_nombre_y_logros_all_dream_team(lista)
    lista_retorno = []
    for diccio in lista_nombre_logros:
        if re.search(r"{0}".format(pattern),diccio["nombre"]) or\
            re.search(r"{0}".format(pattern),diccio["nombre"].lower()):
            lista_retorno.append(diccio)
    if lista_retorno == []:
        imprimir_dato("No se encontraron coincidencias. Inténtelo nuevamente")
    return lista_retorno


def obtener_nombre_y_logros_all_dream_team(lista:list)->list:
    lista_retorno = []
    for i in range(len(lista)):
        diccio_nombre_logros = {}
        diccio_nombre_logros["nombre"] = lista[i]["nombre"]
        diccio_nombre_logros["logros"] = " - ".join(lista[i]["logros"][:])
        lista_retorno.append(diccio_nombre_logros)
    return lista_retorno


def seleccionar_jugador_por_nombre()->str:
    nombre = input("Escribir nombre de jugador: ")
    patron = ""
    if re.match(r"^[A-Za-z ]{3}",nombre):
        patron = nombre
    else:
        imprimir_dato("Nombre inválido. Inténtelo nuevamente")
    return patron


def seleccionar_indice_rango(lista:list,tipo:str)->int:
    '''
    Parámetros: una lista de diccionarios y un string
    Retorno: un número entero
    Función: solicita al usuario ingresar un número dentro de un\\
    intervalo predefinido, lo valida con regex, lo convierte a entero\\
    y lo retorna. Si el número ingresado no es válido retornará un - 1\\
    (tipo entero). El parámetro 'tipo' cambia el formato de la oración\\
    con la que se solicita el ingreso del número.
    '''
    if tipo == "r": subtring = "hasta el"
    elif tipo == "i": subtring = "del"
    indice_rango = input("Mostrar estadísticas {0} jugador número (1-{1}): ".format(subtring,len(lista)))
    if re.match("([0-9]+)$",indice_rango) and int(indice_rango) <= len(lista):
        indice_rango = int(indice_rango)
    else:
        indice_rango = -1
        imprimir_dato("Número inválido. Inténtelo nuevamente\n")
    return indice_rango


def mostrar_estadisticas_por_indice_rango(lista:list,index_range:int,tipo:str)->str:
    '''
    Parámetros: una lista de diccionarios, un entero y un string
    Retorno: un string concatenado con saltos de linea
    Función: a partir de la lista de jugadores del Dream Team, crea una nueva lista
    de jugadores (diccionarios) cuyas claves son: el nombre del jugador más todas\\
    sus estadísticas (son todas las claves del diccionario de estadísticas dentro del\\
    diccionario/jugador). Luego esta nueva lista se puede recortar de acuerdo a los\\
    parámetros 'index_range' y 'tipo'. Con 'tipo' se indica si el 'index_range' es un\\
    índice ('i') o un rango ('r'), e 'index_range' será el número que actuará de índice\\
    o rango (primer jugador hasta la posición indicada inclusive) según el caso. Por\\
    defecto, la función creará una lista con todos los jugadores y sus estadísticas.\\
    Por último se vuelca la información de la lista ya filtrada en un string concatenado.
    '''
    dato = ""
    lista_estadisticas = obtener_nombre_key_y_todas_las_estadisticas(lista)
    if tipo == "r":
        lista_estadisticas = lista_estadisticas[:index_range]
    elif tipo == "i":
        lista_estadisticas = lista_estadisticas[index_range-1:][0:1]
    dato = mostrar_data_hasta_clave_rango(lista_estadisticas)
    return dato


def exportar_csv(lista:list)->None:
    '''
    Parámetros: una lista con dos elementos string: nombre del\\
    archivo y el dato a archivar, en ese preciso orden
    Retorno: no tiene
    Función: solicita al usuario ingresar un número dentro de un\\
    intervalo predefinido, lo pasa a una estructura de control 'match'
    y de allí obtiene una lista con dos elementos: nombre de archivo\\
    y dato string a archivar, en ese orden. Si dicha lista contiene\\
    estos dos elementos, creará un archivo csv donde será guardado el\\
    dato tipo string. Caso contrario, se imprimirá por terminal un aviso\\
    de error.
    '''
    opcion = seleccionar_opcion_a_guardar()
    if opcion != "-1":
        lista_name_data = ejecutar_match_anidado(lista,opcion,True)
        if len(lista_name_data) < 2:
            imprimir_dato("Error. Archivo vacío o incompleto")
        else:
            guardar_archivo(lista_name_data[0],lista_name_data[1])


def seleccionar_opcion_a_guardar()->str:
    '''
    Parámetros: no requiere
    Retorno: un número entero en formato string
    Función: solicita al usuario ingresar un número dentro de\\
    un intervalo predefinido, lo valida y lo devuelve. En caso\\
    de ingresar un 'número' no admitido, imprime un aviso por\\
    terminal y devuelve el string '-1'
    '''
    opcion = input("Seleccione opción a guardar (1-20): ")
    if re.match(r"[0-9]$|1[0-9]$|20$",opcion):
        retorno = opcion
    else:
        imprimir_dato("Opción inválida. Inténtelo nuevamente")
        retorno = "-1"
    return retorno


def leer_archivo_json(path_name_file:str,clave:str)->list:
    '''
    Parámetros: ruta del archivo (necesario), atributo principal (o sea,\\
    una lista) del archivo json (necesario)
    Retorno: una lista de diccionarios
    Función: lee la información del archivo json para luego cargarla en\\
    formato de lista de diccionarios
    '''
    lista_retorno = []
    with open(path_name_file,"r") as file:
        diccio_datos = json.load(file)
        lista_retorno = diccio_datos[clave]
    return lista_retorno


def guardar_archivo(name_file:str,new_data:str)->bool:
    '''
    Parámetros: nombre de archivo (necesario), datos a escribir (necesario)
    Retorno: booleano 'True' si el archivo se creó correctamente, y en caso\\
    contrario devuelve 'False'\\
    Función: crea un archivo con la extensión indicada en 'name_file' cuyo\\
    contenido será la información almacenada en 'new_data'. El modo de\\
    escritura es 'w+'.
    '''
    with open(name_file,"w+") as file:
        bytes = file.write(new_data)
        flag_guardado = True
    if bytes == 0:
        imprimir_dato("Error al crear el archivo: {0}".format(name_file))
        flag_guardado = False
    else:
        imprimir_dato("Se creó el archivo: {0}".format(name_file))
    return flag_guardado 
    

def mostrar_data_hasta_clave_rango(lista:list,clave:str=None,rango:int=None)->str:
    '''
    Parámetros: lista de diccionarios (necesario), clave de diccionario (opcional),\\
    un rango de iteración tipo entero (opcional)
    Retorno: string concatenado\\
    Función: recibe la lista, genera un encabezado con todas las claves del primer\\
    diccionario, luego itera la lista y genera un string concatenado separado por\\
    un salto de línea. Cada linea contiene los valores de todas las claves de cada\\
    diccionario separados por una ',' (coma). Por defecto, la función itera todos los\\
    diccionarios de la lista y todas las claves dentro de cada uno. Caso contrario,\\
    va a iterar hasta el indice o clave que se le indique a través de los parámetros\\
    opcionales 'rango' y 'clave' respectivamente.
    '''
    linea = ""
    if rango == None:
        rango = len(lista)
    if rango >= 1:
        linea = generar_encabezado_hasta_clave(lista,clave)
        for i in range(rango):
            nueva_linea = generar_linea_hasta_clave(lista,i,clave)
            linea = "{0}\n{1}".format(linea,nueva_linea)
    return linea


def generar_linea_hasta_clave(lista:list,i:int,clave:str=None)->str:
    '''
    Parámetros: lista de diccionarios (necesario), posición de un diccionario\\
    (necesario) y clave del diccionario (opcional)
    Retorno: string de valores de claves\\
    Función: recibe la lista y la posición de uno de sus diccionarios. Luego\\
    toma todos los valores de todas sus claves y los concatena en un solo\\
    string usando una ',' (coma) como separador. El parámetro opcional permite\\
    tomar los valores desde la primera clave hasta el valor de la clave indicada.
    '''
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
    '''
    Parámetros: lista de diccionarios (necesario), clave del diccionario (opcional)
    Retorno: string de claves\\
    Función: recibe la lista, toma todas las claves del primer diccionario y las\\
    concatena en un solo string usando una ',' (coma) como separador. El parámetro\\
    opcional permite tomar las claves desde la primera hasta la clave indicada.
    '''
    lista_encabezado = []
    for key in lista[0]:
        lista_encabezado.append(re.sub("_"," ",key).capitalize())
        if clave != None and clave.capitalize() in lista_encabezado:
            break
    if len(lista_encabezado) > 1:
        encabezado = ",".join(lista_encabezado[:])
    else:
        encabezado = lista_encabezado[0]
    return encabezado


lista_dream_team = []
try:
    lista_dream_team = leer_archivo_json("D:\Archivos\Textos\Académicos\Tecnicatura en Programación\(1) Primer Cuatrimestre\ProgLab I\Ejercicios\Ejercicios_PARCIAL_1°_CUATRI\pp_lab1_cabello_angel\dt.json","jugadores")
except FileNotFoundError:
    print("\nError: No se encontró el archivo .json en la ruta especificada\n")
if lista_dream_team != []:
    lista_dream_team_deepcopy = lista_dream_team[:]
    imprimir_dato("\n****** LISTA DREAM TEAM CARGADA ******")
    lanzar_app(lista_dream_team_deepcopy)