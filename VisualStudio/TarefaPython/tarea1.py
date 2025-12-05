posicion = int(input("Introduce la posición inicial: "))
lonxitude = int(input("Introduce la lonxitude: "))
frase = input("Introduce a frase: ")

# En Python, las posiciones empiezan en 0.
# Si el ejercicio considera posición empezando en 1, restamos 1.
inicio_real = posicion - 1

subcadea = frase[inicio_real : inicio_real + lonxitude]

print("Resultado =", subcadea)
