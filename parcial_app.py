import re
import json

'''
Tema: 1er EXAMEN PARCIAL 1er CUATRIMESTRE

Apellido: Cabello
Nombre: Ángel Fabián
'''

def imprimir_dato(string:str):
    print(string)


def imprimir_menu():
    '''
    Parámetros: no requiere
    Retorno: no tiene
    Descripción: imprime por terminal el menú de opciones, el cual es un solo string\\
    concatenado con saltos de linea.
    '''
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
    "21 - Mostrar cantidad total de jugadores de cada posición\n"\
    "22 - Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de\n"\
    "     forma descendente\n"\
    "23 - Mostrar cuál jugador tiene la mejor estadística en cada rubro\n"\
    "24 - Mostrar qué jugador tiene las mejores estadísticas de todos\n"\
    "25 - Exportar a .csv\n"\
    "0 - SALIR\n"
    imprimir_dato(menu)


def menu_principal()->str:
    '''
    Parámetros: no requiere
    Retorno: un string
    Descripción: imprime por terminal el menú de opciones, solicita al usuario\\
    que ingrese la opción deseada (un entero tipo string) y la valida con regex\\
    entre las opciones posibles del menú. En caso de ser válida, la retorna y si\\
    no, retornará '-1' imprimiendo por terminal un aviso de error.
    '''
    imprimir_menu()
    opcion = input("Seleccione opción: ")
    if re.match(r"[0-9]$|1[0-9]$|2[0-5]$",opcion):
        pass
    else:
        print("Opción inválida. Inténtelo nuevamente")
        opcion = "-1"
    return opcion


def continuar():
    input("\nPresione enter para continuar")


def lanzar_app(lista:list):
    '''
    Parámetros: lista de diccionarios (necesaria)
    Retorno: no tiene
    Descripción: recibe la lista de jugadores del Dream Team, ejecuta el menú\\
    principal, solicita al usuario que ingrese una opción, la matchea y lanza\\
    el match anidado que ejecutará la opción seleccionada. El último 'case' del\\
    match principal queda reservado para la opción de 'exportar a csv'. Asimismo,\\
    la opción '0' detiene la iteración de todo lo anterior, es decir, sale de la\\
    aplicación.
    '''
    while True:
        opcion_seleccionada = menu_principal()
        match opcion_seleccionada:
            case "0":
                break
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" |\
                  "12" | "13" | "14" | "15" | "16" | "17" | "18" | "19" | "20" | "21" |\
                    "22" | "23" | "24":
                ejecutar_match_anidado(lista,opcion_seleccionada)
            case "25":
                exportar_csv(lista)
        continuar()


