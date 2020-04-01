"""
Calcular y mostrar en pantalla
la longitud de la sombra de un
edificio de 20 metros de altura
cuando el ángulo que forman los
rayos del sol con el suelo es de 22º.
"""
from math import tan, radians

altura = 20
angulo = 22

# Para obtener la tangente se debe ingesar en radianes en vez de grados
radian = radians(angulo)
longitud_sombra = altura / tan(radian)
print("La longitud de la sombra es", longitud_sombra)
