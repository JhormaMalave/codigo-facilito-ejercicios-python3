"""
A partir del diccionario del
ejercicio anterior, mostrar
en pantalla la materia con
mejor promedio.
"""

# Creacion de variables
calificaciones = {'matematicas': 18, 'dibujo': 12, 'castellano': 19, 'ingles': 12}
calificaciones_total = 0
mejor_calificacion = 0

for calificacion in calificaciones:
    # Mejor calificacion
    if mejor_calificacion < calificaciones[calificacion]:
        mejor_calificacion = calificaciones[calificacion]
        mejor_calificacion_materia = {calificacion: calificaciones[calificacion]}

    # Promedio total
    calificaciones_total += calificaciones[calificacion]
promedio = calificaciones_total / len(calificaciones)

print("El promedio del estudiante es {}".format(promedio))
print("La mejor calificacion fue {} de {}".format(mejor_calificacion_materia))