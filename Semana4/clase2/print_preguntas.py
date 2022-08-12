import preguntas as p

def print_pregunta(enunciado, alternativas):
    """Esta función tiene como objetivo mostrar en pantalla el enunciado y las alternativas
    entregadas con un formato amigable para el usuario
    
    Parameters:
    ----------
    Enunciado : [string] 
        Corresponde al enunciado de una pregunta en especifica
    Alternativas : [lista] 
        Corresponde a las alternativas del enunciado entregado

    Returns
    -------
    [print] 
        Muestra en patanlla el enunciado y las alternativas en un formato de quizz
    """
    # Imprimir enunciado y alternativas
    ###############################################################
    print(''.join(enunciado))
    letras = ['A.','B.','C.','D.']
    for let, alt in zip(letras,alternativas):
        print(let, f'Alternativa {alt[0][-1]}')
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4