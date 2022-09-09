#Se importan librerias necesarias y la funcion que define y crea el template de nuestra pagina web
import requests, json
from string import Template
from template import template_html

def request_get(largo):
    """Esta función tiene como objetivo crear el metodo get para obtener la informacion de la api, como lo es las url de las imagenes 
    y la informacion asociada a ella
    
    Parameters:
    ----------
    Largo : [int] 
        Corresponde a la cantidad de registros que se quiere obteneres desde la api

    Returns
    -------
    [lista] 
        Una lista con el registro de la informacion asociada a cada imagen captura por el curiosity
    """
    apikey = '2q4SMLKRLpkoRrAefPdMhqh0Q0PjPSQMgyDStozJ'  #Api key obtenida desde la pagina de la nasa
    url_api_nasa = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos' #Url de la api de la nasa
    response = json.loads(requests.get(url_api_nasa +'?api_key='+ apikey).text) #obtenemos la respuesta de la api

    return response['latest_photos'][:largo]  #Retornamos la informacion que nos entrega la api con la cantidad registros solicitados


def lista_imagenes(response):
    """Esta función tiene como objetivo crear una lista que contenga solo las url de las imagenes asociadas a un response
    
    Parameters:
    ----------
    Response : [lista] 
        Corresponde a la informacion obtenida desde un metodo get a la api

    Returns
    -------
    [lista] 
        Una lista con las url de cada imagen 
    """
    lista_fotos = [elemento['img_src'] for elemento in response] #Obtengo las url de las imagenes de la api

    return lista_fotos #Retornamos una lista con las url de las imagenes


def build_web_page(lista_imagenes):
    """Esta función tiene como objetivo crear el archivo html con el template para crear la pagina web
    de imagenes de marte
    
    Parameters:
    ----------
    Lista_imagenes : [lista] 
        Corresponde a Una lista con las url de cada imagen 

    Returns
    -------
    [Archivo html] 
        un archivo html llamado Imagenes_NASA.html con las imagenes deseadas 
    """
    template_image = Template('<img src="$url">') #Definimos el template html para las imagenes
    body = ''  #inicializo template del body con imagenes
    for url in lista_imagenes:   #itero para obtener el body del html con la informacion de las imagenes
        body += template_image.substitute(url = url)+'\n'  #agrego las url en el body

    titulo = 'Imagenes del Rovert en Marte de la NASA' #Defino un titulo para la pagina web
    html = template_html(titulo, body) #Creo el HTML con el titulo y el body con las imagenes en su formato correspondiente

    with open('Imagenes_NASA.html','w') as f:  #Por ultimo, guardo el archivo como un HTML
        f.write(html)

#Probamos las funciones creadas
if __name__ == '__main__':
    largo = 3
    response = request_get(largo)
    print(response)
    print(len(response))

    imagenes = lista_imagenes(response)
    print(imagenes)

    build_web_page(imagenes)