def ejecutar_match_anidado(lista:list,opcion:str,exportar:bool=False)->str:
    '''
    Parámetros: lista de diccionarios (necesaria), un entero tipo string 'opcion'\\
    (necesaria) y un booleano 'exportar' (opcional)
    Retorno: una lista de dos elementos tipo string
    Descripción: ejecuta todas las opciones del menú, excepto las opciones '0' y última\\
    que quedan reservadas para el match principal. Cada 'case' ejecutado genera dos
    strings: un nombre de archivo y uno de datos (string concatenado). Al finalizar\\
    la ejecución del 'case' ambos serán almacenados en una lista, en ese orden, para\\
    ser retornada. En caso que el string de datos termine la ejecución del 'case' como\\
    un string vacío todo lo anterior se omite y la lista retornada es vacía. El booleano\\
    opcional 'exportar' permite, en ciertos 'case', consultar al usuario si desea guardar\\
    los datos obtenidos como csv. Esto lo hace por defecto para dichos casos. Cuando\\
    su valor es 'True' bloquea todo lo anterior.
    '''
    lista_nombre_dato = []
    dato = "default_data"
    nombre_archivo = "default_name.csv"
    opcion_exportar = ""
    imprimir_con_formato = False
    tabular = False
    match opcion:
        case "1":
            ordenar_bubble_sort(lista,"list_dict_str","nombre")
            dato = mostrar_data_hasta_clave_rango(lista,"posicion")
            imprimir_con_formato = consultar_imprimir_con_formato()
            nombre_archivo = "nombre_posicion_all_dream_team.csv"
        case "2":
            i_r = seleccionar_indice_rango(lista,"i")
            if i_r != -1:
                dato = mostrar_estadisticas_por_indice_rango(lista,i_r,"i")
                imprimir_con_formato = consultar_imprimir_con_formato()
                nombre_archivo = "estadisticas_de_jugador_posicion_{0}_de_la_lista.csv".format(i_r)
                opcion_exportar = opcion
        case "3":
            patron_nombre = seleccionar_jugador_por_nombre()
            if patron_nombre != "":
                lista_jugador_logros = obtener_nombre_y_logros_x_jugador(lista,patron_nombre)
                if lista_jugador_logros != []:
                    dato = mostrar_data_hasta_clave_rango(lista_jugador_logros)
                    imprimir_con_formato = consultar_imprimir_con_formato()
                    nombre_archivo = "logros_de_jugador_{0}.csv".format(patron_nombre[:3])
        case "4":
            dato = mostrar_promedios_de_puntos_x_partido(lista)
            imprimir_con_formato = consultar_imprimir_con_formato()
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
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                            valor,
                                                                                            "promedio_puntos_por_partido",
                                                                                            True,
                                                                                            "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_puntos_por_partido_mayores_a_{0}.csv".format(re.sub("\.","_",str(valor)))
        case "10":
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "rebotes_totales",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_rebotes_totales_mayores_a_{0}.csv".format(valor)
        case "11":
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
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
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "porcentaje_tiros_libres",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_libres_mayor_a_{0}.csv".format(re.sub("\.","_",str(valor)))
        case "15":
            dato = mostrar_promedios_de_puntos_x_partido(lista,True)
            nombre_archivo = "promedio_puntos_por_partido_con_exclusion.csv"
            imprimir_con_formato = consultar_imprimir_con_formato()
        case "16":
            dato = mostrar_jugador_con_mayor_cant_logros(lista)
            nombre_archivo = "jugador_con_mayor_cant_logros.csv"
        case "17":
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
                lista_promedios = obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista,
                                                                                        valor,
                                                                                        "porcentaje_tiros_triples",
                                                                                        True,
                                                                                        "der")
                dato = mostrar_data_hasta_clave_rango(lista_promedios)
                nombre_archivo = "promedios_porcentaje_tiros_triples_mayor_a_{0}.csv".format(re.sub("\.","_",str(valor)))
        case "18":
            dato = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num","temporadas")
            nombre_archivo = "jugador_con_mayor_cant_temporadas_jugadas.csv"
        case "19":
            valor = ingresar_y_validar_porcentaje_promedio_cantidad()
            if valor != -1:
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
                                                                                        "list_dict_str")
                if lista_promedios != []:
                    dato = mostrar_data_hasta_clave_rango(lista_reordenada)
                    imprimir_con_formato = consultar_imprimir_con_formato()
                    nombre_archivo = "posiciones_A_Z_promedios_tiros_de_campo_mayor_a_{0}.csv".format(re.sub("\.","_",str(valor)))
        case "20":
            dato_tabulado = mostrar_jugadores_rankeados_con_tabulacion(lista)
            dato = mostrar_jugadores_rankeados_con_tabulacion(lista,False)
            nombre_archivo = "jugadores_rankeados.csv"
            imprimir_con_formato = True
            tabular = True
            opcion_exportar = opcion
        case "21":
            lista_cant_x_posicion = obtener_cant_jugadores_x_posición(lista)
            dato = mostrar_data_hasta_clave_rango(lista_cant_x_posicion)
            imprimir_con_formato = True
        case "22":
            lista_cant_logros_all_star = obtener_lista_x_cant_logros_all_star(lista)
            dato = mostrar_data_hasta_clave_rango(lista_cant_logros_all_star,"logros_All-Star")
            imprimir_con_formato = True
        case "23":
            dato = mostrar_mejores_jugadores_de_todas_las_estadisticas(lista)
        case "24":
            dato = mostrar_jugador_con_mejores_estadisiticas(lista)

    if dato != "":
        if imprimir_con_formato == False:
            if dato[0] == "\n": imprimir_dato(dato)
            else: imprimir_dato(f"\n{dato}")
        else:
            if tabular == False: imprimir_dato_con_formato(dato)
            else: imprimir_dato(f"\n{dato_tabulado}")
        lista_nombre_dato.append(nombre_archivo)
        lista_nombre_dato.append(dato)
    if exportar == False and (opcion_exportar == "2" or opcion_exportar == "20"):
        consultar_exportar_archivo(lista_nombre_dato)
    return lista_nombre_dato


def mostrar_jugador_con_mejores_estadisiticas(lista:list)->str:
    lista_claves_estadisticas = list(lista[0]["estadisticas"].keys())
    lista_all_rankings = obtener_todos_los_ranking_por_jugador(lista,lista_claves_estadisticas)
    for diccio in lista_all_rankings:
        promedio = calcular_promedio_todas_las_clave_valor(diccio)
        diccio["promedio_total_ranking"] = promedio
    ordenar_bubble_sort(lista_all_rankings,"list_dict_num","promedio_total_ranking")
    dato = "El jugador con mejor promedio de ranking en todas "\
           "las estadísticas es {0}, con {1:.2f}".format(lista_all_rankings[0]["nombre"],
                                                          lista_all_rankings[0]["promedio_total_ranking"])
    return dato


def calcular_promedio_todas_las_clave_valor(diccio:dict)->float:
    acumulador = 0
    contador_claves = 0
    for clave in diccio:
        if type(diccio[clave]) != str:
            acumulador += diccio[clave]
            contador_claves += 1
    promedio = acumulador / contador_claves
    return promedio


def mostrar_mejores_jugadores_de_todas_las_estadisticas(lista:list)->str:
    lista_claves_estadisticas = lista[0]["estadisticas"].keys()
    dato_total = ""
    for clave in lista_claves_estadisticas:
        dato_parcial = mostrar_mayor_menor_x_clave_estadistica(lista,"list_dict_num",clave)
        dato_total = "{0}\n{1}".format(dato_total,dato_parcial)
    return dato_total


