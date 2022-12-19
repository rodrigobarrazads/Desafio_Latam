import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


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

    ax.set_title('Confusion Matrix');
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Actual Values');

    ax.xaxis.set_ticklabels(['no morosos', 'moroso'])
    ax.yaxis.set_ticklabels(['no morosos', 'moroso'])