"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad """

def crear_archivo_inicial():
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,250.0,20\n")
        archivo.write("Mochila,1500.0,10\n")

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: """

def leer_productos():
    with open("productos.txt", "r") as productos:
        for linea in productos:
            nombre, precio, cantidad = linea.strip().split(",")

            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente."""

def agregar_producto():
    while True:
        print("Ingrese un nuevo producto: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        with open("productos.txt", "a") as productos:
            productos.write(f"{nombre},{precio},{cantidad}\n") 

        opcion = input("Desea agregar otro producto? s/n: ").strip().lower()

        if opcion != 's':
            break

"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad."""

def cargar_productos_en_lista():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error. """

def buscar_producto(productos):
    
    if not productos:
        print("La lista está vacía, no se puede buscar.")
        return
            
    producto_buscar = input("Ingrese el nombre del producto a buscar: ")
        

    encontrado = False 
    for producto in productos:
        if producto["nombre"].lower() == producto_buscar.lower():
            print(f"Producto encontrado: Nombre: {producto['nombre']} Precio: ${producto['precio']} Cantidad: {producto['cantidad']}")
            encontrado = True
            break
        elif not encontrado:
            print(f"Producto '{producto_buscar}' no encontrado.")

"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista. """

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

    print("Archivo actualizado.")

# Ejecución de las funciones

crear_archivo_inicial()
leer_productos()
agregar_producto()

productos = cargar_productos_en_lista()

for producto in productos:
    print(producto)

buscar_producto(productos)
guardar_productos(productos)







