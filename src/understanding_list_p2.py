# Agegando elementos a una lista
motorcycles = ['honda', "mortalica", 'yamaha']
print(motorcycles) #['honda', "mortalica", 'yamaha']

# Metodo append - agrega elementos a la lista
motorcycles.append("Kawasaki")
print(motorcycles) # ['honda', "mortalica", 'yamaha', 'Kawasaki']

"""
  El metodo append ayuda a crear listas facilmente de manera dinamica.

"""
motorcycles_2 = [] #Lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle) # 1 elemento
motorcycles_2.append("yamaha") # 2 elemento
motorcycles_2.append("suzuki") # 3 elemento
print(motorcycles_2)
motorcycle = "Daniel"
print(motorcycles_2)
motorcycles_2.append(motorcycle)
print(motorcycles_2)
motorcycle = "Lerma"
print(motorcycle)
motorcycles_2.append(motorcycle)
print(motorcycles_2)

# EL metodo insert nos ayuda a agregar elementos a una lista en un indice especifico
motorcycles_3 = ['honda', "mortalica", 'suzuki']
print("\nLista Original")
print(motorcycles_3)
motorcycles_3.insert(3, "ducati")
print("Lista despues del metodo insert")
print(motorcycles_3)

## Metodo .pop() Elimina el ultimo elemento de una lista pero nos permite utilizar el elemento despues de eliminarlo.4

print("\n\tAqui aprendi a utilizar el metodo pop")
motorcycles_4 = ['honda', 'suzuki', 'mortalica', 'hd']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# Se puede utilizar para eliminar un elemento especifico.
motorcycles_5 = ['honda', 'suzuki', 'mortalica', 'hd']
motorcycles_5.pop(0)
print(motorcycles_5) # Lista sin honda

# Metodo .remove(), permite eliminar elementos por su valor.
print("\n\tAqui aprendi a utilizar el metodo remove")
motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)


