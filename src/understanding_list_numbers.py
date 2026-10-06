# Listas de Numeros
"""
  Las Listas tambien pueden almacenar numeros. Python ofrede varias herramientas que ayudan a trabajar eficientemente con listas de numeros.

"""

# Metodo Build-in range()
"""
  El Metodo range() nos ayuda a crear facilmente series de numeros.


Ejemplo

"""

first_ten_numbers = range(0, 10)
# print(type(first_ten_numbers))
for value in first_ten_numbers:
    print(value)

for value in range(1, 6):
    print(value)


# Crear una lista de  numeros utilizando range
numbers = list(range(1, 6))
print(numbers)

# Lista de numeros pares
even_numbers = list(range(0, 100, 5))
print(even_numbers)