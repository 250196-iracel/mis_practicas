from collections import deque
import time

cola_turnos=deque()
cola_turnos.append("Turno A01 - Isidoro Ortiz Ramirez")
cola_turnos.append("Turno A02 - Guadalupe Perez Dias")
cola_turnos.append("Turno A03 - Juana Lazcano Rodriguez")

print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print(" -", turno)

print("\nIniciando atención en ventanilla")

while len(cola_turnos) > 0:
    turno_actual = cola_turnos.popleft()

    print("\nLlamando a ventanilla:", turno_actual)

    time.sleep(1)

    print("Atención finalizada:", turno_actual)
    print("(Clientes restantes en la fila:", len(cola_turnos), ")")

print("\nSe han atendido todos los turnos. Fila vacía.")