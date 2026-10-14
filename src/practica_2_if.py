"""
   Ejercicio

   Realizar un programa que determine el costo de un boleto 
   a partir de los siguientes condiciones:

   - costo para una persona menor o igual a 4 años: gratis.
   - costo para persona cuya edad es mayor a 4 años pero menor o igual a 18: 200
   - costo para una persona cuya edad es mayor a 18: 500


"""

age = input("Ingresa tu edad: ")
#print(type(age)) # String
age = int(age)
#print(type(age)) # Int

print(f"\nEsto se realiza con el bloque if-normal \n")

if age <= 4:
    cost = 0

if age > 4 and age <= 18:
    cost = 200

if age > 18:
    cost = 500

print(f"El costo de tu boleto es: {cost}")




# if-elif-else
print(f"\nEsto se realiza con el bloque if-elif-else \n")

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0

print(f"Costo (if-elif-else): {cost}")
