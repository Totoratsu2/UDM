from error.exepciones import FechaInvalida


def verificarFecha(fecha: str) -> (int, int):
    """Verifica el formato de una fecha para ver si es valido.

    Args:
        fecha: String que contiene una fecha en el formato dia/mes.

    Returns:
        dia: Entero con el valor del dia de una fecha.
        mes: Entero con el valor del mes de una fecha.
    """

    dm = list(map(int, fecha.rstrip().split("/")))  # Lista [dia,mes]
    if len(dm) != 2:
        raise FechaInvalida([0, 0])

    if not (0 < dm[0] < 32) or not (0 < dm[1] < 13):
        raise FechaInvalida(dm)

    return dm[0], dm[1]


def obtenerInteres(fechas: list, interes_dias=True) -> float:
    """Obtener la cantidad de interes que se tienen que pagar por un prestamo.

    Args:
        fechas      : Lista con las fechas a trabajar.
        interes_dias: Bandera para saber si se va a calcular el interes
                      a partir la diferencia en los dias o por los meses.

    Returns:
        interes: Cantidad de dinero que se tiene que pagar por los
                 intereses.
    """

    if interes_dias:  # Interes atraso del aporte mensual
        dias = [  # Se toma como si todos los meses tuvieran 30 dias para ahorrar tiempo
            (fecha.dia + (fecha.mes * 30)) for fecha in fechas
        ]
        diff = dias[1] - dias[0]

        if diff > 0:  # No hay intereses
            return 1.0
        else:
            return 0.01 * abs(diff)
    else:  # Interes pago de prestamo
        return 0.02 * abs(fechas[1].mes - fechas[0].mes)


def continuar() -> bool:
    flag = input("\nDesea continuar? [S,n]: ")

    if flag.lower() == "n":
        return False

    return True


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
