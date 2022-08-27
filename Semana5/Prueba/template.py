#importamos librerias necesarias
from string import Template

def template_html(title, body):
    """Esta función tiene como objetivo definir el prototipo del template que tendrá nuestra pagina web
    de imagenes de martes obtenidas por el curiosity
    
    Parameters:
    ----------
    Title : [string] 
        Corresponde al titulo que tendrá nuestra pagina web
    Body : [string] 
        Corresponde al body con las url de las imagenes del curiosity

    Returns
    -------
    [Template (String)] 
        Un string con el template html para la pagina web que se creará
    """
    #Definimos el template
    html_template = Template('''<!DOCTYPE html>
                                <html lang="es">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>$Titulo</title>
                                </head>
                                <h1> $Titulo </h1>
                                <body>
                                    $body
                                </body>
                                </html>
                                ''')
    html = html_template.substitute(Titulo = title, body = body) #Se sustituye el titulo y el body por los parametros necesarios
    return html

#Probamos la funcion creada
if __name__ == '__main__':
    titulo = 'Este es el titulo' 
    body =  'Este es el body'
    print(template_html(titulo,body))
