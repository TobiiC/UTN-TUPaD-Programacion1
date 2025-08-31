"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

edad_usuario = int(input("Por favor, ingrese su edad: "))

if edad_usuario > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
