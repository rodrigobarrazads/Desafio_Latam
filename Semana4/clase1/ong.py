'''
Descripción
La empresa de desarrollo de software DESARROLLA se encuentra actualmente trabajando
en muchos proyectos distintos. Es tanta la demanda que te solicita trabajar en 3 soluciones
que tienen pendientes. Para ello, te entregarán los requerimientos de cada tarea y deberás
implementar una función que entregue la solución a cada problema.

Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda
escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos
operaciones conocidas como el factorial y la productoria y se requiere que usted prepare
una script que implemente esto.

Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. 
'''
#Definimos el Lactorial
def factorial(numero):
    fact = 1  #Inicializamos el factorial el 1
    for i in range(numero):  #Iteramos para cada numero anterior al numero entregrado
        fact *= i+1   #Calculamos el factorial multiplicando el resultado anterior con el presente
    print(f'El factorial de {numero} es {fact}') #Imprimo resultado

#Definimos la Productoria
def pitatoria(lista):
    pita = 1  #Inicializamos la productoria en 1
    for num in lista:  #Iteramos sobre los elementos de la lista
        pita *= num   #Calculamos el producto entre los elementos de la lista
    print(f'La productoria de {lista} es {pita}') #Imprimo resultado

#Definimos el control del calculo
def calcular(**tipo_calculo):
    for k,v in tipo_calculo.items():  #Iteramos sobre cada item de los valores entregados por el kwargs
        if 'fact' in k:  #Si la llave posee el nombre fact, ocupamos el factorial
            factorial(v)
        elif 'prod' in k: #Si la llave posee el nombre prod, ocupamos la productoria
            pitatoria(v)
        else: pass

#Llamamos a la funcion para hacer los calculos
print('-'*80)
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
print('-'*80)