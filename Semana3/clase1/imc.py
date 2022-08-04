'''
Descripción
El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:

                                𝐼𝑀𝐶 = 𝑊/𝐻^2

W : corresponde al peso de la persona en Kg.
H: corresponde a la altura en metros.
IMC: EL valor del IMC, en [Kg/m2]

Requerimientos
Se solicita crear el programa imc.py que permita calcular el IMC de una persona.
1. Al programa se debe ingresar el peso en Kg y la talla (altura) en centímetros.
2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la
   fórmula. El resultado se debe informar con 2 decimales.
3. Entregar al usuario una salida acorde que permita conocer el valor de su IMC
   además de la clasificación dada por la OMS.
'''
#Importamos las librerias necesarios
import sys

peso = int(sys.argv[1]) #Guardamos el peso en Kg
altura = int(sys.argv[2])/100 #Guardamos la altura en metros al dividirla por 100

imc = peso / altura**2 #Calculamos el IMC
print('-'*60)
print(f'Su IMC es {imc:.2f}') #Imprimimos el valor del IMC segun datos entregados

# Definimos su clasificacion OMS
if imc < 18.5:
   print('La clasificación OMS es Bajo Peso')
elif imc >= 18.5 and imc < 25:
   print('La clasificación OMS es Adecuado')
elif imc >= 25 and imc < 30:
   print('La clasificación OMS es Sobrepeso')
elif imc >= 30 and imc < 35:
   print('La clasificación OMS es Obesidad Grado I')
elif imc >= 35 and imc < 40:
   print('La clasificación OMS es Obesidad Grado II')
else: print('La clasificación OMS es Obesidad Grado III')
print('-'*60)