import preguntas as p
import random

def shuffle_alt(pregunta):
    """Esta función tiene como objetivo aleatorizar el orden de la lista entregada, 
    es decir, aleatoriza el orden de las alternativas de cada pregunta
    
    Parameters:
    ----------
    Pregunta : [lista] 
        Corresponde a la lista con las alternativas de cada preguntas
    
    Returns
    -------
    [lista] 
        Retorna la misma lista del argumento pero con sus elementos aleatorizados
    """
    #mezclar alternativas
    #######################################################################
    random.shuffle(pregunta['alternativas'])
    #######################################################################
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]