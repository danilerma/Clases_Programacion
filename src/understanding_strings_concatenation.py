# Combinacion o Concatenacion de STRING
# VARIABLE  
first_name = 'daniel'
last_name = "lerma"
full_name = first_name + " " + last_name 
print(full_name)
# PRINT
print("Hola".upper(), "Daniel" + " " + "Lerma", first_name.title() + " " + last_name.title())

message = "Hola, " + full_name.title() + "!"
print(message)



# WhiteSpace
"""
 WhiteSpace se refiere a cualquier String (Caracter)
 que no se imprime, es decir, un espacio (" "),
 tabuladores (\t) y finales de linea (\n).

 Los whitespace se utilizan comunmente para organizar
 las salidas de texto a usuario de tal manera que sea mas 
 amigable de leer o ver para los usuarios.
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \n Python \n C \n JavaScript")




# f-strings

famous_person = "daniel lerma".title()
message = famous_person + " dijo una vez: python es amor"
print(message)

message = f"{famous_person} una vez dijo: Python es amor"
print(message)