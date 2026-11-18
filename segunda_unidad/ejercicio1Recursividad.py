def limpiar_feed(publicaciones: list) -> list:
    # Caso base: si la lista tiene 0 o 1 elementos, no puede tener duplicados consecutivos
    if len(publicaciones) <= 1:
        return publicaciones

    # Caso recursivo: comparar el primer elemento con el segundo
    if publicaciones[0] == publicaciones[1]:
        # Si son iguales, omitimos el primero y llamamos a la función con el resto de la lista
        return limpiar_feed(publicaciones[1:])
    else:
        # Si son diferentes, conservamos el primero y lo concatenamos con el resultado de procesar el resto
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])


# Ejemplo de uso tal como indica el ejercicio:
entrada = ["Post A", "Post A", "Post B", "Post B", "Post C", "Post B"]
resultado = limpiar_feed(entrada)

print(resultado)
