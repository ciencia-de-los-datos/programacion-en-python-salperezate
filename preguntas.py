"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
# Leamos el archivo de manera global

df = open('data.csv', 'r').readlines()
df = [z.replace('\n', '') for z in df]
df = [line.split('\t') for line in df]

def pregunta_01():
    suma_columna = 0

    for line in df:
        suma_columna = suma_columna + float(line[1])

    return suma_columna

pregunta_01()



from collections import Counter

def pregunta_02():
    contador_letras = Counter([line[0] for line in df])
    return sorted(contador_letras.items())

pregunta_02()


def pregunta_03():
    contador_valor_letras = {}
    for letra, valor in map(lambda line: (line[0], float(line[1])), df):
        contador_valor_letras[letra] = contador_valor_letras.get(letra, 0) + valor
    return sorted(contador_valor_letras.items())

pregunta_03()



def pregunta_04():
    contador_meses = Counter([line[2].split('-')[1] for line in df])
    return sorted(contador_meses.items())


def pregunta_05():
    contador_valor_letras = {}
    for letra, valor in map(lambda line: (line[0], float(line[1])), df):
        contador_valor_letras[letra] = contador_valor_letras.get(letra, []) + [valor]
        lista_tuplas = [(letra, max(valores), min(valores)) for letra, valores in contador_valor_letras.items()]
    return sorted(lista_tuplas)


def pregunta_06():
    valores = {}
    valores_min = {}
    valores_max = {}

    for row in df:
        diccionario = dict(item.split(':') for item in row[4].split(','))
        for clave, valor in diccionario.items():
            valor = int(valor)
            if clave in valores:
                valores[clave].append(valor)
            else:
                valores[clave] = [valor]

    for clave, lista_valores in valores.items():
        valores_min[clave] = min(lista_valores)
        valores_max[clave] = max(lista_valores)

    lista_tuplas = [(clave,valores_min[clave], valores_max[clave]) for clave in valores.keys()]
    return sorted(lista_tuplas)

pregunta_06()


def pregunta_07():
    valores = {}
    for row in df:
        letra = row[0]
        valor = float(row[1])
        if valor in valores:
            valores[valor].append(letra)
        else:
            valores[valor] = [letra]
 
    return sorted(valores.items())


def pregunta_08():
    valores = {}
    for row in df:
        letra = row[0]
        valor = float(row[1])
        if valor in valores:
            valores[valor].append(letra)
        else:
            valores[valor] = [letra]
    lista_tuplas = [(valor, sorted(list(set(valores[valor])))) for valor in valores.keys()]
    return sorted(lista_tuplas)

def pregunta_09():

    valores = {}
    for row in df:
        diccionario = dict(item.split(':') for item in row[4].split(','))
        for clave in diccionario.keys():
            if clave in valores:
                valores[clave] += 1
            else:
                valores[clave] = 1
    return dict(sorted(valores.items()))



def pregunta_10():

    lista = [(fila[0], len(fila[3].split(',')), len(fila[4].split(','))) for fila in df]

    return lista


def pregunta_11():
    suma_por_letra = {}

    for fila in df:
        numero = fila[1]
        elementos = fila[3].split(',')
        for elemento in elementos:
            letra = elemento.split(',')[0]
            if letra in suma_por_letra:
                suma_por_letra[letra] += float(numero)
            else:
                suma_por_letra[letra] = float(numero)

            
    return dict(sorted(suma_por_letra.items()))

pregunta_11()


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
