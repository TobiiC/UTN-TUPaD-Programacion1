"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """

i = 0
while i <= 100:
    print(i)
    i += 1

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. """

numero = int(input("Ingrese un número entero: "))
numero_original = numero
cantidad = 0
while numero > 0:
    numero //= 10
    cantidad += 1
    
print(f"El número {numero_original} tiene {cantidad} dígito(s).")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """

valor1 = int(input("Ingrese el primer valor (entero): "))
valor2 = int(input("Ingrese el segundo valor (entero): "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

suma = 0

for i in range(valor1 + 1, valor2):
    suma += i


print("La suma de los números entre", valor1, "y", valor2, "es:", suma)


"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. """

numero = int(input("Ingrese un número entero para sumar: "))
suma = 0
if numero != 0:
    while numero != 0:
        suma += numero
        numero = int(input("Ingrese un número entero (0 para finalizar): "))

    print("La suma total es:", suma)
else:
    print("La suma total es: 0")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numero_aleatorio = random.randint(0, 9)

intento = int(input("Adivina el número (entre 0 y 9): "))
contador_intentos = 1

while intento != numero_aleatorio:
    intento = int(input("Incorrecto. Intenta de nuevo: "))
    contador_intentos += 1

print(f"¡Correcto! Adivinaste el número en {contador_intentos} intentos.")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. """

i = 100

while i >= 0:   
    if i % 2 == 0:
        print(i)
    i -= 1


"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. """

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
if numero > 0:
    for i in range(numero + 1):
        suma += i
    print("La suma de los números entre 0 y", numero, "es:", suma)
else:
    print("Por favor, ingrese un número entero positivo.")



"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).""" 

cantidad_numeros = 100  
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

print(f"Cantidad de números pares {contador_pares} y impares {contador_impares}")
print(f"Cantidad de numeros positivos {contador_positivos} y negativos {contador_negativos}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 
"""
cantidad_numeros = 100
suma = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad_numeros

print(f"La media de los {cantidad_numeros} números ingresados es: {media}")


"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = int(input("Ingrese un número entero: "))
numero_original = numero
digito = 0
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

if numero < 0:
    invertido = -invertido

print(f"El número {numero_original} invertido es: {invertido}")

