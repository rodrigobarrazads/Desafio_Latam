import pandas as pd

def porcentaje_null(data):  
    """
        Objetivo:
            - Obtener cantidad de valores nulos y su correspondiente porcentaje dentro del dataframe 
        Parámetros:
            - data (Dataframe): Dataframe con las variables que se desean ver los porcentajes de nulos
        Retorno:
           - (print) variables con cantidades y porcentajes de nulos
    """

    count_null=data.isna().sum()
    N = data.shape[0]
    v_porcentaje=[]
    for num in count_null:
        por=round(num/N, 4) 
        v_porcentaje.append(por)
    tabla_null=pd.DataFrame({'N_NaN':count_null, 'Porcentaje':v_porcentaje})
    print(tabla_null.sort_values(by = 'Porcentaje', ascending=False))