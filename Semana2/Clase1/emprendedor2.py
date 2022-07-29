'''
Descripción
Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
del proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

Se pide:
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
'''

#Se solicita al usuario ingresar los valores requeridos, adviertiendole el tipo de dato que debe ingresar
print('Para calcular las utilidades del proyecto, ingrese los siguientes valores solicitados: ')
print('ADVERTENCIA: Los datos ingresados deben ser solo números, de lo contrario, el cálculo será invalido.')
print('-'*60)

#Ingreso de valores
precio_suscripcion = int(input('Precio de Suscripcion: $'))
usuarios_normales = int(input('Número de Usuarios Normales: '))
usuarios_premium = int(input('Número de Usuarios Premium: '))
gastos_totales = int(input('Gastos Totales: $'))

#Se calcula las utilidades segun los datos solicitados, considerando el precio de suscripcion mayor para 
#los usuarios premium (1.5P)
utilidades = precio_suscripcion * (usuarios_normales + 1.5 * usuarios_premium) - gastos_totales

#Se imprime el valor obtenido del calculo
print('-'*60)
print(f'Las utilidades del proyecto son: ${utilidades:.0f}')