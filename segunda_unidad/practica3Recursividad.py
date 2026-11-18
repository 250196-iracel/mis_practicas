
def maxima_profundidad(comentarios):
    # Caso base
    if comentarios == []:
        return 0

    # Función auxiliar recursiva
    def calcular_elementos(lista, indice=0):
        if indice == len(lista):
            return 0

        elem = lista[indice]

        if isinstance(elem, list):
            profundidad = 1 + maxima_profundidad(elem)
        else:
            profundidad = 1

        return max(profundidad, calcular_elementos(lista, indice + 1))

    return calcular_elementos(comentarios)


# Ejemplo de uso
hilo = [
    "Comentario 1",
    ["Respuesta 1.1", ["Respuesta 1.1.1"]],
    "Comentario 2"
]

resultado = maxima_profundidad(hilo)

print("Profundidad máxima:", resultado)
