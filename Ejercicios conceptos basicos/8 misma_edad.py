"""
Mostrar en pantalla True o False
si la edad ingresada por 
dos usuarios es la misma.
"""

edad_user_1 = int(input('Ingresa edad del usuario 1\n>>> '))
edad_user_2 = int(input('Ingresa edad del usuario 2\n>>> '))

respuesta = edad_user_1 is edad_user_2

print(respuesta)