print("BIENVENIDOS A LA CALCULADORA DE PAGOS MENSUALES POR HORAS DE TRABAJO ")

n1 = input("Ingresa numero de trabajadores : ")
n2 = input("Ingresa pago: ")
promedio = input(""


n1 = int(n1)
n2 = int(n2)
operacion = int(promedio)

if promedio == 1:
    print("el resultado es: " + str(n1 + n2))

if promedio == 2:
    print("el resultado es: " + str(n1 - n2))

if promedio == 3:
    print("el resultado es: " + str(n1 * n2))

if promedio == 4:
    print("el resultado es: " + str(n1 / n2))
