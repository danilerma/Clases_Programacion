# Diccionario Simple
alien_0 = {"color": "green", "points": 5}

# Diccionario vacio 
alien_1 = {}

# El diccionario mas simple
alien_2 = {"color": "verde"}

# Accesar a los elementos de un diccionario
print(f"Tu alien 0 es de color: {alien_0["color"].upper()}")
print(f"Si desvives al alien 0 se te otorga: {alien_0["points"]}")

# Agregar elementos a un diccionario

print("\nAgregando elementos al dict")
alien_0["x_position"] = 25
alien_0["y_position"] = 0

print(alien_0)

# Modificando un valor en un diccionario

print("\nModificando elementos del dict")
alien_0["y_position"] = 80
print(alien_0)

# Eliminando un valor de un diccionario

print("\nEliminando elementos del dict")
del alien_0["points"]
print(alien_0)

# Diccionarios para objetos (elementos) similares
favorite_languajes = {
    "jen": "python", 
    "sarah": "c", 
    "eduard": "ruby", 
    "phill": "python"
}

# Looping though all key-values pairs
# Looping a traves de todos los partes llaves-color
user_0 = {
    "username": "Daniel",
    "firstname": "Lerma",
    "lastname": "Martinez",
    "birthday": "24_11_08"
}

print("\nLooping a traves de los pares llave, valor \n")
for key, value in user_0.items():
    print("Key:", key)
    print("Value:", value, "\n")


print("\nLooping a traves de los valores\n")
for value in user_0.values():
    print()
