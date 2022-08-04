'''
Primeros Auxilios
En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías
cómo reaccionar en caso de que alguien necesite de primeros auxilios?

Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de
emergencia. Es por eso que se le solicita construir una aplicación que permita indicar los
pasos a seguir ante una emergencia. Debido a que no se espera que usted sea un experto en
el tema se le provee de un diagrama que explica las distintas instancias a la que se está
sometido durante una emergencia.

Requerimientos
Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
en tiempo real.
'''

print('-'*110)
print('''Pasos a seguir en caso de que alguien necesite de primeros auxilios. Responder siempre con el número  
1 o 2 para una respuesta Si o No respectivamente. Ante cualquier otra respuesta el programa finalizará.''')
print('-'*110)
respuesta_1 = input('¿La persona responde a estimnulos? \n 1: SI \n 2: NO \nRespuesta: ')
print('-'*80)

if respuesta_1 == '1':
    print('>>>Debes valorar la necesidad de llevarlo al hospital más cercano')
    print('-'*80)
    print('Fin de las recomendaciones\n')
else: 
    print('>>>Debes abrir la vía Aérea')
    print('-'*80)
    respuesta_2 = input('¿La persona respira? \n 1: SI \n 2: NO \nRespuesta: ')
    print('-'*80)
    if respuesta_2 == '1':
        print('>>>Debes permitirle una posición de suficiente ventilación')
        print('-'*80)
        print('Fin de las recomendaciones\n')
    else:
        print('>>>Debes administrar 5 ventilaciones y llamar a la Ambulancia')
        print('-'*80)
        llego_ambulancia = [' ', False, True] #Definimos una lista con buleanos para ciclo while
        valor = True #Inicializamos el valor de la sentencia while
        while valor:
            respuesta_3 = input('¿La persona presenta signos de vida? \n 1: SI \n 2: NO \nRespuesta: ')
            print('-'*80)
            if respuesta_3 == '1':
                print('>>>Tienes que reevaluar a la espera de la Ambulancia')
                print('-'*80)
            else:
                print('>>>Debes administrar Compresiones Torácicas hasta que llegue la ambulancia')
                print('-'*80)
            respuesta_4 = input('¿Llego la Ambulancia? \n 1: SI \n 2: NO \nRespuesta: ')
            valor = llego_ambulancia[int(respuesta_4)] #Reasigna valor segun la respuesta del usuario para ver si sale o no del ciclo dependiendo se llego o no la ambulancia
            print('-'*80)
        print('No hay más recomendaciones\n')
        
            
