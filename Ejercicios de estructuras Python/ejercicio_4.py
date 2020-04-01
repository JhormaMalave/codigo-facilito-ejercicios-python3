"""
Dado una lista de frases
ingresadas por el usuario,
mostrar en pantalla todas
aquellas que sean palíndromo.
"""
cantidad_frases = int(input('¿Cuantas frases vas a ingresar?\n>>> '))
frases = []

for indice in range(1, cantidad_frases + 1):
    frase_original = input('Ingresa la frase {}\n>>> '.format(indice))
    # Se borra los espacios y se pone todo en minuscula
    frase_depurada = frase_original.replace(' ', '').lower()
    if frase_depurada == frase_depurada[::-1]:
        frases.append(frase_original)

print(frases)