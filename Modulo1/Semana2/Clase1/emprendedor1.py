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
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
'''

#Se solicita al usuario ingresar los valores requeridos, adviertiendole el tipo de dato que debe ingresar
print('Para calcular las utilidades del proyecto, ingrese los siguientes valores solicitados: ')
print('ADVERTENCIA: Los datos ingresados deben ser solo números, de lo contrario, el cálculo será invalido.')
print('-'*60)

#Ingreso de valores
precio_suscripcion = int(input('Precio de Suscripcion: $'))
numero_usuarios = int(input('Número de Usuarios: '))
gastos_totales = int(input('Gastos Totales: $'))

#Se calcula las utilidades segun los datos solicitados
utilidades = precio_suscripcion * numero_usuarios - gastos_totales

#Se imprime el valor obtenido del calculo
print('-'*60)
print(f'Las utilidades del proyecto son: ${utilidades}')