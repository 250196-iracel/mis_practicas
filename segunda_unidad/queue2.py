from collections import deque
import time
cola_reproduccion=deque()
#AGREGAR CANCIONES A LA COLA
cola_reproduccion.append("1. Antologia")
cola_reproduccion.append("2. Viento")
cola_reproduccion.append("3. Pop")
#MOSTRAR CANCIONES EN ESPERA
print("CANCIONES EN ESPERA")
for cancion in cola_reproduccion:
    print(" _ ",cancion)
    print("Iniciando reproducción ")
#EL REPRODUCTOR PROCESA LA COLA, CANCION POR CANCION
#DESENCOLAR
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"sonando ahora: {cancion_actual}")
    time.sleep(1)#PARA QUE SIMULE AGREGACION DEL TEMA
    print(f"Finalizo: {cancion_actual}")
#MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA
print(f"(Quedan: {len(cola_reproduccion)} canciones en la cola")
print("LA COLA DE REPRODUCCION HA FINALIZADO")
