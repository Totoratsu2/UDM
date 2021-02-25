class Juego:
    def __init__(self, nombre: str, costo: float, categoria: str, tamano: float, licencias: int = 0):
        self.nombre: str = nombre
        self.costo: float = costo
        self.categoria: str = categoria
        self.tamano: float = tamano
        self.licencias: int = licencias

    def Imprimir(self, i: int):
        print("\t", i, self.categoria + "\t", str(self.costo) + "$\t", self.nombre)

    def masInfo(self, i: int):
        print("\t" + str(i), self.categoria, self.nombre)
        print("\t\tValor:", str(self.costo) + "$")
        print("\t\tPeso:", str(self.tamano) + "KB")
        print("\t\tLicencias vendidas:", self.licencias)


class AppStore:
    lista_juegos: list[Juego] = []

    def __init__(self, nombre: str):
        self.nombre: str = nombre

    def agregarJuego(self, obj: Juego):
        self.lista_juegos.append(obj)

    def removerJuego(self, obj: Juego):
        self.lista_juegos.remove(obj)

    def comprar(self, juegos: list[int]) -> float:
        factura = 0.0
        contador_juegos = [0, 0, 0]  # 0: rompecabezas, 1: deportes, 2: accion

        for i in juegos:
            if i >= len(self.lista_juegos) or i < 0:
                print("\tERROR: Juego", i, "no encontrado")
                return
            else:
                juego = self.lista_juegos[i]

                factura += juego.costo
                juego.licencias += 1

                if juego.categoria == "rompecabezas":
                    contador_juegos[0] += 1
                elif juego.categoria == "deportes":
                    contador_juegos[1] += 1
                else:
                    contador_juegos[2] += 1

        # Descuentos
        if contador_juegos[0] >= 25:
            factura -= factura * 0.2
        elif contador_juegos[1] >= 20 and contador_juegos[2] >= 15:
            factura -= factura * 0.15

        return factura

    def vender(self, juegos: list[int]) -> float:
        factura = 0.0

        for i in juegos:
            if i >= len(self.lista_juegos) or i < 0:
                print("\tERROR: Juego", i, "no encontrado")
                return
            else:
                juego = self.lista_juegos[i]

                juego.licencias -= 1
                factura += juego.costo

        return factura

    def masVendido(self) -> Juego:
        mas_vendido = self.lista_juegos[0]
        index = 0

        for i, juego in enumerate(self.lista_juegos):
            if juego.licencias > mas_vendido.licencias:
                mas_vendido = juego
                index = i

        if mas_vendido.licencias == 0:
            return None, None

        return mas_vendido, index

    def mostrarJuegos(self):
        for i, juegos in enumerate(self.lista_juegos):
            juegos.Imprimir(i)
