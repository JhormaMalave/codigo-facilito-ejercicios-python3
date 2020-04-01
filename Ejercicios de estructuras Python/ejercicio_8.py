"""
Mostrar en pantalla la frecuencia
de aparición de vocales en una 
frase dada por el usuario.
Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1
"""

frase = input('Ingresa una frase\n>>> ').lower()
vocales = ['a', 'e', 'i', 'o', 'u']
letra_cantidad = dict()

for letra in frase:
    if letra in vocales:
        letra_cantidad[letra] = letra_cantidad.get(letra, 0) + 1

print(letra_cantidad)