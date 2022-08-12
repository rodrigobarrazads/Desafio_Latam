import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    """Esta función tiene como objetivo seleccionar una pregunta de un set de preguntas para un 
    nivel de dificultad entregado y retornar el enunciado y las alternativas de dicha pregunta para 
    dicho nivel entregado, eliminando la pregunta previamente escogida del set de preguntas disponibles
    
    Parameters:
    ----------
    Dificultad : [string] 
        Corresponde al nivel de dificultad desde donde se quiere obtener la pregunta
    
    Returns
    -------
    [string] 
        Retorna el enunciado de la pregunta escogida para el nivel escogido
    [lista] 
        Retorna la lista con las alternativas para dicho enunciado
    """
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(preguntas[f'pregunta_{n_elegido}'])
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')