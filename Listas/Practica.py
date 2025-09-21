"""1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja. """

notas = [7, 8.5, 6, 9, 5.5, 10, 4, 8, 7.5, 6.5]
print ("Lista de notas:", notas)
promedio = sum(notas) / len(notas)
print ("Promedio de notas:", promedio)
print ("Nota más alta:", max(notas))
print ("Nota más baja:", min(notas))

"""2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista. """

productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
print("Lista de productos ordenada alfabéticamente:", sorted(productos))
opcion = input("¿Desea eliminar un producto? (s/n): ").lower()
if opcion == "s":
    producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    if producto_eliminar in productos:
        productos.remove(producto_eliminar)
        print("Lista actualizada de productos:", productos)
    else:
        print("El producto no se encuentra en la lista.")
else:
    print("No se realizaron cambios en la lista de productos.")


""""3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista. """

import random
numeros = [random.randint(1, 100) for _ in range(15)]
lista_pares = [num for num in numeros if num % 2 == 0]
lista_impares = [num for num in numeros if num % 2 != 0]
print(f"Números generados: {numeros}")
print(f"Números pares: {lista_pares} y tiene una cantidad de {len(lista_pares)} números")
print(f"Números impares: {lista_impares} y tiene una cantidad de {len(lista_impares)} números")

""""4) Dada una lista con valores repetidos: 
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. """

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

lista_sin_repetidos = list(set(datos))
print("Lista sin elementos repetidos:", lista_sin_repetidos)


""""5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada. """

estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]
print("Estos son los estudiantes de su lista:", estudiantes)
accion = input("""¿Desea agregar (A) o eliminar (E) un estudiante?. 
De otra manera presione cualquier otra tecla para salir """).lower()

if accion == "a":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"""{nuevo_estudiante} ha sido agregado a la lista.
Lista actualizada de estudiantes: {estudiantes}""")

elif accion == "e":
    estudiante_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")

    if estudiante_eliminar in estudiantes:
        estudiantes.remove(estudiante_eliminar)
        print(f"""{estudiante_eliminar} ha sido eliminado de la lista.
Lista actualizada de estudiantes: {estudiantes}""")
        
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Saliendo...")

""""6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero)."""

numeros = [10, 20, 30, 40, 50, 60, 70]
rotado = [numeros[-1]] + numeros[:-1]
print("Lista original:", numeros)
print("Lista rotada una posición a la derecha:", rotado)

""""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica. """

temperaturas = [[15, 25],  # Lunes
    [17, 27],  # Martes
    [14, 22],  # Miércoles
    [16, 26],  # Jueves
    [18, 28],  # Viernes
    [19, 30],  # Sábado
    [20, 29]]  # Domingo

suma_minimas = 0
suma_maximas = 0
amplitud = 0
mayor_amplitud = 0
dia = 0

for i, temp in enumerate(temperaturas, start=0):
    suma_minimas += temp[0]
    suma_maximas += temp[1]
    amplitud = temp[1] - temp[0]

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia = i

prom_minimas = suma_minimas / len(temperaturas)
prom_maximas = suma_maximas / len(temperaturas)

print(f"Promedio de las temperaturas mínimas: {prom_minimas}")
print(f"Promedio de las temperaturas máximas: {prom_maximas}")
print(f"El día de mayor amplitud fue el día {dia}")


""""8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia. """

notas_estudiantes = [
    [8, 7.5, 9],    # Estudiante 1
    [6, 8, 7],      # Estudiante 2
    [9, 9.5, 8],    # Estudiante 3
    [7, 6.5, 7.5],  # Estudiante 4
    [10, 9, 9.5]    # Estudiante 5
]
suma_materia_1 = 0
suma_materia_2 = 0
suma_materia_3 = 0

for i, notas in enumerate(notas_estudiantes):
    suma_notas = sum(notas)
    promedio = suma_notas / len(notas)
    suma_materia_1 += notas[0]
    suma_materia_2 +=  notas[1]
    suma_materia_3 += notas[2]
    print(f"Promedio del Estudiante {i + 1}: {promedio}")

promedio_materia_1 = suma_materia_1 / 5
promedio_materia_2 = suma_materia_2 / 5
promedio_materia_3 = suma_materia_3 / 5

print(f"Promedio de la Materia 1: {promedio_materia_1}")
print(f"Promedio de la Materia 2: {promedio_materia_2}")
print(f"Promedio de la Materia 3: {promedio_materia_3}")

"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada. """

ta_te_ti = [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

for fila in ta_te_ti:
    print(fila)

fila = int(input("Jugador 1 (X), ingrese la fila (1, 2, 3): "))
columna = int(input("Jugador 1 (X), ingrese la columna (1, 2, 3): "))

ta_te_ti[fila - 1][columna - 1] = "X"

for fila in ta_te_ti:
    print(fila)

fila = int(input("Jugador 2 (O), ingrese la fila (1, 2, 3): "))
columna = int(input("Jugador 2 (O), ingrese la columna (1, 2, 3): "))
ta_te_ti[fila - 1][columna - 1] = "O"
for fila in ta_te_ti:
    print(fila)

"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana. """

ventas = [
    [150, 200, 250, 300, 350, 400, 450],  # Producto 1
    [100, 150, 200, 250, 300, 350, 400],  # Producto 2
    [200, 250, 300, 350, 400, 450, 500],  # Producto 3
    [50, 100, 150, 200, 250, 300, 350]    # Producto 4
]
ventas_dia = 0
ventas_producto_1 = sum(ventas[0])
ventas_producto_2 = sum(ventas[1])
ventas_producto_3 = sum(ventas[2])
ventas_producto_4 = sum(ventas[3])
total_por_dia = []
for d in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][d]
    total_por_dia.append(suma_dia)

ventas_dia = max(total_por_dia)
dia = total_por_dia.index(ventas_dia) + 1

mayor_venta = max(ventas_producto_1, ventas_producto_2, ventas_producto_3, ventas_producto_4)

print(f"Total vendido del Producto 1: {ventas_producto_1}")
print(f"Total vendido del Producto 2: {ventas_producto_2}")
print(f"Total vendido del Producto 3: {ventas_producto_3}")
print(f"Total vendido del Producto 4: {ventas_producto_4}")
if mayor_venta == ventas_producto_1:
    print("El producto más vendido en la semana fue el Producto 1")
elif mayor_venta == ventas_producto_2:
    print("El producto más vendido en la semana fue el Producto 2")
elif mayor_venta == ventas_producto_3:
    print("El producto más vendido en la semana fue el Producto 3")
elif mayor_venta == ventas_producto_4:
    print("El producto más vendido en la semana fue el Producto 4")
print(f"El día con mayores ventas totales fue el día {dia} con un total de {ventas_dia}")


