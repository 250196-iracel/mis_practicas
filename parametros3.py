def verificar_acceso(edad):
    if edad >= 18:
        print("Acceso concedido: Eres mayor de edad.")
    else:
        print("Acceso denegado: Eres menor de edad.")

# Probando la función con diferentes edades
verificar_acceso(25)
verificar_acceso(16)