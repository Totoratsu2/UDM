from entidades import *
from funciones import *

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

        if opcion == 1:
            print(">>> Ingresar aporte de un socio")

            socio = NATILLERA.obtenerSocio()
            if socio is None:
                continue

            fechas_raw = [
                input("<<< Ingrese la fecha actual (d/m): "),
                input("<<< Ingrese la fecha de pago (d/m): ")
            ]
            err1, fecha1 = verificarFecha(fechas_raw[0])
            err2, fecha2 = verificarFecha(fechas_raw[1])
            if err1 or err2:
                print("ERROR: Fecha invalida")
                continue

            aporte = float(input("<<< Ingrese aporte del socio: ").strip())
            if aporte < NATILLERA.aporte_mensual:
                print("ERROR: El aporte es menor al minimo establecido")
                continue

            factura = aporte + aporte * obtenerInteres([fecha1, fecha2])
            rifa = factura * 0.05

            print("\tTotal del aporte de este mes:", str(factura)+"$")

            socio.ahorro[fecha1[1]-1] = factura
            NATILLERA.dinero_rifa += rifa
            NATILLERA.historial_aportes[fecha1[1]-1] += factura + rifa

            if not continuar():
                break

            print("\n")
        elif opcion == 2:
            print(">>> Rifa")

            for (i, socio) in enumerate(NATILLERA.socios):
                print("\t"+str(i), socio)
                print("\t\tBoleto:", socio.boleto_rifa)

            ganador, premio = NATILLERA.rifa()
            if ganador is None:
                print("Nadie gano, el dinero ira a las arcas")

                if not continuar():
                    break

                print("\n")

                continue

            print("\tGano el socio:", ganador)
            print("\t\tEl premio fue de", premio, "pesos")

            if not continuar():
                break

            print("\n")
        elif opcion == 3:
            print(">>> Pedir prestamo")

            socio = NATILLERA.obtenerSocio()
            if socio is None:
                continue

            err, fecha = verificarFecha(input("<<< Ingrese la fecha actual (d/m): "))
            if err:
                print("ERROR: Fecha invalida")
                continue

            prestamo = float(input("<<< Ingrese valor del prestamo: ").strip())
            if prestamo > sum(socio.ahorro)/2:
                print("ERROR: El prestamo no puede ser mayor a la mitad de los ahorros del socio")
                continue

            print("\tPrestamo por", str(prestamo)+"$ aprobado")

            socio.prestamo = [prestamo, fecha]
            socio.ahorro[-1] -= prestamo
            NATILLERA.historial_aportes[fecha[1]-1] -= prestamo

            if not continuar():
                break

            print("\n")
        elif opcion == 4:
            print(">>> Pagar un prestamo")

            socio = NATILLERA.obtenerSocio()
            if socio is None:
                continue

            err, fecha = verificarFecha(input("<<< Ingrese la fecha actual (d/m): "))
            if err:
                print("ERROR: Fecha invalida")
                continue

            interes = obtenerInteres([socio.prestamo[1], fecha], False)
            factura = socio.prestamo[0] + socio.prestamo[0] * interes
            print("\tTotal a pagar por el prestamo es:", str(factura)+"$")

            socio.ahorro[fecha[1]-1] += factura
            NATILLERA.historial_aportes[fecha[1]-1] += factura

            if not continuar():
                break

            print("\n")
        elif opcion == 5:
            print(">>> Terminar natillera (liquidar)")

            dinero, arcas = NATILLERA.liquidar()

            for socio in NATILLERA.socios:
                porcentaje = sum(socio.ahorro)/dinero

                print("\t"+str(socio))
                print("\t\tAhorro:", str(sum(socio.ahorro))+"$")
                print("\t\tDinero entregado de las arcas:", str(arcas*porcentaje)+"$")
                print("\t\tTotal:", str(sum(socio.ahorro) + arcas*porcentaje)+"$")
            
            break
        elif opcion == 6:
            print(">>> Informacion Socios")

            for socio in NATILLERA.socios:
                socio.info()

            if not continuar():
                break

            print("\n")


if __name__ == "__main__":
    main()
