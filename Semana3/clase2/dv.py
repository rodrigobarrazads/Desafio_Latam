'''
Módulo 11
Módulo 11 es un algoritmo con el cual se calcula el dígito verificador (o DV, es el número que
va después del guión), para los RUT en chile. Este número evita que cualquier persona pueda
inventar un RUT aleatoriamente.

Se pide crear un programa en Python llamado dv.py que permita ingresar el número de RUT
sin puntos ni DV y devuelva el DV correspondiente.
'''

print('-'*60)
rut = input("Ingresa tu RUT sin puntos ni dígito verificador: ") #Solicitamos rut del usuario
serie_numerica = '23456723' #Iniciamos el multiplicador como un string para acceder a el
suma = 0 #Inicializamos la suma de cada multiplicacion en 0
rut_invertido = rut[::-1] #Invertimos el rut para poder iterar

# Empezamos la iteracion
for pos, digito in enumerate(rut_invertido):
    suma += int(digito) * int(serie_numerica[pos]) #Se hace el calculo y se suma al calculo anterior

dv = 11 - (suma % 11) #Obtenemos digito verificador obteniendo el modulo 11 y restando 11 por dicho modulo

#Aplicamos Regla de digito verificador
if dv == 10:
    print(f'Su dígito verificador es K')
elif dv == 11:
    print(f'Su dígito verificador es 0')
else: print(f'Su dígito verificador es {dv}')
print('-'*60)