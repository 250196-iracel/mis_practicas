def mostrar_encabezado_escuela(): 
    print("Instituto x") 
    print("Reporte de evaluacion de calificaciones:") 

def obtener_nota_minima_aprobatoria(): 
    return 6.0 

def evaluar_rendimiento(nota_final): 
    if nota_final < 6.0: 
        return "Reprobado" 
    elif nota_final >= 6.0 and nota_final <= 9.4: 
        return "Aprobado" 
    elif nota_final >= 9.5 and nota_final <= 10: 
        return "Excelente" 
    else: 
        return "Nota no valida" 

def calcular_promedio_ponderado(nota_examenes, nota_tarea): 
    final = (nota_examenes * 0.7) + (nota_tarea * 0.3) 
    return round(final, 1) 

def generar_boleta(nombre_alumno, nota_examenes, nota_tarea): 
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tarea) 
    nota_minima = obtener_nota_minima_aprobatoria() 
    estado = evaluar_rendimiento(nota_final) 
    
    print(f"Boleta de {nombre_alumno}") 
    print(f"Nota de examen (70%): {nota_examenes}") 
    print(f"Nota de tareas (30%): {nota_tarea}") 
    print(f"Calificación final {nota_final}") 
    print(f"Estado academico: {estado}") 
    
    if nota_final < nota_minima: 
        print("Resultado: Debe presentar examen extraordinario") 
    else: 
        print("Resultado: No necesita presentar examen extraordinario") 

mostrar_encabezado_escuela() 
generar_boleta("Mayra Clemente", 8.5, 9.0)
