#importamos librerias necesarias y funcion del template body para crear el body
import requests, json
from template import template_body

def contents_body(url, largo = None):
    """Esta función tiene como objetivo definir el prototipo del template del body que tendrá nuestra pagina web
    de imagenes de aves
    
    Parameters:
    ----------
    Url : [string] 
        Corresponde a un string con la url de las imagenes de la aves
    Largo : [string] 
        Corresponde a la cantidad de imagenes de aves que se van a requerir para almacenar en el body

    Returns
    -------
    [Template body (String)] 
        Un string con el template del body para nuestra pagina html que se creará
    """
    response = json.loads(requests.get(url).text)[:largo] #Obtenemos la respuesta para un largo determinado si así se desea
    lista_nombre = [elemento['name'] for elemento in response] #Obtengo los nombre de cada ave
    lista_fotos = [elemento['images'] for elemento in response] #Obtengo las url de las imagenes de la api

    body = '' #Inicializamos el body
    for nombre, foto in zip(lista_nombre,lista_fotos):  #iteramos sobre la lista de nombres y url de imagenes
        url = foto['main'] #obtenmos url de la imagen
        nombre_ave = nombre['latin'] #obtenmos nombre en latin
        nombre_es = nombre['spanish'] #obtenmos nombre en español
        nombre_en = nombre['english'] #obtenmos nombre en ingles
        body += template_body(url, nombre_ave, nombre_es, nombre_en)+'\n' #creamos el body concatenado cada iteracion

    return body

#Probamos la funcion
if __name__ == '__main__':
    url = 'https://aves.ninjas.cl/api/birds'
    k = contents_body(url,3)
    print(k)
