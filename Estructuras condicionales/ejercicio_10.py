"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. """

hemisferio = input("Ingrese su hemisferio (N/S): ")

mes = int(input("Ingrese el mes (1-12): "))

dia = int(input("Ingrese el día (1-31): "))

if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha inválida")
elif hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes == 1) or(mes == 2) or (mes == 3 and dia < 21):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):
        print("Verano")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        print("Otoño")
    else:
            print("Fecha inválida")
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):
        print("Invierno")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        print("Primavera")
    elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        print("Otoño")
    else:
        print("Fecha inválida")
else:
    print("Hemisferio inválido")