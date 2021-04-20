from mundo.mundo import *
from mundo.funciones import *

SOCIOS = [
    Socio("Jose", 31976743612),
    Socio("Raul", 30438171625),
    Socio("David", 31009847273)
]
NATILLERA = Natillera(SOCIOS, 25000.0)


def main():
    opcion = 0
    while opcion != 7:
        opcion = menu()

        try:
            if opcion == 1:
                print(">>> Ingresar aporte de un socio")

                socio = NATILLERA.obtenerSocio()
                rifa, fecha, factura = socio.ingresarAporte(NATILLERA.aporte_mensual)

                NATILLERA.dinero_rifa += rifa
                NATILLERA.historial_aportes[fecha.mes - 1] += factura + rifa

                if not continuar():
                    break
                print("\n")

            elif opcion == 2:
                print(">>> Rifa")

                NATILLERA.mostrarBoletos()
                ganador, premio = NATILLERA.rifa()
                if ganador is None:
                    print("Nadie gano, el dinero ira a las arcas")
                    continue

                print("\tGano el socio:", ganador)
                print("\t\tEl premio fue de", premio, "pesos")

                if not continuar():
                    break
                print("\n")

            elif opcion == 3:
                print(">>> Pedir prestamo")

                socio = NATILLERA.obtenerSocio()
                prestamo, mes = socio.pedirPrestamo()
                NATILLERA.historial_aportes[mes-1] -= prestamo

                if not continuar():
                    break
                print("\n")

            elif opcion == 4:
                print(">>> Pagar un prestamo")

                socio = NATILLERA.obtenerSocio()
                factura, fecha = socio.pagarPrestamo()

                NATILLERA.historial_aportes[fecha.mes-1] += factura

                if not continuar():
                    break
                print("\n")

            elif opcion == 5:
                print(">>> Terminar natillera (liquidar)")

                dinero, arcas = NATILLERA.liquidar()

                for socio in NATILLERA.socios:
                    socio.liquidar(arcas, dinero)

                if not continuar():
                    break
                print("\n")

            elif opcion == 6:
                print(">>> Informacion Socios")

                for socio in NATILLERA.socios:
                    socio.info()

                if not continuar():
                    break
                print("\n")

        except IndiceInvalido:
            print('ERROR: Indice del usuario invalido')
            continue
        except FechaInvalida:
            print('ERROR: La fecha ingresada no es valida')
            continue
        except CantidadDineroInvalida:
            print('ERROR: Dinero insuficiente para realizar la operacion')
            continue
        except PrestamoInvalido:
            print('ERROR: Prestamo invalido, no se puede pedir mas de lo que se a aportado')
            continue
        except AporteInvalido:
            print('ERROR: El aporte ingresado no es valido')
            continue


if __name__ == "__main__":
    main()
