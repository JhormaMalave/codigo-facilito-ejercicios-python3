"""
Mostrar en pantalla
el promedio de un
alumno que ha cursado
5 materias (Español, 
Matemáticas, Economía,
Programación, Ingles).
"""

castellano = int(input('Calificacion de castellano\n>>> '))
matematicas = int(input('Calificacion de matematicas\n>>> '))
economia = int(input('Calificacion de economia\n>>> '))
programacion = int(input('Calificacion de programacion\n>>> '))
ingles = int(input('Calificacion de ingles\n>>> '))

promedio = (castellano + matematicas + economia + programacion + ingles) / 5

print('Promedio:',str(promedio))