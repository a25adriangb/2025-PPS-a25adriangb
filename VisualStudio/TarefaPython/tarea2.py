total_segundos = int(input("Introduce a cantidade de segundos: "))

minutos = total_segundos // 60  # Minutos enteiros
segundos = total_segundos % 60  # Resto da división (equivalente a segundos)

print(f"{minutos} minutos e {segundos} segundos.")
