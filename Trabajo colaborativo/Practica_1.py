"""Ejercicio 1
Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """

print("Hola Mundo!")

"""Ejercicio 2
 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. """

nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

"""Ejercicio 3
Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. """

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
lugar_residencia = input("Por favor, ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

"""Ejercicio 4
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro. """

import math

radio = float(input("Por favor, ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area} y el perímetro es: {perimetro}")

"""Ejercicio 5
Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale. """

segundos = int(input("Por favor, ingresa una cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas} horas.")

"""Ejercicio 6
Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.  """

numero = int(input("Por favor, ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

"""Ejercicio 7
Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

numero1 = int(input("Por favor, ingresa el primer número entero distinto de 0: "))
numero2 = int(input("Por favor, ingresa el segundo número entero distinto de 0: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2  
division = numero1 / numero2 
if numero1 == 0 or numero2 == 0:
    print("Los números deben ser distintos de 0.")
else:
    print(f"""Resultados de las operaciones con {numero1} y {numero2}:
          suma: {suma}
          resta: {resta}
          multiplicación: {multiplicacion}
          división: {division}""")

"""Ejercicio 8
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. """

altura_cm = float(input("Por favor, ingresa tu altura en centimetros: "))
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))

altura_m = altura_cm / 100

imc = peso / (altura_m ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc}")

"""Ejercicio 9
Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. """

grados_celsius = float(input("Por favor, ingresa una temperatura en grados Celsius: "))
grados_fahrenheit = (9/5 * grados_celsius) + 32

print(f"{grados_celsius} grados Celsius equivalen a {grados_fahrenheit} grados Fahrenheit.")

"""Ejercicio 10
 Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números. """

numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
numero3 = float(input("Por favor, ingresa el tercer número: ")) 

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los números {numero1}, {numero2} y {numero3} es: {promedio}")
