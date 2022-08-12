def validate(opciones, eleccion):
    """Esta función tiene como objetivo validar que la respuesta se 
    encuentre dentro de las opciones a escoger.
    
    Parameters:
    ----------
    Opciones : [lista] 
        Corresponde a la lista con las opciones disponibles a elegir
    Eleccion : [int] o [string] 
        Corresponde a la eleccion elegida por el usuario
    
    Returns
    -------
    [int] o [string] 
        Retorna la Eleccion del usuario previamente validada
    """
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: \n >').lower()
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    opciones = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(opciones, eleccion)
    
    
