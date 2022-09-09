'''
Descripción
La empresa de desarrollo de software DESARROLLA se encuentra actualmente trabajando
en muchos proyectos distintos. Es tanta la demanda que te solicita trabajar en 3 soluciones
que tienen pendientes. Para ello, te entregarán los requerimientos de cada tarea y deberás
implementar una función que entregue la solución a cada problema.

se debe medir mediante telemetría las velocidades de cada una de sus correas
transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que,
para poder entregar energía a las correas más lentas, es necesario ralentizar las más
rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se
requiere levantar una alerta de la posición de las correas transportadoras que están por
sobre el promedio
'''
#Definimos funcion que calcula la posicion del numero mayor al promedio
def posicion_sobre_media(lista):
    promedio = sum(lista)/len(lista)  #Obtenemos el promedio de la lista
    resultado = [pos for pos, num in enumerate(lista) if num > promedio] #Para cada valor, guardo solo aquellos que sean mayores que el promedio
    return print(resultado) #Imprimo resultado

#Defino la lista con las velocidades
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#Llamo a la funcion para obtener resultado
print('-'*120)
posicion_sobre_media(velocidad)
print('-'*120)