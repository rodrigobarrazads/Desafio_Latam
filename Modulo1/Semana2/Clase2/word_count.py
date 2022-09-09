''' 
El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas
tipografías además de usarse para rellenar espacios que requieran largos textos.
¿Cuántas palabras componen este texto?

'''
#Importo las librerias necesarias
import sys

#Obtengo el directorio donde me encuentro y lo concateno con el nombre del archivo
nombre_archivo = sys.argv[1]

#Leemos el texto alojado en la misma carpeta del directorio
with open(nombre_archivo, "r") as file:
    texto = file.read()

#Contamos la cantidad de caracteres distintos
caracteres_unicos = set(texto) #convertimos el texto en estructura sets para dejar caracteres unicos
n_caracteres_unicos = len(caracteres_unicos) #guardamos la cantidad de caracteres unicos contando su largo

#Contamos la cantidad de caracteres distintos
texto_split = texto.split(" ") #se hace el split por espacio para convertirlo en una lista
palabras_unicas = set(texto_split) #convertimos la lista en estructura sets para dejar palabras unicas
n_palabras_unicas = len(palabras_unicas) #guardamos la cantidad de palabras unicas contando su largo

#Imprimimos el resultado
print('-'*60)
print(f'El número de caracteres distintos es: {n_caracteres_unicos}')
print(f'El número de palabras distintas es: {n_palabras_unicas}')
print('-'*60)
