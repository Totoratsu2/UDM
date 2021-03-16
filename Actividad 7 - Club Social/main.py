from entidades import *

SOCIOS = [
    Socio("Nixon", 1),
    Socio("Juan", 2),
    Socio("Samuel", 3)
]
CLUB = Club()


def continuar() -> bool:
    flag = input("\nDesea continuar? [S,n]: ")

    return False if flag.lower() == "n" else True


def menu() -> int:
    opt = 0
    while opt not in range(1, 7):
        print("\n===== MENU DE OPCIONES =====")
        print("1. Registrar una persona autorizada por un socio")
        print("2. Pagar una factura")
        print("3. Afiliar un socio al club")
        print("4. Registrar un consumo en la cuenta de un socio")
        print("5. Ver socios")
        print("6. Salir")

        try:
            opt = int(input("\nIngrese una opción: "))

            if opt not in range(1, 8):
                print("\nERROR: OPCIÓN NO VÁLIDA")
        except:
            print("\nERROR: OPCIÓN NO VÁLIDA")

    return opt


def main():
    opcion = 0
    while opcion != 6:
        opcion = menu()

        if opcion == 1:
            print(">>> Registrar una persona autorizada por un socio")

            cedula = int(input("<<< Ingrese la cedula del socio: "))
            _socio = None
            for s in CLUB.socios:
                if s.cedula == cedula:
                    _socio = s
            if _socio is None:
                print("ERROR: Socio no encontrado\n")
                continue

            nombre = input("<<< Ingrese el nombre del autorizado: ")

            print("\t"+_socio.autorizar(nombre))

            if not continuar():
                break

            print("\n")
        elif opcion == 2:
            print(">>> Pagar una factura")

            cedula = int(input("<<< Ingrese la cedula del socio: "))
            _socio = None
            for s in CLUB.socios:
                if s.cedula == cedula:
                    _socio = s
            if _socio is None:
                print("ERROR: Socio no encontrado\n")
                continue

            _socio.verFacturas()
            indexFactura = int(input("<<< Ingresar indice de la factura: "))
            if indexFactura < 0 or indexFactura >= len(_socio.facturas):
                print("ERROR: Factura no encontrada\n")
                continue

            print("\t"+_socio.facturas[indexFactura].pagar())

            if not continuar():
                break

            print("\n")
        elif opcion == 3:
            print(">>> Afiliar un socio al club")

            nombre = input("<<< Ingrese el nombre: ")
            cedula = int(input("<<< Ingrese la cedula del socio: "))
            _socio = None
            for s in CLUB.socios:
                if s.cedula == cedula:
                    _socio = s
            if _socio is not None:
                print("ERROR: Socio con esa cedula ya existe\n")
                continue

            _socio = Socio(nombre, cedula)
            CLUB.afiliarSocio(_socio)

            if not continuar():
                break

            print("\n")
        elif opcion == 4:
            print(">>> Registrar un consumo en la cuenta de un socio")

            cedula = int(input("<<< Ingrese la cedula del socio: "))
            _socio = None
            for s in CLUB.socios:
                if s.cedula == cedula:
                    _socio = s
            if _socio is None:
                print("ERROR: Socio no encontrado\n")
                continue

            concepto = input("<<< Ingrese el concepto: ")
            valor = float(input("<<< Ingrese el valor: "))

            _socio.consumir(concepto, valor)

            if not continuar():
                break

            print("\n")
        elif opcion == 5:
            print(">>> Ver socios")

            for (i, _socio) in enumerate(CLUB.socios):
                print("\t"+str(i), _socio)

            if not continuar():
                break

            print("\n")


if __name__ == '__main__':
    for socio in SOCIOS:
        CLUB.afiliarSocio(socio)

    main()
