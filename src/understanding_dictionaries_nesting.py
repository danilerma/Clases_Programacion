# Nesting

# Listas de Diccionarios
covenant_elite = {"name": "Elite", "color": "blue", "points": 10, "shield": True}
covenant_jackal = {"name": "Jackal", "color": "gray", "points": 6, "shield": True}
covenant_grunts = {"name": "Grunts", "color": "orange", "points": 3, "shield": False}

# Nesting de Lista de diccionarios
covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

# Looping though the list
for covenant in covenants:
    print(covenant)


# Vamos a crear una flotilla de enemigos (Covenant)
covenants_fleet  = []
for _ in range(5):
    covenants_fleet.append(covenant_elite)

for _ in range(20):
    covenants_fleet.append(covenant_grunts)

print("\nFlotilla")
print(covenants_fleet)



# Nesting: Una losta en un diccionario
# Menu
print("\n Nesting: Listas en diccionarios")
tacos = {
    "tortillas": ["maiz", "harina"],
    "guisos": ["bistek", "tripa", "pastor"]
}

print(f"Tu has ordenando unos tacos de {tacos["guisos"][0]}")
print(f"En tortilla de {tacos["tortillas"][1]}")
