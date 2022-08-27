'''
Requerimientos
4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.
'''
#importamos librerias necesarias
import requests

#URL con la data de muestra
url = "https://reqres.in/api/users/6" #Acá se encuentra el usuario llamado Tracey

payload = {} 
headers = {}      

#Obtenemos la data creada
delete_user = requests.request("DELETE", url, headers=headers, data=payload)

#se imprimen los resultados
print('-'*100)
print(f'Codigo de Respuesta: {delete_user}') #Muestra el codigo asociado al get
print('-'*100)
print(f'Data Eliminada {delete_user.text}') #Muestra data extraida
print('-'*100) 