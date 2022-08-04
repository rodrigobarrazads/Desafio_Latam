'''
Filtrado compacto
Una empresa provee de los balances del año anterior en un diccionario como se muestra a
continuación:
        ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
        }
Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
asociado siempre y cuando superen el umbral especificado.
'''
#Importamos librerias necesarias
import sys

umbral = int(sys.argv[1]) #Guardamos el umbral

#Definimos ventas del año anterior
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

#Definimos nuevo diccionario vacio
ventas_umbral = {}

# Iteramos sobre el diccionario
for clave, valor in ventas.items():
    if valor >= umbral:
        ventas_umbral[clave] = valor #Agregamos la tupla que cumple con condicion dada

print('-'*60)
print(ventas_umbral) #Impremimos las ventas que solo cumplen con un monto mayor al umbral
print('-'*60)