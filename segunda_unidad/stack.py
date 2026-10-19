historial_navegacion=[]
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("Historial cargado: ", historial_navegacion)
#OPERACION TOP PEEK
pagina_actual=historial_navegacion[-1]
print("Pagina actual en pantalla: ",pagina_actual)
#OPERACION PARA DESAPILAR(POP)
pagina_cerrada=historial_navegacion.pop()
print("Saliendo de: ",pagina_cerrada)
print("Historial despues de presionar 'atras': ",historial_navegacion)

#OPERACION TAMAÑO (SIZE)
total_paginas=len(historial_navegacion)
print("Paginas previas guardadas: ",total_paginas)

 #OPERACION VACIA
sin_paginas = len(historial_navegacion) == 0 
print("¿El historial esta vacio?", sin_paginas)
