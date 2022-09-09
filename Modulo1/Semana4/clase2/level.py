def choose_level(n_pregunta, p_level):
    """Esta función tiene como objetivo entregar el nivel de dificultad en base al numero
    de pregunta y el numero de preguntas por nivel, con el cual se escogeran las preguntas
    
    Parameters:
    ----------
    n_pregunta : [int] 
        Corresponde al numero de preguntas a escoger
    p_level : [int] 
        Corresponde a numero de preguntas por nivel

    Returns
    -------
    [string] 
        Retorna el nivel escogido
    """
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2*p_level:
        level = 'intermedias'
    else: level = 'avanzadas'
    ##################################################
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias