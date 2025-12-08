# Pedimos os dous números enteiros
n1 = int(input("Escriba o primeiro número enteiro: "))
n2 = int(input("Escriba o segundo número enteiro: "))

# Si o primeiro e menos xeneramos unha lista creciente.
if n1 <= n2:
    lista = list(range(n1, n2 + 1))
# Si o primeiro e maior xeneramos lista decrecente.
else:
    lista = list(range(n1, n2 - 1, -1))

print(lista)