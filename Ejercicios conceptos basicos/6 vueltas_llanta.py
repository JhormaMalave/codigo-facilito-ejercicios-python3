"""
Calcular el número de vueltas
que da una llanta en 1 km,
dado que el diámetro de la
llanta es de 50 cm, mostrar
el resultado en pantalla.
"""
from math import pi

distancia_km = 1
distancia_cm = distancia_km * 100000
diametro_cm = 50
perimetro_cm = diametro_cm * pi

vueltas = distancia_cm / perimetro_cm
print("Un llanta de",diametro_cm,"cm realiza",vueltas,"vueltas en",distancia_km,"km")
