import preguntas as p


def verificar(alternativas, eleccion):
    """Esta función tiene como objetivo verificar para un set de alternativas, si la respuesta 
    entregada corresponde a la alternativa correcta
    
    Parameters:
    ----------
    Alternativa : [lista] 
        Corresponde a la lista con las alternativas, donde cada alternativa cuenta con el indicador 
        si es la respuesta correcta
    Eleccion : [string] 
        Corresponde a la respuesta de la alternativas entregadas

    Returns
    -------
    [boolean] 
        Retorna un booleano indicando como True o False indicando si la respuesta es correcta o 
        incorrecta respectivamente
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    respuesta = alternativas.index(['alt_2', 1])
    if eleccion == respuesta:
        print('Respuesta Correcta')
        correcto = True
    else: 
        print('Respuesta Incorrecta')
        correcto = False
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






