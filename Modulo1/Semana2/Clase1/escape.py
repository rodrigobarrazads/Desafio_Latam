'''
Descripción
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un 
planeta venciendo la gravedad. 

La velocidad de escape se calcula mediante la siguiente fórmula:        

                            𝑉𝑒 = raiz(2𝑔𝑟)

𝑉𝑒: corresponde a la Velocidad de Escape en [m/s].
𝑔: corresponde a la constante gravitacional en [m/s2].
𝑟: Corresponde al radio del planeta en [m].

Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
'''
#importa la libreria necesaria para ocupar la raiz
from math import sqrt

#Se solicita al usuario ingresar los valores requeridos
print('Para calcular la velocidad de escape del planeta X, ingrese los siguientes valores solicitados: ')
print('''ADVERTENCIA: Los datos ingresados deben ser solo números, y ademas en la unidad de medida solicitada,
de lo contrario, el cálculo será invalido o no será correcto.''')
print('-'*60)

#Ingreso de valores
radio_kilometros = int(input('Ingrese el radio del planeta X en Kilómetros: '))
constante_g = float(input('Ingrese la constante g en [m/s^2]: '))

#Se pasa el radio del planeta de kilometros a metros
radio_metros = radio_kilometros * 1000

#Calculo la velocidad de escape
velocidad_escape = sqrt(2 * radio_metros * constante_g)

#Muestro el resultado en pantalla
print('-'*60)
print(f'La velocidad de Escape del planeta X es de {velocidad_escape:.1f}[m/s] ')