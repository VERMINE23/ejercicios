print("BIENVENIDOS A LA CALCULADORA DE PAGOS MENSUALES POR HORAS DE TRABAJO ")

trabajadores = int(input("Introduce cantidad de trabajadores: "))


sueldo = 0
dias = 30


for i in range(trabajadores):
    hora = float(
        input(f"Introduce lasa horas de trabajo para el trabajador numero {i + 1}: "))

    paga = float(input(f"Introduce lo que cobra el trabajador {i + 1}: "))

    sueldo = sueldo + (paga * hora * dias)

promedio = sueldo / trabajadores


print("el promedio de dinero del trabajador es  ", promedio)
