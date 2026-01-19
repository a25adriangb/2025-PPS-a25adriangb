def es_entero(cadena):
    if cadena.isdigit():
        return True
    else:
        return False


cadena = input("Introduce una cadena: ")
print(es_entero(cadena))
