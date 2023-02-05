#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, roc_curve, auc

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


def grid_plot_batch(df, cols, plot_type):

    """
    grid_plot_batch: Genera una grilla matplotlib para cada conjunto de variables.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame
        - cols: cantidad de columnas en la grilla.
        - plot_type: tipo de gráfico a generar. Puede ser una instrucción genérica de matplotlib o seaborn.

    Retorno:
        - Una grilla generada con plt.subplots y las instrucciones dentro de cada celda.

    """
    # calcular un aproximado a la cantidad de filas
    rows = np.ceil(df.shape[1] / cols)

    # para cada columna
    for index, (colname, serie) in enumerate(df.iteritems()):
        plt.subplot(rows, cols, index + 1)
        plot_type(serie)
        plt.title(colname)
        plt.xlabel('')
        plt.tight_layout()

def identify_high_correlations(df, threshold=.7):
    """
    identify_high_correlations: Genera un reporte sobre las correlaciones existentes entre variables, condicional a un nivel arbitrario.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame, por lo general es la base de datos a trabajar.
        - threshold: Nivel de correlaciones a considerar como altas. Por defecto es .7.

    Retorno:
        - Un pd.DataFrame con los nombres de las variables y sus correlaciones
    """

    # extraemos la matriz de correlación con una máscara booleana
    tmp = df.corr().mask(abs(df.corr()) < .8, df)
    # convertimos a long format
    tmp = pd.melt(tmp)
    # agregamos una columna extra que nos facilitará los cruces entre variables
    tmp['var2'] = list(df.columns) * len(df.columns)
    # reordenamos
    tmp = tmp[['variable', 'var2', 'value']].dropna()
    # eliminamos valores duplicados
    tmp = tmp[tmp['value'].duplicated()]
    # eliminamos variables con valores de 1 
    return tmp[tmp['value'] < 1.00]

def plot_roc(model, y_true, X_test, model_label=None):
    """TODO: Docstring for plot_roc.

    :model: TODO
    :y_true: TODO
    :X_test: TODO
    :model_label: TODO
    :returns: TODO

    """
    class_pred = model.predict_proba(X_test)[:1]
    false_positive_rates, true_positive_rates, _ = roc_curve(y_true, class_pred)
    store_auc = auc(false_positive_rates, true_positive_rates)

    if model_label is not None:
        tmp_label = f'{model_label}: {round(store_auc, 3)}'
    else:
        tmp_label = None
    plt.plot(false_positive_rates, true_positive_rates, label=tmp_label)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
