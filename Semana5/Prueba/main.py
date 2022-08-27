#importamos desde functions las funciones creadas para el requerimiento deseado
from functions import request_get, lista_imagenes, build_web_page

largo = 25 #Definimos el largo de los registros que queremos, en este caso por lo requerido en la prueba, serán solo 25

#llamamos a esta funcion para obtener los 25 primeros registros de la api incluyendo las imagenes y la info asociada a ella
response = request_get(largo) 

#llamamos a esta funcion para obtener la lista de las imagenes del rovert de la NASA
url_imagenes = lista_imagenes(response) 

#llamamos a la funcion para crear nuestro sitio web con las imagenes, creado el html llamado Aves_Chile.thml
build_web_page(url_imagenes) 

