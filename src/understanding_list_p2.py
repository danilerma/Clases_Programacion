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
motorcycles_3.insert(0, "ducati")
print("Lista despues del metodo insert")
print(motorcycles_3)