'''
Fuerza bruta
¿Qué tan seguro es tu password? ¿Intentemos hackear un password? Mediante el siguiente
desafío se busca utilizar un algoritmo muy sencillo, llamado fuerza bruta para determinar
cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.

Para ello se ingresará un password oculto. Este password puede contener sólo
combinaciones de letras y se requiere determinar su seguridad. Un mayor número de
intentos implica un password más seguro:

El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en
orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña
indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.
'''
#Se importan la libreria getpass para ocultar la contraseña
import getpass
from string import ascii_lowercase

#Solicitamos clave 
print('-'*60)
password = getpass.getpass("Ingrese la contraseña: ").lower() #Forzamos a que la contraseña ingresada sea en minuscula para evitar problemas
letras_abecedario = ascii_lowercase #Almacenamos todas las letras del abecedario en orden

#Inicializamos el contador
i=0
#Iteramos sobre la constraseña
for letra_pasword in password:
    for letra in letras_abecedario:
        i+=1 #Contamos las veces iteradas
        if letra_pasword == letra: #Evaluamos condicion para salir del For anidado
            break
print(f'La contraseña fue forzada en {i} intentos')
print('-'*60)