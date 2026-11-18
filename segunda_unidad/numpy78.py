import numpy as np
#DEFINICIONES DE MATRICES
A=np.array([[1,2],[3,4]])
B=np.array( [[5,6],[7 ,8]])
#SUMA ELEMENTO A ELEMENTO
suma=A+B
print("..Suma(A+B)..")
print(suma)
#MULTIPLICACION
prod_elem=A*B
print("..MULTIPLICACION (A*B)..")
print(prod_elem)
#PRODUCTO MATRICIAL
prod_mat=A@B
print("..PRODUCTO MATRICIAL (A@B)..")
print(prod_mat)
#TRANSPUESTA
transpuesta=A. T
print("..TRANSPUESTA (A .T)..")
print(transpuesta)
#DETERMINANTE E INVERSA
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("..DETERMINANTE DE A..")
print(det)
print("..DETERMINANTE DE B..")
print(inv)
