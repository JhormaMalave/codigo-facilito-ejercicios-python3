"""
Dado un diccionario, el cual
almacena las calificaciones
de un alumno, siendo las llaves
los nombres de las materia y los
valores las calificacion, mostrar
en pantalla el promedio del alumno.

"""
calificaciones = {'matematicas': 18, 'dibujo': 12, 'castellano': 10, 'ingles': 12}
calificaciones_total = 0
for calificacion in calificaciones:
    calificaciones_total += calificaciones[calificacion]
promedio = calificaciones_total / len(calificaciones)
print("El promedio del estudiante es {}".format(promedio))