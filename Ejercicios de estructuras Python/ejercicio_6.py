"""
Remplazar cada letra
de una frase dada por
el usuario por la posición
que le corresponde en el
abecedario y mostrar el
nuevo string en pantalla.
(Los espacios no se remplazan).
Ejemplo: 
frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""

frase = input('Ingrese una frase\n>>> ').lower()
frase_numerica = str()
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedario_numerico = dict()

# Asignar valor a las letras del abecedario
for valor in range(1, len(abecedario) + 1):
    abecedario_numerico[abecedario[valor - 1]] = str(valor)

# Creacion de la nueva frase
for letra in frase:
    if not letra == ' ':
        frase_numerica += abecedario_numerico[letra]
    else:
        frase_numerica += ' '

print(frase_numerica)