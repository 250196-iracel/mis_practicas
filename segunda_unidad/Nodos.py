class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None # REFERENCIA INICIAL QUE VA A INDICAR EL ORIGEN
        
    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        # Caso 1: si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        # Caso 2: recorrer hasta el último nodo que existe
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        # Conectar el último nodo con el nuevo nodo
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            # CORREGIDO: Se cambió la coma por un punto (actual.dato)
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        # Opcional: Se cambió "..." por " -> " para mejor lectura visual
        print("...".join(elementos) + "--None")

# USO DEL PROGRAMA
lista = ListaEnlazada()
# Insertar elementos a utilizar
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")
lista.mostrar_lista()
