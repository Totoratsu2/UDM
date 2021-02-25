from entidades import Juego, AppStore

appStore = AppStore("Juegos UDM")
JUEGOS = [
    Juego("Rompecabezas1", 15.7, "puzzle  ", 3500),
    Juego("Fifa", 55.1, "deportes", 18902),
    Juego("Pes", 35.7, "deportes", 35000),
    Juego("CallofDuty", 45.66, "accion  ", 65000),
    Juego("Multicabezas", 19.99, "puzzle  ", 8500)
]


def continuar() -> bool:
    flag = input("\nDesea continuar? [S,n]: ")

    return True if flag.lower() == "s" else False


def menu() -> int:
    opt = 0
    while opt not in range(1, 7):
        print("\n===== MENU DE OPCIONES =====")
        print("1. Comprar licencias de un juego")
        print("2. Vender licencias de un juego")
        print("3. Consultar el juego más vendido")
        print("4. Visualizar info detallada de cada juego")
        print("5. Consultar los descuentos aplicados por un volumen de compra")
        print("6. Salir")

        opt = int(input("\nIngrese una opción: "))

        if opt not in range(1, 7):
            print("\nERROR: OPCIÓN NO VÁLIDA")

    return opt


def main():
    for juego in JUEGOS:
        appStore.agregarJuego(juego)

    opcion = 0
    while opcion != 6:
        opcion = menu()

        if opcion == 1:
            print(">>> Comprar licencias de un juego")

            appStore.mostrarJuegos()
            seleccion = list(map(int, input("<<< Comprar licencias (ejm: 1,2,3): ").rstrip().split(",")))
            factura = appStore.comprar(seleccion)

            if factura is not None:
                print("\tTotal a pagar:", str(factura) + "$")

            if not continuar():
                break

            print("\n")
        elif opcion == 2:
            print(">>> Vender licencias de un juego")

            appStore.mostrarJuegos()
            seleccion = list(map(int, input("<<< Vender licencias (ejm: 1,2,3): ").rstrip().split(",")))
            factura = appStore.vender(seleccion)

            if factura is not None:
                print("\tTotal a devolver:", str(factura) + "$")

            if not continuar():
                break

            print("\n")
        elif opcion == 3:
            print(">>> Consultar el juego más vendido")

            mas_vendido, index = appStore.masVendido()
            if mas_vendido is not None:
                mas_vendido.masInfo(index)
            else:
                print("\tNo se han vendido licencias")

            if not continuar():
                break

            print("\n")
        elif opcion == 4:
            for i, juego in enumerate(appStore.lista_juegos):
                juego.masInfo(i)

            if not continuar():
                break

            print("\n")
        elif opcion == 5:
            print(">>> Consultar los descuentos aplicados por un volumen de compra")

            print("\t1. Al menos 25 licencias de juegos de rompecabezas sin importar la cantidad de")
            print("\tjuegos que solicite de otras categorías, se dará el 20% de descuento sobre el")
            print("\tvalor total del pedido.\n")

            print("\t2. Si el comprador solicita al menos 20 licencias de juegos de deportes y 15")
            print("\tlicencias de juegos de acción, se dará el 15% de descuento sobre el valor")
            print("\ttotal del pedido.\n")

            print("\tSi en una compra se cumplen ambas condiciones, sólo se aplica la primera promoción que aplique.")

            if not continuar():
                break

            print("\n")


if __name__ == "__main__":
    main()
