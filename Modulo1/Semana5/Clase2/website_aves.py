'''
Descripción
La asociación de Amantes de los pájaros de Chile ha notado que actualmente no se tiene información de los distintos 
pájaros que pueden ser observados en Chile. Es por eso que les gustaría poder entender a manera de prototipo como 
poder listar muchos de estos especímenes. Para ello se le solicita generar un prototipo muy sencillo en el cual se puedan
observar algunas imágenes de pájaros típicos de Chile junto con su nombre en español e inglés. La idea es que esta 
información pueda ser eventualmente transformada en señaléticas bilingües que permitan fomentar el turismo en Chile.

Para ello se le da acceso a la API 'https://aves.ninjas.cl/api/birds', la cual da acceso a una base de datos con la 
información requerida.

Se solicita entonces que usted pueda crear un script en Python que permita crear este sitio web con los requerimientos 
solicitados, es decir, un listado con el título Aves de Chile, y cada especie registrada con su nombre en inglés y 
español junto con sus imágenes. 

Requerimientos
1. Crear templates del HTML a utilizar.
2. Generar un llamado a la API que permita recopilar la información necesaria para construir el sitio.
3. Exportar el sitio creado como un archivo html que pueda ser abierto en el navegador.
'''
#importamos desde los archivos las funciones requeridas para montar archivo html
from template import template_html
from body import contents_body

#Definimos titulo de nuestra pagina
titulo = 'Aves de Chile'
url = 'https://aves.ninjas.cl/api/birds'

#Llamamos a la funcion para crear el body requerido con las imagenes de las aves y sus nombres respectivos
body = contents_body(url)

#Obtenemos la estructura del HTML
html = template_html(titulo, body)

#Guardamos el archivo HTML 
with open('Aves_Chile.html','w') as f:
    f.write(html)