def obtener_lista_x_cant_logros_all_star(lista:list)->list:
    lista_logros_all_team = obtener_nombre_y_logros_all_dream_team(lista)
    for i in range(len(lista_logros_all_team)):
        lista_logros = re.split(" - ",lista_logros_all_team[i]["logros"])
        for logro in lista_logros:
            if re.search(r"(All\-Star)",logro):
                lista_logros_all_team[i]["logros_All-Star"] = logro
                lista_logros_all_team[i].pop("logros")
    clave = "logros_All-Star"
    i = 0
    while i < len(lista_logros_all_team):
        if clave not in lista_logros_all_team[i]:
            lista_logros_all_team.pop(i)
        i += 1
    ordenar_bubble_sort(lista_logros_all_team,"list_dict_key_int","logros_All-Star",False)
    return lista_logros_all_team


def obtener_cant_jugadores_x_posición(lista:list)->list:
    lista_retorno = []
    diccio_retorno = {}
    for diccio in lista:
        clave = diccio["posicion"]
        if clave not in diccio_retorno:
            diccio_retorno[clave] = 1
        else:
            diccio_retorno[clave] += 1
    lista_retorno.append(diccio_retorno)
    return lista_retorno


def imprimir_dato_con_formato(string:str)->str:
    '''
    Parámetro: string concatenado (necesario)
    Retorno: string concatenado
    Descripción: recibe un string concatenado con saltos de línea cuya primera\\
    linea es el encabezado (también puede no serlo pero la función está preparada para\\
    salvar esa situación) y las demás, los datos en el mismo orden que en el encabezado\\
    (como filas de una tabla excel). Las lineas de datos a su vez, están concatenadas\\
    con comas. Reformatea el string y lo devuelve.
    '''
    lista_lineas = re.split("\n",string)
    lista_encabezado = re.split(",",lista_lineas[0])
    rango = range(1,len(lista_lineas))
    contador = 0
    while len(lista_encabezado) < 2:
        contador += 1
        lista_encabezado = re.split(",",lista_lineas[contador])
        rango = range(contador+1,len(lista_lineas))
    dato_retorno = generar_dato_formateado(lista_encabezado,lista_lineas,rango)
    imprimir_dato(dato_retorno)


def generar_dato_formateado(lista_headline:list,lista_lines:list,rango:int)->str:
    '''
    Parámetro: una lista 'headline' de strings (necesaria), una lista 'lines' de strings\\
    concatenados (necesaria), un iterable de índices 'rango' (necesario)
    Retorno: string concatenado
    Descripción: a partir del iterable 'rango' recorre ambas listas. Primero va generando una\\
    lista de datos por cada linea de datos. Luego, a cada string del encabezado le asigna su
    valor correspondiente en un nuevo string. Cada string tipo 'clave: valor', es concatenado\\
    con un separador. Al finalizar la asignación de valores almacena el string en una lista de\\
    datos formateados. Repite el proceso con cada linea, y al finalizar concatena todos los\\
    string de la lista de datos formateados con un salto de linea como separador. Por último,\\
    imprime el string resultante.
    '''
    dato = ""
    dato_retorno = ""
    lista_datos_formateados = []
    for i in rango:
        if dato == "": primer_index = i
        lista_datos = re.split(",",lista_lines[i])
        dato_formateado = ""
        for j in range(len(lista_datos)):
            if j == 0 and dato == "": dato = "\n{0}: {1}".format(lista_headline[j],lista_datos[j])
            else: dato = "{0}: {1}".format(lista_headline[j],lista_datos[j])
            if len(lista_headline) <= 3: separador = " -> "
            else: separador = "\n"
            if j != len(lista_datos) - 1: dato_formateado = "{0}{1}{2}".format(dato_formateado,dato,separador)
            else:
                if i != len(lista_lines) - 1: dato_formateado = "{0}{1}\n".format(dato_formateado,dato)
                else: dato_formateado = "{0}{1}".format(dato_formateado,dato)
        lista_datos_formateados.append(dato_formateado)
    dato_retorno = "".join(lista_datos_formateados[:])
    if primer_index != 1: dato_retorno = "\n{0}\n{1}".format("\n".join(lista_lines[:primer_index-1]),dato_retorno)
    return dato_retorno


def consultar_imprimir_con_formato()->bool:
    '''
    Parámetros: no requiere
    Retorno: un booleano
    Descripción: consulta al usuario por terminal si desea imprimir los datos obtenidos\\
    con un formato distinto al formato de guardado csv. En caso que el usuario\\
    acepte devuelve 'True' y si no, 'False'. En este último caso, también se imprime\\
    po terminal un aviso de opción omitida.
    '''
    consulta = input("Desea desea imprimir datos con formato? (S/N): ")
    flag_consulta = True
    if re.match("S$|s$",consulta):
        pass
    else:
        imprimir_dato("Se omitió impresión con formato")
        flag_consulta = False
    return flag_consulta


def obtener_lista_ordenada_x_key_estadistica_y_key_jugador(lista:list,
                                                           key_uno:str,
                                                           key_dos:str,
                                                           tipo_dato_uno:str,
                                                           tipo_dato_dos:str,
                                                           flag_uno:bool=True,
                                                           flag_dos:bool=True)->list:
    '''
    Parámetros: una lista de diccionarios donde cada diccionario, además de la clave\\
    'nombre', debe tener al menos una clave estadística y otra no estadística tipo string,\\
    float o int; dos string 'key', dos string 'tipo_dato' y dos booleanos 'flag' (todos\\
    paramétros necesarios excepto los 'flag' de ordenamiento)
    Retorno: la misma lista recibida pero reordenada
    Descripción: reordena la lista recibida, primero según de la clave estadística y luego\\
    según la clave no estadística. Los parámetros restantes determinan el tipo de dato a\\
    ordenar y el tipo de ordanamiento, ascendente ('True') o descendente ('False').
    '''
    ordenar_bubble_sort(lista,
                        tipo_dato_uno,
                        key_uno,
                        flag_uno)
    ordenar_bubble_sort(lista,
                        tipo_dato_dos,
                        key_dos,
                        flag_dos)
    return lista


