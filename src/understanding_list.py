"""

 Las listas nos permite almacenar informacion en un lugar, la cantidad que se desee: ya sean pocos elementos o millones de elementos.
 Una lista es una coleccion de items(elementos) que tienen un orden particular. Se pueden crear listas que incluyan strings, enteros, floats, 
 los nombres de las personas de tu familia, etcetera, podemos almacenar (los tipos de datos permitidos en python) lo que queramos  en una lista.

 Son elementos mutables: pueden modificarse el tamaño de la lista. 

 Se recomienda nombran una variable del tipo lista en plural.

 En python, los corchetes [] indican una lista, sus elementos se separan por comas.

 Ejemplo: 



"""



bicycles = ['trek', "cannondale", 'redline', 'specialized', 'giant']
print(bicycles)

# ¿Cómo podemos acceder a los elementos de una lista?
"""
 Las listas son colecciones ordenadas. Se pueden acceder a un elementos de una lista diciendole a Python la posicion o indice del elemento deseado.
 Para obtener el valor deseado, se debe escribir el nombre de la lista, seguido del indice del elemento entre corchetes.

"""

print(bicycles [0], bicycles [2], bicycles [3])

print(bicycles[0].upper())

# Los indices comienzas en 0, no en 1
# Ejemplo:

print(bicycles[1]) #cannondale
print(bicycles[3]) #speacialized

#Accediendo al ultimo elemento de una lista
print(bicycles[-1])
print(bicycles[-2])

# Utilizandop valores individuales de una lista
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)