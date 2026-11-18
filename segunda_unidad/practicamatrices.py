A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]

total_vendido = []

for i in range(2):
    fila = []
    for j in range(2):
        fila.append(A[i][j] + B[i][j])
    total_vendido.append(fila)

precio = 50
ingreso_total = []

for i in range(2):
    fila = []
    for j in range(2):
        fila.append(total_vendido[i][j] * precio)
    ingreso_total.append(fila)

print("Total de productos vendidos (Sábado + Domingo):")
for fila in total_vendido:
    print(fila)

print("Ingreso total en pesos (a $50 por producto):")
for fila in ingreso_total:
    print(fila)