def obtener_todos_los_ranking_por_jugador(lista:list,lista_claves:list)->list:
    '''
    Parámetros: una lista de diccionarios (necesaria)
    Retorno: una lista de diccionarios
    Descripción: primero obtiene una lista de diccionarios con el nombre del jugador y todas\\
    sus estadísticas. Luego itera la lista de claves estadísticas de interés para generar\\
    el ranking. Por cada clave iterada, ordena la lista de estadísticas según esta última,\\
    de manera descendente. A continuación recorre la lista reordenada. Utiliza un contador\\
    'ranking'. Dado que la lista esta reordenada de manera descendente, el primer jugador\\
    de la lista es el numero uno de este ranking como indica el contador. Guarda los nombres\\
    de todos los jugadores cada uno en un diccionario distinto, más la primer clave estadística\\
    con su respectivo valor de ranking. Todos estos diccionaros son appendeados a una lista\\
    retorno. Repite el proceso para las siguientes pasadas, pero para cada clave estadística\\
    recorre la lista retorno para hallar el jugador que está primero en el ranking en la clave\\
    actual y así siguiendo.
    '''
    lista_estadisticas = obtener_nombre_key_y_todas_las_estadisticas(lista)
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


def mostrar_jugadores_rankeados_con_tabulacion(lista:list,tabular:bool=True)->str:
    lista_claves_estadisticas = ["puntos_totales","rebotes_totales","asistencias_totales","robos_totales"]
    lista_jugadores_rankeados = obtener_todos_los_ranking_por_jugador(lista,lista_claves_estadisticas)
    if tabular == True:
        convertir_a_string_valores_de_claves(lista_jugadores_rankeados)
        tabular_jugadores_rankeados(lista_jugadores_rankeados)
    dato = mostrar_data_hasta_clave_rango(lista_jugadores_rankeados)
    if tabular == True: dato = tabular_encabezado_jugadores_rankeados(dato)
    return dato


def tabular_encabezado_jugadores_rankeados(string:str)->str:
    dato = ""
    lista_lineas = re.split("\n",string)
    lista_encabezados = re.split(",",lista_lineas[0])
    lista_primera_linea = re.split(",",lista_lineas[1])
    lista_headlines = []
    for i in range(len(lista_encabezados)):
        str_tab = ""
        while len(str_tab) <= len(lista_primera_linea[i])-1:
            if str_tab == "":
                if lista_encabezados[i] == "Nombre": str_tab = "{0}{1}".format(lista_encabezados[i]," ")
                else: str_tab = "{0}{1}".format(" ",lista_encabezados[i])
            else:
                if lista_encabezados[i] == "Nombre": str_tab = "{0}{1}".format(str_tab," ")
                else: str_tab = "{0}{1}".format(" ",str_tab)
        lista_headlines.append(str_tab)
    lista_lineas[0] = " ".join(lista_headlines[:])
    for i in range(1,len(lista_lineas)):
        lista_lineas[i] = re.sub(","," ",lista_lineas[i])
    dato = "\n".join(lista_lineas[:])
    return dato


def tabular_jugadores_rankeados(lista:list)->None:
    lista_copia = lista[:]
    lista_keys = lista[0].keys()
    for key in lista_keys:
        ordenar_bubble_sort(lista_copia,"list_dict_len_key",key)
        maximo_len = len(lista_copia[len(lista_copia)-1][key])
        if maximo_len < len(key): maximo_len = len(key)
        for diccio in lista:
            valor_tab = ""
            while len(valor_tab) <= maximo_len:
                if valor_tab == "":
                    if key == "nombre": valor_tab = "{0}{1}".format(diccio[key]," ")
                    else: valor_tab = "{0}{1}".format(" ",diccio[key])
                else:
                    if key == "nombre": valor_tab = "{0}{1}".format(valor_tab," ")
                    else: valor_tab = "{0}{1}".format(" ",valor_tab)
            diccio[key] = valor_tab

            
def convertir_a_string_valores_de_claves(lista:list)->None:
    for diccio in lista:
        for key in diccio:
            if type(diccio[key]) == int:
                diccio[key] = str(diccio[key])


def ingresar_y_validar_porcentaje_promedio_cantidad()->float:
    '''
    Parámetros: no requiere
    Retorno: un valor tipo float
    Descripción: solicita al usuario ingresar un valor mayor que 1 que puede ser int o float.\\
    Luego lo valido con regex. Si cumple la validación lo retorna castéandolo a float. Caso\\
    contrario, retornará -1 e imprimirá un aviso por terminal informando que el valor no\\
    es válido.
    '''
    valor = input("Ingrese un valor: ")
    if re.match(r"[1-9]$|[1-9]+\.[0-9][0-9]$|[1-9][0-9]+$|[1-9][0-9]+\.[0-9]{1}$|[1-9][0-9]+\.[0-9]{2}$|100",valor):
        valor = float(valor)
    else:
        imprimir_dato("Valor no válido. Inténtelo nuevamente")
        valor = float(-1)
    return valor


