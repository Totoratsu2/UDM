from random import randint


class Socio:

    def __init__(self, nombre: str, telefono: int):
        self.nombre: str = nombre
        self.telefono: int = telefono

        self.ahorro: list[float] = [0] * 12
        self.boleto_rifa = randint(1, 999)
        self.prestamo: list = [0, [0, 0]]  # Valor y fecha en la que se pidio el prestamo

    def __str__(self):
        return self.nombre + " " + str(self.telefono)

    def info(self):
        print("\t" + str(self))
        print("\t\tAhorros:", self.ahorro)
        print("\t\tBoleto:", self.boleto_rifa)


class Natillera:

    def __init__(self, socios: list[Socio], aporte: float):
        self.socios: list[Socio] = socios
        self.aporte_mensual: float = aporte

        self.dinero_rifa: float = 0.0
        self.arcas: float = 0.0
        self.historial_aportes: list[float] = [0.0] * 11

    def obtenerSocio(self) -> Socio:
        for (i, socio) in enumerate(self.socios):
            print("\t" + str(i), socio)

        index = int(input("<<< Seleccionar indice del socio: ").strip())
        if index < 0 or index >= len(self.socios):
            print("ERROR: Indice invalido")
            return None

        return self.socios[index]

    def rifa(self) -> (Socio, float):
        boleto_ganador = randint(1, 999)

        for socio in self.socios:
            if socio.boleto_rifa == boleto_ganador:
                premio = self.dinero_rifa
                socio.ahorro[-1] += premio
                self.dinero_rifa = 0.0

                return socio, premio

        self.arcas += self.dinero_rifa
        self.dinero_rifa = 0.0

        return None, None

    def liquidar(self) -> (float, float):
        intereses = [
            mes + mes * 0.01 for mes in self.historial_aportes
        ]

        return sum(intereses), self.arcas
