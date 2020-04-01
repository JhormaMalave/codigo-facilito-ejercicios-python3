"""
Eliminar todas las vocales
de una frase dado por el 
usuario y mostrar el nuevo
string en pantalla.
"""

frase = input('Igresa una frase\n>>> ').lower()
vocales = ['a', 'e', 'i', 'o', 'u']
frase_nueva = str()

for letra in frase:
    if not letra in vocales:
        frase_nueva += letra

print(frase_nueva)