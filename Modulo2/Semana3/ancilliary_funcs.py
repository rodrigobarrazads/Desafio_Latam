import numpy as np
import matplotlib.pyplot as plt

def fecth_descriptives(dataframe):
    """
        Objetivo:
            - Retornar las estadisticas descriptivas de un dataframe entregado
            
        Parámetros:
            - dataframe (dataframe): Dataframe que contine las variables para el resumen de estadistica descriptiva

        Retorno:
           - Retorna un frame el resumen de las variables entregadas
    """

    df_categoricas = dataframe.select_dtypes('object')
    df_numericas = dataframe.select_dtypes(np.number)
    print(df_numericas.describe())

    for columns, serie in df_categoricas.iteritems():
        print(serie.value_counts().to_frame())



def listar_nulos(dataframe, var, print_list = False):
    """
        Objetivo:
            - Retornar la cantidad de casos perdidos y el porcentaje correspondiente de estos, para una variable
            
        Parámetros:
            - dataframe (dataframe): Dataframe donde esta la variable a calcular
            - var (columna): Nombre de la columna para calcular
            - print_list (booleano): Se especifica si se quiere saber cuales son las regiones de la variable es nula. Por defecto es False

        Retorno:
           - Retorna un print con la candidad de nulos de la variable y el porcentaje correspondiente
    """

    perdidos = dataframe[var].isna()
    n_perdidos = perdidos.sum()
    porc_nulos = n_perdidos/perdidos.shape[0]
    lista_regiones = dataframe[perdidos]['ht_region'].unique().tolist()

    print(f'Cantidad de nulos de {var}: {n_perdidos}')
    print(f'Porcentaje de nulos de {var}: {porc_nulos}')

    if print_list == True:
        print(f'Las regiones donde {var} es nula son: {lista_regiones}\n')



def plot_hist(sample_df, full_df, var, true_mean, sample_mean = False):
    """
        Objetivo:
            - Generar un histograma de una variable entregada para un Dataframe de muestra
            
        Parámetros:
            - sample_df (dataframe): Dataframe de muestra
            - full_df (dataframe): Dataframe completo
            - var (columna): Nombre de la columna a graficar en el histograma
            - true_mean (booleano): Se especifica si se desea mostrar el valor de la media de la columna entregada segun el dataset completo. Por defecto es True
            - sample_mean (booleano): Se especifica si se desea mostrar el valor de la media de la columna entregada segun el dataset de muestra. Por defecto es True

        Retorno:
           - Retorna un histograma con las medias especificadas
    """

    sample_var = sample_df[var].dropna()
    full_var = full_df[var].dropna()

    plt.hist(sample_var, color= 'blue', alpha = .4, label = var)

    if sample_mean == True:
        plt.axvline(sample_var.mean(), color = 'tomato', ls = '--', label = f'Media_Muestral de {var}')

    if true_mean == True:
        plt.axvline(full_var.mean(), color = 'blue', ls = '--', label = f'Meadia_Real de {var}')    

    plt.legend()



def dotplot(dataframe, plot_var, plot_by, statistic = 'mean', global_stat = False):
    """
        Objetivo:
            - Generar un dotplot de una variable entregada para un Dataframe
            
        Parámetros:
            - dataframe (dataframe): Dataframe donde se encuentra la columna a graficar
            - plot_var (columna): Nombre de la columna a graficar en el histograma
            - plot_by (columna): Nombre de la columna segun un filtro
            - statistic (string): Nombre de la estadistica a mostrar. Admite solo 2 valores posible: mean o median
            - global_stat (booleano): Se especifica si se desea mostrar el valor de la media de la columna entregada. Por defecto es True

        Retorno:
           - Retorna un histograma con las medias especificadas
    """
    
    medias = dataframe.groupby(plot_by)[plot_var].mean()
    medianas = dataframe.groupby(plot_by)[plot_var].median()

    if statistic =='mean' and global_stat == False:
        plt.plot(medias.values, medias.index, 'o', label= f'media de {plot_var}')

    if statistic =='median' and global_stat == False:
        plt.plot(medianas.values, medianas.index, 'o', label= f'mediana de {plot_var}')

    if statistic =='mean' and global_stat == True:
        plt.plot(medias.values, medias.index, 'o', label= f'media de {plot_var}')
        plt.axvline(dataframe[plot_var].mean(), color = 'tomato', ls = '--', label = f'media global de {plot_var}')

    if statistic =='median' and global_stat == True:
        plt.plot(medianas.values, medianas.index, 'o', label= f'mediana de {plot_var}')
        plt.axvline(dataframe[plot_var].mean(), color = 'tomato', ls = '--', label = f'mediana global de {plot_var}')
    
    plt.legend()