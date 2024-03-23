saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola mundo vengance"


def SaludaChanchito():
    saludo = 24
    print(saludo)


print(saludo)
saludar()
print(saludo)
