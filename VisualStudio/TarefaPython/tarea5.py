lista = [12,23,5,29,92,64]

# Elimina o último número e engádeo ao principio.
ultimo = lista.pop()
lista.insert(0,ultimo)

print (lista)

# Move o segundo elemento á última posición
segundo = lista.pop(1)
lista.append(segundo)
print (lista)

# Engade o número 14 ao comezo da lista
lista.insert(0,14)
print (lista)

# Suma todos os números da lista e engade o resultado ao final da lista
suma = sum(lista)
lista.append(suma)
print (lista)

#Fusiona a lista actual coa seguinte: [4, 11, 32]
lista2= [4,11,32]
lista.extend(lista2)
print (lista)

# Elimina todos os números impares da lista
pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)

lista=pares
print(lista)

# Ordena os números da lista de forma ascendente
lista.sort()
print (lista)

# Baleira a lista
lista.clear()
print (lista)



