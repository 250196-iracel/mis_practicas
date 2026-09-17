lista =[10,30,15,100]
n=len(lista)
swapped=True
while swapped:
    swapped=False
for i in range (n-1):
    if lista[i]>lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]
        swapped=True
print ("Lista ordenada:", lista)