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
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior, todo esto mediante input(). El programa debe calcular las
utilidades actuales y mostrar la razón entre las utilidades actuales y las del año
anterior con dos decimales.
'''

#Se solicita al usuario ingresar los valores requeridos, adviertiendole el tipo de dato que debe ingresar
print('Para calcular las utilidades del proyecto, ingrese los siguientes valores solicitados: ')
print('ADVERTENCIA: Los datos ingresados deben ser solo números, de lo contrario, el cálculo será invalido.')
print('-'*60)

#Ingreso de valores
precio_suscripcion = int(input('Precio de Suscripcion: $'))
numero_usuarios = int(input('Número de Usuarios: '))
gastos_totales = int(input('Gastos Totales: $'))
utilidades_anterior = int(input('Utilidades del Año Anterior: $'))

#Se calcula las utilidades (año actual) segun los datos solicitados
utilidades_actual = precio_suscripcion * numero_usuarios - gastos_totales

#Se obtiene la razon entre las utilidades actuales y las del año anterior
razon_utilidades = utilidades_actual/utilidades_anterior

#Se imprime el valor obtenido del calculo
print('-'*60)
print(f'Las utilidades actuales del proyecto son: ${utilidades_actual}')
print(f'La razon entre las utilidades actuales versus las del año anterior es: {razon_utilidades:.2f}')