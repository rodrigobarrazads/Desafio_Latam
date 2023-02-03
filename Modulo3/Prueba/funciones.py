import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import spacy 
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.metrics import classification_report, confusion_matrix

# Definimos el idioma para la lemmatización
nlp = spacy.load('en_core_web_sm')

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


def graf_word_cloud(df, columna):
    """
        Objetivo:
            - Realizar una nube de palabras para una variable con contiene textos, tokenizando, lematizando y eliminando los stopwords del texto. Además, 
              deja en una nueva columna llamada 'content_clean el texto totalmente limpio'
        Parámetros:
            - df (Dataframe): Dataframe a utlizar
            - columna (string): Nombre de la columna con el texto
        Retorno:
           - (print) nube de palabras
    """

    text_clean = []
    words = []
    words_graf = []

    stop_words = list(stopwords.words('english'))
    stop_words.append('im')
    stop_words.append('u')

    for i, row in enumerate(df[columna]):
        words = []
        for tok in nlp(row):
            tok = tok.lemma_
            if tok not in stop_words and tok not in ['-pron-','-PRON-']:
                words.append(tok)
                words_graf.append(tok)
        text_clean.insert(i," ".join(words))
    df['content_clean'] = text_clean

    wc = WordCloud(width=1280, height=720, max_words=200)
    long_str = ','.join(words_graf)
    word_cloud = wc.generate(long_str)

    plt.figure(figsize=(20, 20))
    plt.imshow(word_cloud)
    plt.axis("off")


def plot_classification_report(y_test, class_pred, dummy_class=False):
    """TODO: Docstring for plot_classification_report.

    :y_test: TODO
    :class_pred: TODO
    :dummy_class: TODO
    :returns: TODO

    """

    colors = ['dodgerblue', 'tomato']
    report = pd.DataFrame(classification_report(y_test, class_pred, output_dict=True))
    class_specific_values = report.drop(columns=['accuracy', 'macro avg', 'weighted avg'])
    class_specific_values = report.loc[:, class_specific_values.columns].T
    macro_avg = report.drop(index='support')['macro avg']

    for index, value in enumerate(class_specific_values.index):
        plt.scatter(class_specific_values['precision'][value], [1], marker='x', c=colors[index])
        plt.scatter(class_specific_values['recall'][value], [2], marker='x', c=colors[index])
        plt.scatter(class_specific_values['f1-score'][value], [3], marker='x', c=colors[index], label=f"Class: {index}")

    plt.scatter(macro_avg, [1, 2, 3], color='forestgreen', label='Macro Average')
    plt.yticks([1.0, 2.0, 3.0], ['Precision', 'Recall', 'F1-Score'])

    if dummy_class is True:
        plt.axvline(.5, label = '.5 Boundary', linestyle='--')


def distr_num(data, columna, target):
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
    ax.set_title(f'Distribucion de la variable {columna} con respecto al vector objetivo');
    ax = fig.add_subplot(spec[1, 0])
    ax = sns.distplot(data[columna])
    ax.axvline(np.mean(data[columna]), color='red')

    plt.xlabel(f'Valores de la variable {columna}')
    plt.ylabel('Frecuencia observada')
    plt.title(f'Distribución de la variable {columna}')
    plt.legend(labels=['Curva de densidad','Media', 'Distribucion de los datos']);
    
    plt.show()


def dist_cat(df, target, ancho=30, largo=80):
    """
        Objetivo:
            - Generar un gráficos de barras agrupadas para cada variable categórica según una variable objetivo (taret)
            
        Parámetros:
            - df (dataframe): Dataframe que contine las variables categóricas y vector objetivo
            - target (string): Nombre del vector objetivo
            - ancho (int): ancho del plot
            - largo (int): largo del plot

        Retorno:
            - (plot) Entrega graficos de barras separado por clusters
    """

    fig = plt.figure()
    fig.set_size_inches(ancho,largo)
    i = 1

    # ITERAMOS SOBRE CADA VARIABLE SIN TRANSFORMAR Y GRAFICAMOS PARA OBSERVAR SU DISTRIBUCIÓN
    col_cat = df.drop(columns=target).select_dtypes(['object',int,'category']).columns
    for col in col_cat:
        df_graf = pd.DataFrame(df.groupby(by=[target,col])[col].count()).rename(columns={col:'count'}).reset_index()
        df_graf = df_graf.pivot(index=target, columns=col, values='count')
        df_graf.reset_index(inplace=True)

        df_graf.plot(ax = plt.subplot(15,5,i), 
                    x=target,
                    kind='bar',
                    stacked=False,
                    title=f'Distribución de la variable {col}');
        plt.xticks(rotation=360)
        i+= 1

    plt.show()

def valores_unicos(dataset):
    """
        Objetivo:
            - realiza un value_counts para cada variable del dataset
        Parámetros:
            - data (Dataframe): Dataframe a realizar el análisis
        Retorno:
           - (print) value_counts de cada columna
    """
    for col in dataset:
        print(f'Columna : {col}')
        print(dataset[col].value_counts(normalize= True))
        print('-'*80)


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