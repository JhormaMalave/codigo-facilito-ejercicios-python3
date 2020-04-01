"""
Convertir la cantidad de dólares
ingresados por un usuario a
bolivares venezolanos
y mostrar el resultado en pantalla.
"""
#Lunes 23 marzo 2020 11:42am DolarToday
cambio_actual = 75184.82
dolares = float(input("Ingresa la cantidad de dólares: "))
resultado = dolares * cambio_actual
print("El resultado sería:", resultado, "bls")