def obtener_jugadores_mayores_menores_a_valor_ingresado_x_key(lista:list,
                                                              valor:float,
                                                              key_estadistica:str,
                                                              ascdt:bool=True,
                                                              izq_o_der:str="der",
                                                              key:str=None)->list:
    '''
    Parámetros: una lista de diccionarios (necesario), un float 'valor' (necesario), un string\\
    'key_estadistica' (necesario), un booleano 'ascdt'(opcional), un string 'izq_o_der' (opcional)\\
    y otro string 'key' (opcional)
    Retorno: una lista de diccionarios
    Descripción: primero obtiene una lista con el nombre y una clave estadística de todos los jugadores.\\
    Como opción se puede agregar una clave no estadística más, 'key', aparte de 'nombre' y seguida\\
    de éste. Luego ordena la lista de estadísticas obtenida de acuerdo a su única clave estadísitica.\\
    Por defecto, lo hace de manera ascendente. Toma el 'valor' float recibido por parámetro como\\
    pivot y lo utiliza para encontrar los valores mayores o menores al mismo. Cuando finaliza obtiene\\
    una lista, que puede ser la lista de valores a la izquierda o a la derecha del pivot (menores o\\
    mayores respectivamente). Por defecto toma la lista de la derecha, que es lista que retorna. Si\\
    ocurre que el pivot recibido es mayor que el máximo valor de la clave estadística que hay en la\\
    lista, el proceso antes mencionado se interrumpe y avisa por terminal que el pivot es mayor a ese\\
    valor máximo. Entonces retornará una lista vacía.
    '''
    lista_retorno = []
    lista_estadisticas = obtener_estadistica_x_key_all_dream_team(lista,key_estadistica,key)
    ordenar_bubble_sort(lista_estadisticas,"list_dict_num",key_estadistica)
    maximo = lista_estadisticas[len(lista_estadisticas)-1][key_estadistica]
    if valor < maximo:
        lista_retorno = ordenar_quick_sort_reducida(lista_estadisticas,
                                                    valor,
                                                    key_estadistica,
                                                    ascdt,
                                                    izq_o_der)
    else:
        imprimir_dato("El valor ingresado supera el máximo {0}. Inténtelo nuevamente".format(maximo))
    return lista_retorno


def ordenar_quick_sort_reducida(lista:list,
                                valor:int,
                                key:str,
                                menor_a_mayor:bool=True,
                                izq_o_der:str="der")->list:
    '''
    Parámetros: una lista de diccionarios (necesaria), un entero 'valor' (necesaria),\\
    un string 'key' (necesario), un booleano 'menor_a_mayor' (opcional) y un string\\
    'izq_o_der' (opcional)
    Retorno: una lista de diccionarios
    Descripción: toma al 'valor' como pivot y appendea en la 'lista_derecha' todos los diccionarios\\
    cuyos valores en la clave 'key' son mayores al pivot, si el booleano 'menor_a_mayor' es 'True',\\
    y en 'la lista_izquierda' los que son menores al pivot. Si 'menor_a_mayor' es 'False', los mayores\\
    al pivot quedarán en la 'lista_izquierda' y los menores en la 'lista_derecha'. La lista a retonar\\
    va a ser la 'lista_izquierda' o la 'lista_derecha' de acuerdo a lo indicado por parámetro 'izq_o_der'\\
    ('izq' o 'der' respectivemente). Por defecto, ordenará de manera ascendete y retornará la lista\\
    derecha (o sea, todos los diccionarios con valores por clave que son mayores al pivot).
    '''
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
    '''
    Parámetros: una lista de diccionarios
    Retorno: un string concatenado
    Descripción: ordena la lista recibida por cantidad de logros de cada jugador,\\
    de manera ascendente. Guarda el último índice de la lista ordenada (o sea,\\
    la posición del jugador con más logros obtenidos) y con éste genera el string\\
    concatenado a retornar.
    '''
    lista_ordenada_x_cant_logros = ordenar_x_cantidad_de_logros(lista)
    ultimo_indice = len(lista_ordenada_x_cant_logros) - 1
    dato = "El jugador con MAYOR cantidad de logros es: {0}, con {1} logros\n{2}".format(
        lista_ordenada_x_cant_logros[ultimo_indice]["nombre"],
        len(lista_ordenada_x_cant_logros[ultimo_indice]["logros"]),
        "\n".join(lista_ordenada_x_cant_logros[ultimo_indice]["logros"][:]))
    return dato


def ordenar_x_cantidad_de_logros(lista:list)->list:
    '''
    Parámetros: una lista de diccionarios (necesaria)
    Retorno: una lista de diccionarios
    Descripción: ordena la lista recibida por párametro de manera ascendente según la\\
    clave 'logros' (lo hace, calculando la longitud de las listas-valor dentro de\\
    la clave 'logros' de cada jugador) y la retorna.
    '''
    lista_copia = lista[:]
    ordenar_bubble_sort(lista_copia,"list_dict_len_key","logros")
    return lista_copia


