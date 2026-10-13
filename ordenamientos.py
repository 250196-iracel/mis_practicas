# ============================================
# REPASO DE PYTHON PARA EXAMEN
# LISTAS, ARREGLOS Y METODOS DE ORDENAMIENTO
# Burbuja, Seleccion, Insercion y QuickSort
# ============================================

# ---------- 1. MOSTRAR UNA LISTA ----------

def mostrar_lista(lista):
    if len(lista) == 0:
        print("La lista esta vacia.")
    else:
        print("Elementos de la lista:", lista)
        print("Cantidad de elementos:", len(lista))


# ---------- 2. AGREGAR ELEMENTOS ----------

def agregar_elemento(lista):
    numero = leer_entero("Ingresa un numero: ")
    lista.append(numero)
    print("Numero agregado correctamente.")


# ---------- 3. BUSQUEDA LINEAL ----------

def buscar_elemento(lista):
    numero = leer_entero("Numero que deseas buscar: ")

    encontrado = False

    for i in range(len(lista)):
        if lista[i] == numero:
            print("Encontrado en la posicion:", i)
            encontrado = True

    if encontrado == False:
        print("El numero no existe en la lista.")


# ---------- 4. ORDENAMIENTO BURBUJA ----------

def burbuja(lista):
    arreglo = lista.copy()
    n = len(arreglo)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arreglo[j] > arreglo[j + 1]:
                auxiliar = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = auxiliar

    return arreglo


# ---------- 5. ORDENAMIENTO POR SELECCION ----------

def seleccion(lista):
    arreglo = lista.copy()
    n = len(arreglo)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            if arreglo[j] < arreglo[menor]:
                menor = j

        auxiliar = arreglo[i]
        arreglo[i] = arreglo[menor]
        arreglo[menor] = auxiliar

    return arreglo


# ---------- 6. ORDENAMIENTO POR INSERCION ----------

def insercion(lista):
    arreglo = lista.copy()
    n = len(arreglo)

    for i in range(1, n):
        actual = arreglo[i]
        j = i - 1

        while j >= 0 and arreglo[j] > actual:
            arreglo[j + 1] = arreglo[j]
            j = j - 1

        arreglo[j + 1] = actual

    return arreglo


# ---------- 7. ORDENAMIENTO QUICKSORT ----------

def quicksort(lista):
    # Caso base: listas con cero o un elemento
    if len(lista) <= 1:
        return lista.copy()

    pivote = lista[len(lista) // 2]

    menores = []
    iguales = []
    mayores = []

    for numero in lista:
        if numero < pivote:
            menores.append(numero)
        elif numero == pivote:
            iguales.append(numero)
        else:
            mayores.append(numero)

    return (
        quicksort(menores)
        + iguales
        + quicksort(mayores)
    )


# ---------- 8. ORDENAR DE MAYOR A MENOR ----------

def ordenar_descendente(lista):
    arreglo = insercion(lista)

    arreglo.reverse()

    return arreglo


# ---------- 9. CALCULAR ESTADISTICAS ----------

def calcular_estadisticas(lista):
    if len(lista) == 0:
        print("No hay datos para calcular.")
        return

    suma = 0

    for numero in lista:
        suma += numero

    promedio = suma / len(lista)

    print("Suma:", suma)
    print("Promedio:", promedio)
    print("Mayor:", max(lista))
    print("Menor:", min(lista))


# ---------- 10. LEER ENTEROS CON VALIDACION ----------

def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debes ingresar un numero entero.")


# ---------- 11. MOSTRAR MENU ----------

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Mostrar lista")
    print("2. Agregar un elemento")
    print("3. Buscar un elemento")
    print("4. Ordenar por burbuja")
    print("5. Ordenar por seleccion")
    print("6. Ordenar por insercion")
    print("7. Ordenar por QuickSort")
    print("8. Ordenar de mayor a menor")
    print("9. Calcular estadisticas")
    print("10. Reiniciar lista")
    print("0. Salir")
    print("====================================")


# ---------- 12. PROGRAMA PRINCIPAL ----------

def main():
    # Lista inicial de ejemplo
    numeros = [8, 3, 10, 1, 6, 3, 12]

    while True:
        mostrar_menu()

        opcion = leer_entero("Selecciona una opcion: ")

        if opcion == 1:
            mostrar_lista(numeros)

        elif opcion == 2:
            agregar_elemento(numeros)
            mostrar_lista(numeros)

        elif opcion == 3:
            buscar_elemento(numeros)

        elif opcion == 4:
            resultado = burbuja(numeros)
            print("Ordenado por burbuja:", resultado)

        elif opcion == 5:
            resultado = seleccion(numeros)
            print("Ordenado por seleccion:", resultado)

        elif opcion == 6:
            resultado = insercion(numeros)
            print("Ordenado por insercion:", resultado)

        elif opcion == 7:
            resultado = quicksort(numeros)
            print("Ordenado por QuickSort:", resultado)

        elif opcion == 8:
            resultado = ordenar_descendente(numeros)
            print("De mayor a menor:", resultado)

        elif opcion == 9:
            calcular_estadisticas(numeros)

        elif opcion == 10:
            numeros = [8, 3, 10, 1, 6, 3, 12]
            print("Lista reiniciada:", numeros)

        elif opcion == 0:
            print("Fin del programa. Exito en tu examen.")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()