"""
Crear una lista la cual
almacene 10 números positivos
ingresados por el usuario,
mostrar en pantalla: la suma
de todos los números, el promedio,
el número mayor y el número menor.
"""

numeros = []
suma_numeros = 0
numero_mayor = 0
numero_menor = 1000000000
for indice in range(1,11):
	numero = int(input("Ingresa el numero {}: \n>>> ".format(indice)))
	if numero > numero_mayor:
		numero_mayor = numero 
	if numero < numero_menor:
		numero_menor = numero 
	suma_numeros += numero
	numeros.append(numero)

promedio = suma_numeros / len(numeros)

print("Suma de total {}".format(suma_numeros))
print("Promedio {}".format(promedio))
print("Numero mayor {}".format(numero_mayor))
print("Numero_menor {}".format(numero_menor))
