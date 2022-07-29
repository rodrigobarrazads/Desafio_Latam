'''
Crear un archivo conversiones.py y una estructura de datos apropiada que permita
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.

Para ello considere las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
Además ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa
debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
'''
#Importa la libreria necesaria
import sys

#Guardo como variable las tasas de conversion
cambio_sol_peruano = float(sys.argv[1])
cambio_peso_argentino = float(sys.argv[2])
cambio_dolar_americano = float(sys.argv[3])
peso_chileno = int(sys.argv[4])

#Calculo el valor del monto del peso chileno ingresado a las distintas divisas
sol_peruano = cambio_sol_peruano * peso_chileno
peso_argentino = cambio_peso_argentino * peso_chileno
dolar_americano = cambio_dolar_americano * peso_chileno

#Imprimo los resultados
print('-'*60)
print(f'''Los {peso_chileno} pesos chilenos equivalen a: \n{sol_peruano} Soles \n{peso_argentino} Pesos Argentinos 
{dolar_americano} Dolares''')
print('-'*60)
