#CREACION DE UNA MATRIZ
matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#ACCESO A ELEMENTOS
print(matriz[1][2])#IMPRIMIR INDICES A 1 COLUMNA INDICE 2

#MODIFICAR ELEMENTOS
matriz[0][0]=50

#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
        print()