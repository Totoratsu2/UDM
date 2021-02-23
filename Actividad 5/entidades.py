class Juego:
    def __init__(self, nombre: str, costo: float, categoria: str, tamano: float, licencias: int = 0):
        self.nombre: str = nombre
        self.costo: float = costo
        self.categoria: str = categoria
        self.tamano: float = tamano
        self.licencias: int = licencias

    def Imprimir(self):
        print("\t"+self.categoria, self.nombre, self.costo+"$")

    def masInfo(self):
        print("\t"+self.categoria, self.nombre)
        print("\t\tValor:", self.costo)
        print("\t\tPeso:", self.peso+"KB")
        print("\t\tLicencias vendidas:", self.licencias)

class AppStore:
    lista_juegos: list[Juego] = None

    def __init__(self, nombre: str):
        self.nombre: str = nombre

    def agregarJuego(self, obj: Juego):
        self.lista_juegos.append(obj)

    def removerJuego(self, obj: Juego):
        self.lista_juegos.remove(obj)

    def comprar(self, juegos: list[Juego]) -> float:
        factura = 0.0
        contador_juegos = [0 * 3]  # 0: rompecabezas, 1: deportes, 2: accion

        for juego in juegos:
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

    def vender(self, juegos: list[Juego]) -> float:
        factura = 0.0

        for juego in juegos:
            juego.licencias -= 1
            factura += juego.costo

        return factura

    def masVendido(self) -> Juego:
        mas_vendido = self.lista_juegos[0]

        for juego in self.lista_juegos:
            if juego.licencias > mas_vendido.licencias:
                mas_vendido = juego

        return mas_vendido

    def mostrarJuegos(self):
        for juegos in self.lista_juegos:
            juegos.Imprimir()