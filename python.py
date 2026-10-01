import matplotlib.pyplot as plt 

datos = [42, 12, 88, 23, 7, 65, 34, 50]

# ALGORITMO DE INSERCIÓN
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)): # <- Corregido [] por ()
        clave, j = a[i], i - 1
        while j >= 0 and a[j] > clave:
            comp += 1
            a[j+1] = a[j]
            j -= 1 # <- Corregido j=1 por j-=1 para evitar bucle infinito
        
        # Estas líneas van fuera del while
        if j >= 0: 
            comp += 1
        a[j+1] = clave
        
    return a, comp # <- Corregido: movido fuera de los bucles

# ALGORITMO DE SELECCIÓN
def seleccion(arr):
    a = arr.copy()
    n = len(a) # <- Corregido: definición de n
    comp = 0
    for i in range(n):
        min_idnx = i
        for j in range(i + 1, n): # <- Corregido i+1+,n
            comp += 1
            if a[j] < a[min_idnx]:
                min_idnx = j
        # El intercambio va fuera del bucle 'j'
        a[i], a[min_idnx] = a[min_idnx], a[i]
        
    return a, comp # <- Corregido: movido fuera de los bucles

# Ejecutamos los dos algoritmos
lista_ordenada, comp_ins = insercion(datos)
lista_ordenada_sel, comp_sel = seleccion(datos) # <- Corregido: quitado el guion '-' inicial

# graficacion: lista desordenada
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4)) # <- Corregido subplots y figsize

# GRAFICO 1: LISTA DESORDENADA
ax1.bar(range(len(datos)), datos, color='red')
ax1.set_title('1. Lista Original')
ax1.set_ylabel('Valor')

# GRAFICO 2: LISTA_ORDENADA
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='blue')
ax2.set_title('2. Lista Ordenada')

# GRAFICO 3: COMPARACIONES REALIZADAS 
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_sel], color=["#175b8b", "#b6733a"])
ax3.set_title('3. Comparaciones')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show() 