def mostrar_mayor_menor_x_clave_estadistica(lista:list,
                                            tipo_dato:str,
                                            key:str,
                                            max_min:str="mayor")->str:
    '''
    Parámetros: lista de diccionarios
    Retorno: un string informativo de una sola linea
    Descripción: de la lista de jugadores, obtiene una nueva lista solo con los nombres\\
    de cada jugador y todas sus claves estadísticas. Luego ordena esta última de\\
    manera ascendente de acuerdo a la 'key' estadística pasada por parámetro. El\\
    string 'tipo_dato' indica el tipo de dato a ser evaluado, en este caso, un valor\\
    numérico correspondiente a una clave estadística de un jugador-diccionario\\
    dentro de una lista ('list_dict_num'). Por último, por medio del parámetro string\\
    'max_min', selecciona al jugador con valor máximo ('mayor') de la 'key', o bien,\\
    al jugador con el valor mínimo ('menor') de la misma. Con los datos del jugador\\
    encontrado genera el string informativo a ser retornado.
    '''
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
    '''
    Parámetros: lista de diccionarios (necesaria) y un string 'key' (opcional)
    Retorno: una lista de diccionarios
    Descripción: toma la lista de jugadores, la itera y extrae de cada jugador su\\
    nombre y todas sus claves estadísticas, las guarda en un nuevo diccionario\\
    y lo appendea a la lista que será retornada. Como opción, puede incluir en\\
    cada jugador, una clave no estadística más 'key', aparte de 'nombre'.
    '''
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
    '''
    Parámetros: una lista de diccionarios (necesaria), un string 'key_estadistica'\\
    y otro string 'key' (opcional)
    Retorno: una lista de diccionarios
    Descripción: obtiene una lista de jugadores con todas sus claves estadísticas.\\
    Extrae de la misma, solo el nombre y la 'key_estadistica' pasada por parámetro.\\
    Con éstas crea un nuevo diccionario y lo appendea a la lista que será retornada.\\
    Repite este proceso por iteración de la lista obtenida al comienzo. Como opción,\\
    puede incluir en cada jugador, una clave no estadística más 'key', aparte de\\
    'nombre'.
    '''
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
    '''
    Parámetros: una lista de diccionarios (necesaria) y un booleano 'exclusion' (opcional)
    Retorno: un string informativo de una linea
    Descripción: primero obtiene una nueva lista de jugadores con solo dos claves en cada uno:\\
    'nombre' y 'promedio_puntos_por_partido'. Luego ordena dicha lista de manera ascendente.\\
    Seguidamente puede excluir (o no) al jugador con el valor mínimo de la lista, de la clave\\
    en cuestión. Reordena la lista por nombre, calcula el promedio y genera la linea a retornar.
    '''
    lista_promedios_de_puntos_x_partido = obtener_estadistica_x_key_all_dream_team(lista,"promedio_puntos_por_partido")
    dato = ""
    dato_excluido = ""
    ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,
                            "list_dict_num",
                            "promedio_puntos_por_partido")
    if exclusion == True:
        diccio_excluido = lista_promedios_de_puntos_x_partido[0]
        lista_promedios_de_puntos_x_partido.pop(0)
        dato_excluido = "Excluido: {0} -> Promedio puntos por partido: {1}\n".format(diccio_excluido["nombre"],
                                                                                     diccio_excluido["promedio_puntos_por_partido"])
    ordenar_bubble_sort(lista_promedios_de_puntos_x_partido,
                        "list_dict_str",
                        "nombre")
    promedio_total = calcular_promedio(lista_promedios_de_puntos_x_partido,"promedio_puntos_por_partido")
    dato = mostrar_data_hasta_clave_rango(lista_promedios_de_puntos_x_partido)
    dato = "{0}Promedio total de puntos por partido de todo el Dream Team: {1:.2f}\n{2}".format(dato_excluido,promedio_total,dato)
    return dato


def calcular_promedio(lista:list,key:str)->float:
    '''
    Parámetros: lista de diccionarios (necesaria) y un string 'key' (necesario)
    Retorno: un valor tipo float
    Descripción: recorre la lista de diccionarios y calcula el promedio de los valores\\
    de una de las claves de cada diccionario. En caso de no existir dicha clave dentro\\
    del diccionario, la omitirá en el denominador del promedio. En caso de que la clave\\
    no se encuentre en ningún diccionario, retornará -1.
    '''
    contador = 0
    acumulador = 0
    for diccio in lista:
        if key in diccio and (type(diccio[key]) == int or type(diccio[key]) == float):
            acumulador += diccio[key]
            contador += 1
    if contador > 0: promedio = acumulador / contador
    else: promedio = -1
    return promedio


def ordenar_bubble_sort(lista:list,
                        tipo_dato:str,
                        key:str=None,
                        flag_orden:bool=True)->None:
    '''
    Parámetros: una lista de diccionarios (necesaria), un string 'tipo_dato' (necesario),\\
    un string 'key' (necesario) y un booleano 'flag_orden' (opcional)
    Retorno: no tiene
    Descripción: ordena la lista recibida de acuerdo a un criterio de swap (intercambio) de\\
    elementos. El string 'tipo_dato' debe ser representativo de tipo de valor a comparar\\
    en el ordenamiento. El string 'key' es opcional ya que la lista podría ser o no de\\
    diccionarios, es decir, podría requerir o no un clave a partir de la cual la lista\\
    necesite ser ordenada la lista. El booleano 'flag_orden' es por defecto 'True', o sea\\
    que por defecto va a ordenar de manera ascendente (o menor a mayor), salvo que\\
    se indique lo contrario asignándole 'False'.
    '''
    rango = len(lista) 
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango -= 1
        for i in range(rango):
            if  flag_orden == False and\
                retornar_tipo_dato(lista,tipo_dato,i,key) <\
                retornar_tipo_dato(lista,tipo_dato,i+1,key) \
             or flag_orden == True and\
                retornar_tipo_dato(lista,tipo_dato,i,key) >\
                retornar_tipo_dato(lista,tipo_dato,i+1,key):
                lista[i],lista[i+1] = lista[i+1],lista[i]
                flag_swap = True


