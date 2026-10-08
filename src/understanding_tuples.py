"""
  TUPLAS

  Las tuplas son listas de elementos que no cambian de tamaño.
  Las tuplas son listas inmutables.


  Se utilizan los parentesis () para definir una tupla.

  Ejemplo

    Si tenemos un rectangulo (largo, ancho) que siempre va a tener cierto tamaño, podemos asegurar que sus dimensiones
    no va a cambiar si colocamos sus valores en una tupla.

"""

dimensions = (200, 50) # 200 de largo x 50 de ancho
print(dimensions)


# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])

# print(dir(dimensions))

# Lista
# dimensions_2 = [200, 50]
# print(dir(dimensions_2))


# string
# name = "Daniel"
# print(dir(name))

# Vamos a  modificar el valor de una lista
names = ["Daniel", "Carlos", "Juan", "wendy"]
print(names)
names[0] = "Lerma"
names [1] = "Lerma"
names [2] = "Lerma"
print(names)

# dimensions[0] = "500" # Esta operacion no esta permitida

# Looping through a tuple
for  dimension in dimensions:
    print(dimension)


"""
    No podemos modificar una tupla, lo que si podemos hacer es cambiar la asignacion de una variable que almacena una tupla.
"""

dimensions = (500, 1000)
print("tupla re-definida:", dimensions)