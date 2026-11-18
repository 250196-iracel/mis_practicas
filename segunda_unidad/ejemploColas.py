from collections import deque
import time

pedidos = deque()

# Registrar pedidos de los clientes
pedidos.append("Pedido 101 - Pizza de pepperoni")
pedidos.append("Pedido 102 - Pizza hawaiana")
pedidos.append("Pedido 103 - Pizza de queso")
pedidos.append("Pedido 104 - Pizza mexicana")

print("=== PIZZERIA EL BUEN SABOR ===")
print("Pedidos pendientes:", len(pedidos))

# Mostrar los pedidos registrados
for pedido in pedidos:
    print(pedido)

print("\nComenzando la preparacion de pizzas...")

# Preparar los pedidos
while pedidos:
    pedido_preparado = pedidos.popleft()

    print("\nPreparando:", pedido_preparado)
    time.sleep(2)

    print("Pedido listo para entregar.")

    if pedidos:
        print("Siguiente pedido:", pedidos[0])
    else:
        print("No hay mas pedidos pendientes.")

print("\nTodos los pedidos fueron preparados.")