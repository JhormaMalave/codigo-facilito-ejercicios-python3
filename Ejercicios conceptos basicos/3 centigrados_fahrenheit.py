"""
Convertir los grados centígrados
ingresados por un usuario a
grados Fahrenheit y mostrar
el resultado en pantalla.
"""

centigrados = float(input("Ingresa los °C: "))
fahrenheit = (centigrados * 9 / 5 ) + 32
print("El resultado es:", fahrenheit, "°F")
