def es_capicua(numero):
    return str(numero) == str(numero)[::-1]


numero = input("Introduce un número: ")
print(es_capicua(numero))
