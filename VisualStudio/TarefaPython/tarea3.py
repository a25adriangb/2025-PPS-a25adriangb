import random

# Tiradas do dado (números entre 1 e 6)
tiro1 = random.randint(1, 6)
tiro2 = random.randint(1, 6)

print("Primeira tirada:", tiro1)
print("Segunda tirada:", tiro2)

# Comparación
if tiro1 > tiro2:
    print("O maior é o primeiro.")
elif tiro2 > tiro1:
    print("O maior é o segundo.")
else:
    print("Hai empate.")
