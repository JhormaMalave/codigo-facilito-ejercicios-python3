"""
Mostrar en pantalla la
cantidad de vocales que
existe en una frase dada
por el usuario.
"""

frase = input('Ingresa una frase\n>>> ').lower()
vocales = ['a', 'e', 'i', 'o', 'u']
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print('Cantidad de vocales:', contador)

