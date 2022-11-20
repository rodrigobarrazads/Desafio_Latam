import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score 
from math import sqrt


def graf_pie(data, name_column):
    """
        Objetivo:
            - Generar un gráfico de torta 
        Parámetros:
            - data (Dataframe): Dataframe donde se encuentra la variable a graficar
            - name_column (string): nombre de la variable a graficar

        Retorno:
           - (Grafico) gráfico de torta
    """
    
    df_pie = data[name_column].value_counts().to_frame()

    plt.pie(x=df_pie[name_column], labels=df_pie.index, autopct = '%.2f%%')
    plt.title(f"Distribución de la variable {name_column}")
    plt.legend()
    plt.show()

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

def recodificar(df, columna, obj):
    """
        Objetivo:
            - recodifica una variable
        Parámetros:
            - df (Dataframe): Dataframe que contenga la variable a recodificar
            - columna (string): nombre de la variable a recodificar
            - obj (dict): Diccionario como 
                    -'key': nombre de las nuevas categorias
                    -'values' lista de las categorias a recodificar

        Retorno:
           - (Dataframe) Dataframe con la variable recodificada
    """

    df_tmp = df.copy()
    serie = pd.Series(obj)
    for n, llave in enumerate(serie.index):
        df_tmp[columna].replace(serie.get(llave), [llave]*len(serie.get(llave)), inplace = True)
    return df_tmp[columna]


def distr_with_cat(data, columna, target):
    """
        Objetivo:
            - realizar un boxplot y un histograma con la distribucion de una variable continua, junto con un 
              boxplot de la distribucion de la variable con respecto a una la variable objetivo y/o categorica
        Parámetros:
            - data (Dataframe): Dataframe que contenga la variable numérica, y la variable categorica o target
            - columna (string): nombre de la variable continua a graficar
            - target (string): nombre del target (variable objetivo) o variable categorica

        Retorno:
           - (plot) boxplot e histograma
    """

    fig = plt.figure(constrained_layout=True, figsize=(13,6))
    widths = [2, 1.5]
    heights = [1, 3]
    spec = fig.add_gridspec(ncols=2, nrows=2, width_ratios=widths,
                                height_ratios=heights)
    
    ax = fig.add_subplot(spec[0, 0])
    ax = sns.boxplot(data[columna]).set(title = f'Boxplot de la variable {columna}', xlabel='')
    ax = fig.add_subplot(spec[:, 1])
    ax = sns.boxplot(x=data[target], y=data[columna])
    ax.set_title(f'Distribucion de la variable {columna} con respecto al vector objetivo')
    ax = fig.add_subplot(spec[1, 0])
    ax = sns.distplot(data[columna])
    ax.axvline(np.mean(data[columna]), color='red')

    plt.legend()
    plt.xlabel(f'Valores de la variable {columna}')
    plt.ylabel('Frecuencia observada')
    plt.title(f'Distribución de la variable {columna}')
    plt.legend(labels=['Curva de densidad','Media', 'Distribucion de los datos'])
    
    plt.show()


def hist_and_box(data, columna):
    """
        Objetivo:
            - realizar un boxplot y un histograma con la distribucion de una variable continua
        Parámetros:
            - data (Dataframe): Dataframe que contenga la variable a graficar
            - columna (string): nombre de la variable a graficar

        Retorno:
           - (plot) boxplot e histograma
    """

    f, ax = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.20, .80)})

    sns.boxplot(data[columna], ax=ax[0]).set(title = f'Boxplot de la variable {columna}', xlabel='')
    sns.distplot(data[columna], ax=ax[1])
    ax[1].axvline(np.mean(data[columna]), color='red')
    plt.legend()
    plt.xlabel(f'Valores de la variable {columna}')
    plt.ylabel('Frecuencia observada')
    plt.title(f'Distribución de la variable {columna}')
    plt.legend(labels=['Curva de densidad','Media', 'Distribucion de los datos'])
    
    plt.show()


def binarization(data, column):
    """
        Objetivo:
            - binarizar una columna, dejando fuera como columna a la clase minoritaria
        Parámetros:
            - data (Dataframe): Dataframe que contenga la variable a binarizar
            - column (string): nombre de la variable a binarizar

        Retorno:
           - (dataframe) dataframe con la variable binarizada
    """

    df = data.copy()
    df[f'{column}_bin'] = np.where(df[column] == df[column].value_counts().index[1], 1, 0)

    return df


def dummies(data, columnas):
    """
        Objetivo:
            - generar variables dummies de una lista de nombres de columnas, dejando fuera como columna a la clase minoritaria de cada variable 
        Parámetros:
            - data (Dataframe): Dataframe que contenga las variables a binarizar
            - columnas (list): lista con el nombrse de la variables a binarizar

        Retorno:
           - (dataframe) dataframe con la variable binarizada
    """

    list = []
    for col in columnas:
        name_cat_minoritaria = f'{col}_{data[col].value_counts(ascending=True).index[0]}'
        list.append(name_cat_minoritaria)

    df_dummy = pd.get_dummies(data[columnas])
    df_dummy = df_dummy.drop(list, axis=1)
    df_dummy = pd.concat([data,df_dummy], axis=1)

    return df_dummy


def matriz_confusion(y_test, y_pred):
    """
        Objetivo:
            - graficar la matriz de confunsión
        Parámetros:
            - y_test (list): lista con los valores del vector objetivo
            - y_pred (list): lista con las predicciones del vector objetivo

        Retorno:
           - (plot) matriz de confución
    """

    cf_matrix = confusion_matrix(y_test, y_pred)

    group_names = ['True Neg','False Pos','False Neg','True Pos']
    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]

    labels = [f"{v1}\n{v2}" for v1, v2 in zip(group_names,group_counts)]
    labels = np.asarray(labels).reshape(2,2)

    ax = sns.heatmap(cf_matrix,  annot=labels ,fmt='', cmap='Blues')

    ax.set_title('Confusion Matrix\nTrue: >50k\nFalse: <=50k');
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Actual Values');

    ax.xaxis.set_ticklabels(['False', 'True'])
    ax.yaxis.set_ticklabels(['False', 'True'])


def report_scores(target_testeo, predicciones):
    """
        Objetivo:
            - Reportar las metricas MSE y R2 para un conjunto de datos de testeo y las predicciones de dicho conjunto de datos
        Parámetros:
            - target_testeo (serie): serie con los datos de testeo no probados.
            - predicciones (serie): serie con las predicciones de dichos datos 

        Retorno:
           - print con los scores de las metricas MSE y R2
    """
    print(f"  Mean Error: {(np.mean(target_testeo-predicciones)):.2f}")
    print(f"  MSE: {mean_squared_error(target_testeo, predicciones):.2f}")
    print(f'  RMSE: {sqrt(mean_squared_error(target_testeo, predicciones)):.2f}')