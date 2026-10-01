# Trabajando con listas
print("\n\tel dia de hoy boy aprender a trabajar con listas\n".upper())
# Vamos a crear una lista de puros strings con nombres de magos
magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])

# Ciclo for
print("\n\tFor con saltos de linea".upper())
for magician in magicians:
    print(magician)

print("\n\tFor sin saltos de linea".upper())
for magician in magicians:
    print(magician, end =" ")


# A esto se le conoce como looping
# for cat in cats
# for dog in dogs
# for item in items

# Ahora vamos a imprimir un mensaje por cada mago}
print("\n\tMensaje de cada mago".upper())
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}\n")
print("Gracias a todos. Fue un gran espectaculo")