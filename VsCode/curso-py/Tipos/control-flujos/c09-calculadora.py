print("bienvenidos a la calculadora")
print("para salir escribe salir")
print("las operaciones son suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese Número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operación no Válida")
        break
    print(f"El resultado es {resultado}")
