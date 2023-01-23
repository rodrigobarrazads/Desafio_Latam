import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.metrics import classification_report

# Se requiere las siguientes descargar para poder realizar la implementación
nltk.download('wordnet')
nltk.download('omw-1.4')

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
    tokenizer = RegexpTokenizer(r'\w+')
    lematizer = WordNetLemmatizer()

    stop_words = list(stopwords.words('english'))
    stop_words.append('im')
    stop_words.append('u')

    for i, row in enumerate(df[columna]):
        words = []
        tokens = tokenizer.tokenize(row)
        for tok in tokens:
            if tok not in stop_words:
                words.append(lematizer.lemmatize(tok))
                words_graf.append(lematizer.lemmatize(tok))
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