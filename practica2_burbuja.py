calificaciones=[8.5,9.2,7.8,9.0,8.8,7.6,9.5,8.9,6.9,7.5,9.3,9.6,8.9,7.8,9.9]
print(f"Lista original: {calificaciones}")
ascendente=calificaciones.copy()
n=len(ascendente)
for i in range (n):
    swapped=False
    for j in range (0, n-i-1):
        if ascendente[j]>ascendente[j+1]:
            ascendente[j],ascendente[j+1]=ascendente[j+1],ascendente[j]
            swapped=True

        if not swapped:
            break
            print (f"Orden Ascendente: {ascendente}")

            descendente=calificaciones.copy()

            for i in range(n):
                swapped=False
                for j in range (0,n-i-1):
                    if descendente[j]<descendente[j+1]:
                        descendente[j],descendente[j+1]=descendente[j+1],descendente[j]
                        swapped=True

                        if not swapped:
                            break 

                                  print (f"Orden Descendente: {descendente}")
