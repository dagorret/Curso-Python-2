mi_lista = ["elemento 1", "elemento 2", "elemento 3", "elemento 4"]

print(mi_lista)

print(mi_lista[1])

print(mi_lista[-2])

print(mi_lista[0:3])

#Es lo mismo
print(mi_lista[:3])

print(mi_lista[1:3])

print(mi_lista[2:])

# Agregar elementos a la lista

mi_lista.append("Elemento 5")

print(mi_lista)

mi_lista.insert(2, "Elemento 6")

print(mi_lista)

mi_lista.extend(["Elemento 7", "Elemento 8"])

print(mi_lista)

# Buscar el indice de un elemento

print(mi_lista.index("Elemento 5"))

# Comprobar si un elemento existe
print("elemento 1" in mi_lista)

# Eliminar un elementos
mi_lista.remove("elemento 2")
print(mi_lista)

# Eliminar el ultimo elemento
mi_lista.pop()
print(mi_lista)

# 
mi_lista2 = ["alfa", "beta"]

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista2 = ["*"]
print(mi_lista2 * 3)