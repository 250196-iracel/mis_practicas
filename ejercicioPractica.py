estudiantes=["Ana", "Carlos", "Diana"]
print(f"1. lista inicial: {estudiantes}")

estudiantes.append("Elena")
estudiantes.insert(1,"Beatriz")
print(f"2. lista tras inserciones: {estudiantes}")

print("BUSQUEDA Y ACCESO POR INDICE ")
print(f"Estudiante en el indice cero: {estudiantes[0]}")
print(f"Estudiante en el indice dos: {estudiantes[2]}")

posicion_diana=estudiantes.index("Diana")
print(f"Diana se encuentra en el indice: {posicion_diana}")

print("Operaciones de Slicing [INICIO-FIN-PASO]")
print(f"Los primeros tres estudiantes son: {estudiantes[:3]}")
print(f"El primer subconjunto de estudiantes son: {estudiantes[1:4]}")
print(f"Los ultimos estudiantes son [-2]: {estudiantes[-2:]}")
print(f"Lista totalmente invertida [::-1]: {estudiantes[::-1]}")

