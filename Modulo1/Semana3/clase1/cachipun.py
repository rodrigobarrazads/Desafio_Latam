'''
Descripción
El Cachipún, conocido también como chin chan pu, pikachú, jankenpón, yan ken po, pin pon
papas, hakembó o how-are-you-speak, es un juego de manos en el que existen tres
elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo
y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado. Se
utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se
hace a veces usando una moneda, o para dirimir algún asunto.
Para poner en práctica lo que hemos aprendido a lo largo de la unidad, se implementará un
programa en Python que permite jugar al cachipún en contra del computador.

Requerimientos
1. Se pide crear el programa cachipun.py, donde el usuario entregará como
   argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
   valor al azar. Para eso se solicita investigar random.choice() de la librería random.
2. Considerar las opciones de ganar, perder o empatar con la computadora.
3. En caso que el argumento sea distinto a piedra, papel o tijera, el programa debe
   mostrar las opciones que se pueden jugar.
'''

#Se importa libreria para generar numero aleatorio
import random
import sys

usuario = sys.argv[1].lower() #Se deja todo como minuscula para un mejor manejo en caso que el usuario escriba opcion con alguna mayuscula
opciones = ['piedra', 'papel', 'tijera'] #Definimos los posibles valores a elegir
entra_al_juego = usuario in opciones #Valido si el valor del usuario esta dentro de la lista de opciones elegibles y escritas correctamente
computador =  random.choice(opciones) #encontramos el valor escogido por el computador

print('-'*60)
#Si variable es False, entonces debe arrojar la error del argumento
if entra_al_juego == False:
   print('Argumento inválido: Debe ser piedra, papel o tijera.')
#En caso contrario, la opcion ingresada es correcta
#Usuario Empata:
elif usuario == computador:
   print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nEmpate!!')
#Usuario gana:
elif (usuario == 'piedra' and computador == 'tijera') or (usuario == 'papel' and computador == 'piedra') or (usuario == 'tijera' and computador == 'papel'):
   print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nGanaste!!')
#Usuario Pierde:
else: print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nPerdiste!!')
print('-'*60)