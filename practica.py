inventario = ["laptop","tarjeta de video","procesador","memoria RAM"]
inventario.append("disco SSD")
inventario.insert(2,"fuente de poder")
inventario.extend(["gabinete","monitor 4k","teclado mecanico","mouse gamer",])
posicion=inventario.index("monitor 4k")
inventario[3]="memoria RAM DDR5"
equipo_despachado = inventario.pop()
inventario.remove("tarjeta de video")
print(equipo_despachado)
print("lista final:",inventario)
print("cantidad total:",len(inventario))
