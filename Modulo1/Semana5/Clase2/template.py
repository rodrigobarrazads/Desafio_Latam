from string import Template

def template_html(title, body):
    """Esta función tiene como objetivo definir el prototipo del template html que tendrá nuestra pagina web
    de imagenes de aves
    
    Parameters:
    ----------
    Title : [string] 
        Corresponde al titulo que tendrá nuestra pagina web
    Body : [string] 
        Corresponde al body con las url de las imagenes de las aves

    Returns
    -------
    [Template (String)] 
        Un string con el template html para la pagina web que se creará
    """
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
    html = html_template.substitute(Titulo = title, body = body)
    return html

def template_body(url, name_ave, name_es, name_en):
    """Esta función tiene como objetivo crear el body de nuestra pagina web con las url de las imagenes de las aves
    y la descripcion de cada una de estas
    
    Parameters:
    ----------
    Url : [lista] 
        Corresponde a una lista con las url de las imagenes de las aves
    Name_ave : [lista] 
        Corresponde a una lista con el nombre en latin de las aves
    Name_es : [lista] 
        Corresponde a una lista con el nombre en español de las aves
    NAme_en : [lista] 
        Corresponde a una lista con el nombre en ingles

    Returns
    -------
    [String] 
        Un string con el template del body para nuestra pagina web de aves
    """
    body_template = Template('''<img src="$url">
                                 <h1> $name_ave </h1>
                                 <h3> $name_es / $name_en </h3>
                                 ''')   #Se define el template prototipo del body para las imagenes y descripcion de las aves

    image = body_template.substitute(url = url, name_ave = name_ave, name_es = name_es, name_en = name_en) #Sustituimos por los parametros de la funcion

    return image

#Probamos la funcion
if __name__ == '__main__':
    titulo = 'Este es el titulo' 
    body =  'Este es el body'
    print(template_html(titulo,body))

    url = 'Aca va la url'
    nombre_ave = 'Aca va el nombre latin de la ave'
    nombre_es = 'aca va el nombre en español'
    nombre_en = 'aca va el nombre en ingles'
    print(template_body(url, nombre_ave, nombre_es, nombre_en))