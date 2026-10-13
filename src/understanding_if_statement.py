# If Statement
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car)  


# EL condicional o condition
# EL condicional es el corazon del if

# Condicional Verdadero 
# Condicional = True
truck = "ford"
print(truck == "ford")

# Condicional Falso
# Condicional False
print(truck == "audi")

#
print(truck == "Ford".lower())


# Condicional de desigualdad !=
print(truck!="audi") # True
print(truck!="ford") # False


# Comparaciones numéricas
print("Comparaciones Numericas")
age = 34
print(age==34) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta")

# Conector menor que <
print("Conectores < > <= >=")
age = 19
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Multiple conditions
print("\n\tMultiple conditions")
print("\n\tOperacion AND")
age_0 = 22
age_1 = 18
print(age_0>=21 and age_1 >= 21)
print(age_0>=21 and age_1 >= 18)










age = 21
if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿Ya fuiste a tramitar tu INE?")
else: 
    print("Lo siento, eres demasiado joven para votar")
    print("Ve a registrarte cuando cumplas 18 años")