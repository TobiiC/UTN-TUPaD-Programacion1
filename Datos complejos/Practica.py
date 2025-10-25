""""1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 """

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. """

frutas = list(precios_frutas.keys())
print(frutas)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero de telefono del contacto: ")
    agenda[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in agenda:
    print(f"El numero de {nombre_consulta} es {agenda[nombre_consulta]}")
else:
    print("El contacto no existe en la agenda.")

"""5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. """

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Palabras únicas:", contador_palabras)

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. """
alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print(alumnos)

print("Promedios de los alumnos:")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """
parcial1 = {10, 20, 30, 45}
parcial2 = {30, 45, 60, 70}

ambos_parciales = parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

solo_un_parcial = parcial1 ^ parcial2
print(f"Estudiantes que aprobaron solo uno de los dos: {solo_un_parcial}")

todos_los_estudiantes = parcial1 | parcial2
print(f"Lista total de estudiantes (al menos un parcial): {todos_los_estudiantes}")



"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe."""

stock_productos = { 'Manzanas': 50, 'Bananas': 30, 'Naranjas': 20, 'Leche': 15, 'Pan': 25 }
consulta_stock = input("Ingrese el nombre del producto para consultar su stock: ")
if consulta_stock in stock_productos:
    print(f"El stock de {consulta_stock} es {stock_productos[consulta_stock]}")
    opcion_unidades = input("¿Desea agregar unidades al stock? (si/no): ")
    if opcion_unidades.lower() == 'si':
        unidades_agregar = int(input("Ingrese la cantidad de unidades a agregar: "))
        stock_productos[consulta_stock] += unidades_agregar
        print(f"Nuevo stock de {consulta_stock} es {stock_productos[consulta_stock]}")
    else: 
        print("No se realizaron cambios en el stock.")
else:
    print(f"{consulta_stock} no existe en el stock.")
    opcion_nuevo = input("¿Desea agregar este producto al stock? (si/no): ")
    if opcion_nuevo.lower() == 'si':
        unidades_nuevo = int(input("Ingrese la cantidad de unidades para el nuevo producto: "))
        stock_productos[consulta_stock] = unidades_nuevo
        print(f"{consulta_stock} ha sido agregado al stock con {unidades_nuevo} unidades.")

"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Permití consultar qué actividad hay en cierto día y hora. """

agenda_eventos = {}
while True:

    """Menu de opciones
    1. Agregar evento
    2. Consultar evento"""
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        cantidad_eventos = int(input("¿Cuántos eventos desea agregar?: "))
        if cantidad_eventos > 0:
            for i in range(cantidad_eventos):
                dia = input("Ingrese el día del evento (formato DD/MM): ")
                hora = input("Ingrese la hora del evento (formato HH:MM): ")
                evento = input("Ingrese el nombre del evento: ")
                agenda_eventos[evento] = (dia, hora)
        else:
            print("La cantidad de eventos debe ser mayor a cero.")
    elif opcion == 2:
        evento_consulta = input("Ingrese el nombre del contacto a consultar: ")
        if evento_consulta in agenda_eventos:
            print(f"La fecha y horario de {evento_consulta} es {agenda_eventos[evento]}")
        else:
            print("El evento no existe en la agenda.")
    else:
        print("Opción no válida.")
        break

"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. """

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Perú': 'Lima'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)