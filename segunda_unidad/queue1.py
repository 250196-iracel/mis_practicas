from collections import deque
cola=deque()
#Agregar elementos a la cola(encolar)
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#Sacar el primer elemento que llego(desencolar)
atendido=cola.popleft()
#Mostar resultado sobtenidos
print("Atendido: ",atendido)
print("Cola restante: ",cola)