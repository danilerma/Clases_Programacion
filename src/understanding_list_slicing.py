players = ['Daniel', 'juan', 'iancarlo', 'lisandro']
print("Lista original: ", players)

# Silicing
print(players[0:2]) # ["daniel", "juan"]

# El slicing me permite trabajar con un grupo especifico de una lista: al resultado se le conoce como "un slice".

print(players[1:4]) #["juan", "iancarlo", "lisandro"]
print(":3", players[:3]) # ['daniel', 'juan', 'iancarlo']
print("2:", players[2:]) # ['iancarlo', 'lisandro']
print("[-3:]", players[-3:]) # ['juan', 'iancarlo', 'lisandro']


# players = ['Daniel', 'juan', 'iancarlo', 'lisandro']
# Casos Especiales
print(players[1:6]) # ['juan', 'iancarlo', 'lisandro']
print(players[6:1]) # []
print(players[:0])  # []

# Looping through a slice

print("\n\tLooping through a slice")
students = ['Daniel', 'Juan', 'Iancarlo', 'Lisandro']


for student in students[2:4]:
    print(f"El estudiante {student}, va a pasar la materia.")




# ¿Cómo podemos copir una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food # Manera erronea de copiar una lista

# Tres maneras de copiar una lista
# Metodo 1 - Utilizando slicing
my_friend_food_2 = my_food[:]

# Metodo 2 - Utilizando el metodo de las listas copy()
my_friend_food_3 = my_food.copy()

# Metodo 3 - Utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)