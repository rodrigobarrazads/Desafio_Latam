'''
Aplicando métodos apropiados para la estructura de datos entregada edite la lista de
recordatorios de la siguiente manera:

1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para "Empezar el Año".
2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea 
   el 16 de Julio.
3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
'''
#Eventos sin modificar
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para "Empezar el Año"
empezar_año = ["2021-01-02","06:00","Empezar el año"] #registro lista a agregar
recordatorios.insert(1,empezar_año) #agrego lista en la ubicacion deseada

#2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
error_fecha = ['2021-07-15', "13:00", "No hacer nada es feriado"] #registro lista a cambiar
indice_a_cambiar = recordatorios.index(error_fecha) #busco el indice de la lista a cambiar
recordatorios[indice_a_cambiar][0] = "2021-07-16" #cambio el valor de la lista por la que corresponde
#recordatorios[3][0]="2021-07-16" era ota forma mas facil de cambiar, pero menos elegante

#3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
eliminar = ['2021-05-01', "15:00", "No trabajar"] #registro lista a elimnar
indice_a_eliminar = recordatorios.index(eliminar) #busco el indice de la lista a eliminar
recordatorios.pop(indice_a_eliminar) #elimino registro de la lista

#4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad'] #registro lista de cena de navidad a agregar
recordatorios.insert(-1,cena_navidad) #agrego lista segun ubicacion deseada
cena_año_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo'] #registro lista cena de año nuevo a agregar
recordatorios.append(cena_año_nuevo) #agrego lista segun ubicacion deseada

#Se imprime el resultado obtenido
print('-'*60)
print(recordatorios)
print('-'*60)