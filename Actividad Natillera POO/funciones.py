def verificarFecha(fecha: str) -> (bool, list[int]):
    dm = list(map(int, fecha.rstrip().split("/")))  # Lista [dia,mes]

    if (dm[0] > 30 or dm[0] < 1) or (dm[1] > 11 or dm[1] < 1):
        return True, None
    return False, dm


def obtenerInteres(fechas: list[list[int]], interes_dias=True) -> float:
    if interes_dias:  # Interes atraso del aporte mensual
        dias = [  # Se toma como si todos los meses tuvieran 30 dias para ahorrar tiempo
            (fecha[0] + (fecha[1] * 30)) for fecha in fechas
        ]
        diff = dias[1] - dias[0]

        if diff > 0: # No hay intereses
            return 1.0
        else:
            return 0.01 * abs(diff)
    else:  # Interes pago de prestamo
        return 0.02 * abs(fechas[1][1] - fechas[0][1])


def continuar() -> bool:
    flag = input("\nDesea continuar? [S,n]: ")

    return False if flag.lower() == "n" else True


def menu() -> int:
    opt = 0
    while opt not in range(1, 8):
        print("\n===== MENU DE OPCIONES =====")
        print("1. Ingresar aporte de un socio")
        print("2. Rifa")
        print("3. Pedir prestamo")
        print("4. Pagar un prestamo")
        print("5. Terminar natillera (liquidar)")
        print("6. Informacion Socios")
        print("7. Salir")

        try:
            opt = int(input("\nIngrese una opción: "))

            if opt not in range(1, 8):
                print("\nERROR: OPCIÓN NO VÁLIDA")
        except:
            print("\nERROR: OPCIÓN NO VÁLIDA")

    return opt