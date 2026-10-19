pila=[]
print("Paso 1: Pila Creada: ",pila)

for i in range(1,11):
    pila.append(f"Plato {i}")

print("Paso 2:Despues de apilar 10 elementos: ", pila)
if len(pila)>0:
    print("Paso 3: El plato que esta arriba del todo (cima) es: ",pila[-1])

print("Paso 4: Desapilando 4 platos:")
for i in range(4):
    plato_sacado=pila.pop()
    print(f"Se saco: {plato_sacado}")

print("Pila ahora:", pila)
print("Aqui se ve LIFO: el ultimo en entrar (plato 10) fue el primero en salir")

print("Paso 5")
print(f"Tamaño de la pila: {len(pila)} elementos")

print("Paso 6: Vaciar la pila por completo")
while len (pila)>0:
    pila.pop()
    
sin_platos=len(pila)==0
print("Pila Final:", pila)
print(f"¿Esta vacia ahora?",sin_platos)