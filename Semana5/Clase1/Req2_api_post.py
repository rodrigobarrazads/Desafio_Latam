'''
Requerimientos
2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
   diccionario de respuesta en una variable llamada created_user e imprímala en
   pantalla.
'''
#importamos librerias necesarias
import requests

#URL con la data de muestra
url = "https://reqres.in/api/users/"

#Creamos el requerimiento solicitado
payload='''{
            'nombre': 'Ignacio'
            'trabajo': 'Profesor'
            }'''     
headers = {}      

#Obtenemos la data creada
created_user = requests.request("POST", url, headers=headers, data=payload)

#se imprimen los resultados
print('-'*100)
print(f'Codigo de Respuesta: {created_user}') #Muestra el codigo asociado al get
print('-'*100)
print(f'Data Creada: \n {created_user.text}') #Muestra data extraida
print('-'*100) 