def retornar_tipo_dato(lista:list,
                       tipo_dato:str,
                       i:int,
                       key:str=None)->None:
    '''
    Parámetros: una lista (necesaria), un string 'tipo_dato' (necesario), un valor\\
    entero tipo entero (necesario) y un string 'key'(opcional)
    Retorno: un valor que puede ser string, int o float
    Descripción: define la sintaxis del valor a ser retornado de acuerdo al parámetro\\
    'tipo_dato'. Por ejemplo: 'list_dict_str' expresa una lista de diccionarios, donde\\
    el valor de la clave del diccionario es un string. Esta función puede ser usada en\\
    iteraciones de 'for' en virtud del parámetro 'i' (índice de la lista). El parámetro\\
    'key' solo será necesario para recorrer una determinada clave de los diccionarios\\
    de una lista de diccionarios.
    '''
    if tipo_dato == "list_dict_str": dato = lista[i][key][0]
    elif tipo_dato == "list_dict_num": dato = lista[i][key]
    elif tipo_dato == "list_dict_len_key": dato = len(lista[i][key])
    elif tipo_dato == "list_dict_key_int": dato = int(lista[i][key][0:2])
    return dato


def consultar_exportar_archivo(lista:list)->None:
    '''
    Parámetros: una lista de dos strings (necesaria)
    Retorno: no tiene
    Descripción: consulta al usuario si desea guardar ciertos datos generados en un archivo\\
    csv. En caso afirmativo le pasa a la función 'guardar_archivo' el string de nombre\\
    de archivo y el string concatenado de datos recibidos por la lista, en ese orden.\\
    En caso negativo, imprime por terminal que se omitió la creación del archivo.
    '''
    consulta = input("\nDesea exportar los resultados a .csv? (S/N): ")
    if re.match("S$|s$",consulta):
        guardar_archivo(lista[0],lista[1])
    else:
        imprimir_dato("Se omitió creación de archivo")


def mostrar_jugador_salon_de_la_fama(lista:list,pattern:str)->str:
    '''
    Parámetros: una lista de diccionarios y un patrón tipo string (ambos necesarios)
    Retorno: un string concatenado
    Descripción: a partir del 'pattern' obtiene una lista de jugadores cuyos nombres matchearon\\
    con éste. Luego evalúa si el valor-string de la clave 'logros' tiene como substring al\\
    patrón 'Salon de la Fama', escrito con mayúscula y también con minúscula. Ya sea que el\\
    patrón 'Salon de la Fama' coincida o no, genera un string con el aviso de pertenencia o\\
    no pertenencia del jugador al Salón de la Fama y lo retorna. En caso de que ningún nombre\\
    de los jugadores matchee con el patrón recibido, retornará el dato como string vacío.
    '''
    dato = ""
    lista_logros_jugador = obtener_nombre_y_logros_x_jugador(lista,pattern)
    if lista_logros_jugador != []:
        patron = "Salon de la Fama"
        flag_pertenece = False
        for diccio in lista_logros_jugador:
            if re.search(r"{0}|{1}".format(patron,patron.lower()),diccio["logros"]):
                flag_pertenece = True
            if flag_pertenece == True: substring = "es"
            else: substring = "NO es"
            if dato == "": separador = dato
            else: separador = "\n"
            dato = "{0}{1}{2} {3} Miembro del {4} del Baloncesto".format(dato,separador,diccio["nombre"],substring,patron)
    return dato


def obtener_nombre_y_logros_x_jugador(lista:list,pattern:str)->list:
    '''
    Parámetros: una lista de diccionarios y un patrón tipo string (ambos necesarios)
    Retorno: una lista de diccionarios
    Descripción: recibe la lista de jugadores, crea una nueva lista sólo con las claves\\
    'nombre' y 'logros'. Luego evalúa por medio del 'pattern' recibido si el nombre\\
    de algún jugador coincide con el mismo. Si ocurre algún match dicho jugador se\\
    appendea a una nueva lista y se retorna. Caso contrario, retorna una lista vacía\\
    e imprime por terminal que no se encontraron coincidencias.
    '''
    lista_nombre_logros = obtener_nombre_y_logros_all_dream_team(lista)
    lista_retorno = []
    for diccio in lista_nombre_logros:
        if re.findall(r"{0}".format(pattern),diccio["nombre"]) or\
            re.findall(r"{0}".format(pattern),diccio["nombre"].lower()):
            lista_retorno.append(diccio)
    if lista_retorno == []:
        imprimir_dato("No se encontraron coincidencias. Inténtelo nuevamente")
    return lista_retorno


