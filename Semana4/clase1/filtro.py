'''
Descripción
La empresa de desarrollo de software DESARROLLA se encuentra actualmente trabajando
en muchos proyectos distintos. Es tanta la demanda que te solicita trabajar en 3 soluciones
que tienen pendientes. Para ello, te entregarán los requerimientos de cada tarea y deberás
implementar una función que entregue la solución a cada problema.

Filtrado Relevante
La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
problema. Dada una muestra de los productos que actualmente se encuentran disponibles
en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función debe permitir mostrar los valores mayor que o menor que un umbral
  (siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a
  menos que se indique lo contrario.
'''
#Importamos las librerias necesarias
import sys

#Defino el filtro para productos mayores al umbral
def filtro_mayor(diccionario, umbral):
    resultado = ', '.join([k for k,v in diccionario.items() if v > umbral]) #Obtengo clave del diccionario que cumple condicion de mayor
    return print(f'Los productos mayores al umbral son: {resultado}') #Muestro el resultado del filtro

#Defino el filtro para productos menores al umbral
def filtro_menor(diccionario, umbral):
    resultado = ', '.join([k for k,v in diccionario.items() if v < umbral]) #Obtengo clave del diccionario que cumple condicion de menor
    return print(f'Los productos menores al umbral son: {resultado}') #Muestro el resultado del filtro

#Funcion para calcular umbral considerando con o sin operador >, < o distinto
def filtro_relevante(diccionario, umbral, tipo_filtro = None):
    if tipo_filtro is None or tipo_filtro == 'mayor':  #Si no especificar la operacion o si la operacion especificada es igual a mayor, llamo a funcion correspondiente
        filtro_mayor(diccionario, umbral)
    elif tipo_filtro == 'menor':     #Si la operacion especificada es igual a menor, llamo a funcion correspondiente
        filtro_menor(diccionario, umbral)
    else: print('Lo sentimos, no es una operación válida') #Muestro la operacion invalida

#Se define diccionario
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

valor_umbral = int(sys.argv[1]) #Guardamos el valor del umbral introducido
contiene_signo = len(sys.argv) #Obtenemos el largo para saber si se especifico o no el signo
print('-'*100)
if contiene_signo == 2:   #Ejecutamos la funcion considerando solo el umbral
    filtro_relevante(precios, valor_umbral)
elif contiene_signo == 3:  #Ejecutamos la funcion considerando el umbral y el operador escrito
    filtro_relevante(precios, valor_umbral, sys.argv[2])
else: pass  #En otro caso, no se hace nada.
print('-'*100)