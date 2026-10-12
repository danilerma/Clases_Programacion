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