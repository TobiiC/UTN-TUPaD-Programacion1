"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. """

edad_usuario = int(input("Por favor, ingrese su edad: "))

if edad_usuario < 12:
    print("Niño/a")
elif 12 <= edad_usuario < 18:
    print("Adolescente")
elif 18 <= edad_usuario < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")