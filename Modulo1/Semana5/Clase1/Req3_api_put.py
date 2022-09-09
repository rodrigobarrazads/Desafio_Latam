'''
Requerimientos
3. Actualice un usuario llamado morpheus para que tenga un campo llamado
   residence igual a zion. Guarde el diccionario de respuesta en una variable llamada
   updated_user e imprímala en pantalla.
'''
#importamos librerias necesarias
import requests

#URL con la data de muestra
url = "https://reqres.in/api/users/2"

#Creamos el requerimiento solicitado
payload='''{
            'nombre': 'morpheus'
            'job': 'residence zion'
            }'''     
headers = {}      

#Obtenemos la data creada
update_user = requests.request("PUT", url, headers=headers, data=payload)

#se imprimen los resultados
print('-'*100)
print(f'Codigo de Respuesta: {update_user}') #Muestra el codigo asociado al get
print('-'*100)
print(f'Data Actualizada: \n {update_user.text}') #Muestra data extraida
print('-'*100) 