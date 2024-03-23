n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa segundo numero: ")
operacion = input(
    "Que operacion deseas realizar? 1-para suma 2-para resta, 3-para multiplicacion 4-para division: ")


n1 = int(n1)
n2 = int(n2)
operacion = int(operacion)

if operacion == 1:
    print("el resultado es: " + str(n1 + n2))

if operacion == 2:
    print("el resultado es: " + str(n1 - n2))

if operacion == 3:
    print("el resultado es: " + str(n1 * n2))

if operacion == 4:
    print("el resultado es: " + str(n1 / n2))
