def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado  # Se movió fuera del ciclo for

print(factorial_iterativo(5))
