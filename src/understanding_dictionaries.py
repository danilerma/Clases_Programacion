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

alien_0["x_position"] = 25
alien_0["y_position"] = 0

print(alien_0)