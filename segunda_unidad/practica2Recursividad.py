
def calcular_saldo_final(depositos, tasa_interes):
    # Caso base
    if depositos == []:
        return 0.0

    # Caso recursivo
    return (calcular_saldo_final(depositos[:-1], tasa_interes) + depositos[-1]) * (1 + tasa_interes)


# Ejemplo de uso
depositos = [1000, 2000, 1500]
tasa_interes = 0.05

resultado = calcular_saldo_final(depositos, tasa_interes)

print("Saldo final:", resultado)
