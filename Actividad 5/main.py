from entidades import Juego, AppStore

appStore = AppStore("Juegos UDM")
juegos = [
    Juego("Rompecabezas1", 15.7, "rompecabezas", 3500),
    Juego("Fifa", 55.1, "deportes", 18902),
    Juego("Pes", 35.7, "deportes", 35000),
    Juego("Call of Duty", 45.66, "accion", 65000),
    Juego("Multicabezas", 19.99, "rompecabezas", 8500)
]

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
    for juego in juegos:
        appStore.agregarJuego(juego)

    opcion = 0
    while opcion != 6:
        opcion = menu()

        if opcion == 1:
            print(">>> Comprar licencias de un juego")
            appStore.mostrarJuegos()


if __name__ == "__main__":
    main()

