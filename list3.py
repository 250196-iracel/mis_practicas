frutas =["manzana","guayaba","uva"]
#ACTUALIZAR
frutas[1] = "pera"
#INSERTAR
frutas.append("sandia")
#extend une multiples elementos al final de la lista
frutas.extend(["kiwi","Mango"])
#ELIMINAR
retirado = frutas.pop(2)
ultimo=frutas.pop()
#busca el valor exacto y elimina la primera aparicion
frutas.remove("sandia")
#del utiliza palabra clave para borrar una casilla directamente
del frutas[0]

posicion=frutas.index("kiwi")
print(frutas)