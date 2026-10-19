guisos = ["Salsa Verde","Desebrada", "Nopales"]

if "Salsa Verde" in guisos:
    print("Hay salsa verde.")
elif "Desebrada" in guisos:
    print("Hay desebrada")
elif "Guiso especial" in guisos:
    print("Hay guiso especial")


#Lista Vacia
guisos_2 = ["salsa verde", "picadillo", "asado"]
if guisos_2:
    for guiso in guisos_2:
        print(guiso)
else:
    print("No hay guisos")

#
guisos_disponibles = ["salsa verde", "desebradas", "picadillo", "asado"]
guisos_a_ordenar = ["barbacoa", "desebrada", "cabrito"]

for guiso in guisos_a_ordenar:

    if guiso in guisos_disponibles:
        print(f"Ordenaste {guiso}: Si hay de ese guiso")
    else:
        print(f"Ordenaste {guiso}: Una disculpa, no tenemos de ese guiso")

print("Final")