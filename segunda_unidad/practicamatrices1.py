import numpy as np
A=np.array([[10,15], [20,5]])
B=np.array([[5,12], [15,8]])

total_vendido=A+B
precio=50
ingreso_total=total_vendido*precio
print("Total de productos vendidos (Sabado + Domingo):")
print(total_vendido)
print("Ingreso total en pesos (a 50 pesos por producto): ")
print(ingreso_total)