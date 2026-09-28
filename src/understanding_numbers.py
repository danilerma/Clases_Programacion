# Numeros
# Enteros - Integers
"""
   Los numeros enteros los podemos sumar (+),
   restar (-), multiplicar (*), dividir (/).

"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)
print(3**2) #3^2
print(3**3) #3^3
print(10**6) #10^6
print(10%2) #Módulo (mod)
age = 17     # Entero (int)
print(age)
name = "Daniel Lerma"  # String
print(name, age)

# Floats (Flotantes)
"""
 Python llama floats a cualquier numero con punto decimal
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# Imprimir la edad de alguien 
age = 17 # Variable del tipo Int
# message = 'Daniel tiene' + age + 'años.' (Error)
message = 'Daniel tiene ' + str(age) + ' años.'
message_f = f"Daniel tiene {age} años."
print(message)
print(message_f)
"""
 Type Error: Python no puede reconocer el tipo de informacion que se esta utilizando.

 En este caso no se pueden concatenar ints a strings
 """
print (type(age))
print (type(0.1))
print (type(message_f), type (1+5), type(2+0.1))
