'''
Requerimientos
1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una
   variable llamada users_data e imprímala en pantalla.
'''
#importamos librerias necesarias
import requests

#URL con la data de muestra
url = "https://reqres.in/api/users"

payload={}     
headers = {}      

#Obtenemos la data con get
user_data = requests.request("GET", url, headers=headers, data=payload)

#se imprimen los resultados
print('-'*100)
print(f'Codigo de Respuesta: {user_data}') #Muestra el codigo asociado al get
print('-'*100)
print(f'Data Extraida: \n {user_data.text}') #Muestra data extraida
print('-'*100) 