def obtener_nombre_y_logros_all_dream_team(lista:list)->list:
    '''
    Parámetros: una lista de diccionarios (necesario)
    Retorno: una lista de diccionarios
    Descripción: recibe la lista de jugadores, la itera y toma de cada jugador los valores\\
    de las claves 'nombre' y 'logros' para asigárselos a las mismas claves pero en un\\
    nuevo diccionario. Al valor-lista de la clave 'logros' antes de incluirlo en el nuevo\\
    diccionario lo convierte en un string concatenado con el separador ' - '. Al nuevo\\
    diccionario con estas dos únicas claves lo appendea a una lista, y al finalizar la\\
    iteración la retorna
    '''
    lista_retorno = []
    for i in range(len(lista)):
        diccio_nombre_logros = {}
        diccio_nombre_logros["nombre"] = lista[i]["nombre"]
        diccio_nombre_logros["logros"] = " - ".join(lista[i]["logros"][:])
        lista_retorno.append(diccio_nombre_logros)
    return lista_retorno


def seleccionar_jugador_por_nombre()->str:
    '''
    Parámetros: no requiere
    Retorno: un string
    Descripción: solicita al usuario ingresar el nombre de un jugador,\\
    y lo valida así: al menos 3 caracteres alfabéticos en minúscula o\\
    mayúscula. Si resulta válido lo retorna. En caso contrario imprime\\
    un aviso de error por terminal y devuelve un string vacío.
    '''
    nombre = input("Ingrese el nombre del jugador: ")
    patron = ""
    if re.match(r"^[A-Za-z]{3}",nombre):
        patron = nombre
    else:
        imprimir_dato("Nombre inválido. Inténtelo nuevamente")
    return patron


def seleccionar_indice_rango(lista:list,tipo:str)->int:
    '''
    Parámetros: una lista de diccionarios y un string (ambos necesarios)
    Retorno: un número entero
    Descripción: solicita al usuario ingresar un número dentro de un\\
    intervalo predefinido, lo valida con regex, lo convierte a entero\\
    y lo retorna. Si el número ingresado no es válido retornará un - 1\\
    (tipo entero). El parámetro 'tipo' cambia el formato de la oración\\
    con la que se solicita el ingreso del número.
    '''
    if tipo == "r": subtring = "hasta el"
    elif tipo == "i": subtring = "del"
    indice_rango = input("Mostrar estadísticas {0} jugador número (1-{1}): ".format(subtring,len(lista)))
    if re.match("[1-9]$|1[0-9]$",indice_rango) and int(indice_rango) <= len(lista):
        indice_rango = int(indice_rango)
    else:
        indice_rango = -1
        imprimir_dato("Número inválido. Inténtelo nuevamente\n")
    return indice_rango


def mostrar_estadisticas_por_indice_rango(lista:list,index_range:int=None,tipo:str=None)->str:
    '''
    Parámetros: una lista de diccionarios (necesaria), un entero (opcional) y un string\\
    (opcional)
    Retorno: un string concatenado con saltos de linea
    Descripción: a partir de la lista de jugadores del Dream Team, crea una nueva lista
    de jugadores (diccionarios) cuyas claves serán: el nombre del jugador más todas\\
    sus estadísticas (son todas las claves del diccionario de estadísticas dentro del\\
    diccionario/jugador). Luego esta nueva lista se puede recortar de acuerdo a los\\
    parámetros 'index_range' y 'tipo'. Con 'tipo' se indica si el 'index_range' es un\\
    índice ('i') o un rango ('r'), e 'index_range' será el número que actuará de índice\\
    o rango (primer jugador hasta la posición indicada inclusive) según el caso. Por\\
    último vuelca la información de la lista ya filtrada (o no) en un string concatenado\\
    y lo retorna.
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
    Parámetros: una lista (necesaria) con dos elementos string:\\
    nombre del archivo y el dato a archivar, en ese orden
    Retorno: no tiene
    Descripción: solicita al usuario ingresar un número dentro de un\\
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
    Descripción: solicita al usuario ingresar un número dentro de\\
    un intervalo predefinido, lo valida y lo devuelve. En caso\\
    de ingresar un 'número' no admitido, imprime un aviso por\\
    terminal y devuelve el string '-1'
    '''
    opcion = input("Seleccione opción a guardar (1-24): ")
    if re.match(r"[0-9]$|1[0-9]$|2[0-4]$",opcion):
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
    Descripción: lee la información del archivo json para luego cargarla en\\
    formato de lista de diccionarios
    '''
    lista_retorno = []
    with open(path_name_file,"r",encoding="utf-8") as file:
        diccio_datos = json.load(file)
        lista_retorno = diccio_datos[clave]
    return lista_retorno


def guardar_archivo(name_file:str,new_data:str)->bool:
    '''
    Parámetros: nombre de archivo (necesario), datos a escribir (necesario)
    Retorno: booleano 'True' si el archivo se creó correctamente, y en caso\\
    contrario devuelve 'False'
    Descripción: crea un archivo con la extensión indicada en 'name_file' cuyo\\
    contenido será la información almacenada en 'new_data'. El modo de\\
    escritura es 'w+'.
    '''
    with open(name_file,"w+",encoding="utf-8") as file:
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
    Retorno: string concatenado
    Descripción: recibe la lista, genera un encabezado con todas las claves del primer\\
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
    Retorno: string de valores de claves de una sola linea
    Descripción: recibe la lista y la posición de uno de sus diccionarios. Luego\\
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
    Retorno: string de claves de una sola linea
    Descripción: recibe la lista, toma todas las claves del primer diccionario y las\\
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