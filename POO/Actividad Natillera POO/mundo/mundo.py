from random import randint
from typing import List

from error.exepciones import IndiceInvalido, AporteInvalido, PrestamoInvalido, CantidadDineroInvalida
from mundo.funciones import verificarFecha, obtenerInteres


class Fecha:
    """Clase para manejar de una manera mas ordenada las fechas.

        Attributes:
            dia: Entero comprendido en el rango [1, 31]
                 que expresa la cantidad de dias.
            mes: Entero comprendido en el rango [1, 12]
                 que expresa la cantidad de meses.
    """

    def __init__(self, dia: int, mes: int):
        d, m = verificarFecha(f'{dia}/{mes}')

        self.dia: int = d
        self.mes: int = m


class Socio:
    """Clase de los socios de la natillera.

        Attributes:
            nombre     : Nombre del socio.
            telefono   : Numero de telefono del socio.
            ahorro     : Lista que guarda un registro de los ahorros
                         del socio durante el año de la natillera.
            boleto_rifa: Boleto asignado del socio para las rifas.
            prestamo   : Valor del prestamo pedido por el socio y la
                         fecha en la que se pidio.
    """

    def __init__(self, nombre: str, telefono: int):
        self.nombre: str = nombre
        self.telefono: int = telefono

        self.ahorro: List[float] = [0] * 12
        self.boleto_rifa = randint(1, 999)
        self.prestamo: list = [0, Fecha(1, 1)]  # Valor y fecha en la que se pidio el prestamo

    def __str__(self) -> str:
        return self.nombre + " " + str(self.telefono)

    def info(self):
        """Imprimir la informacion detallada del socio."""

        print("\t" + str(self))
        print("\t\tAhorros:", self.ahorro)
        print("\t\tBoleto:", self.boleto_rifa)

    def ingresarAporte(self, aporte_mensual: float) -> (float, Fecha, float):
        """Ingresar a la natillera el nuevo aporte de un socio.

        Args:
            aporte_mensual: Cantidad minima de dinero que se tiene que pagar
                            en un aporte.

        Returns:
            rifa   : Cantidad de dinero que se ira para el fondo de rifas.
            fecha  : Fecha en la que se ingreso el aporte.
            factura: Cantidad neta de dinero aportado por el socio.
        """

        fechas_raw = [
            input("<<< Ingrese la fecha actual (d/m): "),
            input("<<< Ingrese la fecha de pago (d/m): ")
        ]
        d1, m1 = verificarFecha(fechas_raw[0])
        d2, m2 = verificarFecha(fechas_raw[1])
        fecha1 = Fecha(d1, m1)
        fecha2 = Fecha(d2, m2)

        aporte = float(input("<<< Ingrese aporte del socio: ").strip())
        if aporte < aporte_mensual:
            raise AporteInvalido(aporte)

        factura = aporte + aporte * obtenerInteres([fecha1, fecha2])
        rifa = factura * 0.05

        print("\tTotal del aporte de este mes:", str(factura) + "$")

        self.ahorro[fecha1.mes - 1] = factura

        return rifa, fecha1, factura

    def pedirPrestamo(self) -> (float, int):
        """Pedir un prestamo a la natillera.

        Returns:
            prestamo: Cantidad de dinero que el socio pidio.
            mes     : Mes en el cual el socio pidio el prestamo.
        """

        d, m = verificarFecha(input("<<< Ingrese la fecha actual (d/m): "))
        fecha = Fecha(d, m)

        prestamo = float(input("<<< Ingrese valor del prestamo: ").strip())
        if prestamo > sum(self.ahorro) / 2:
            raise PrestamoInvalido(prestamo)

        print("\tPrestamo por", str(prestamo) + "$ aprobado")

        self.prestamo = [prestamo, fecha]
        self.ahorro[-1] -= prestamo

        return prestamo, fecha.mes

    def pagarPrestamo(self) -> (float, Fecha):
        """Se paga un prestamo pedido a la natillera anteriormente.

        Returns:
            factura: Valor del prestamo + intereses a pagar.
            fecha  : Fecha en la cual se pago el prestamo.
        """

        d, m = verificarFecha(input("<<< Ingrese la fecha actual (d/m): "))
        fecha = Fecha(d, m)

        interes = obtenerInteres([self.prestamo[1], fecha], False)
        factura = self.prestamo[0] + self.prestamo[0] * interes
        print("\tTotal a pagar por el prestamo es:", str(factura) + "$")

        self.ahorro[fecha.mes - 1] += factura

        return factura, fecha

    def liquidar(self, arcas: float, dinero: float):
        """Se liquida el dinero al socio y se muestra lo liquidado.

        Args:
            arcas : Dinero sobrante de la natillera para repartir.
            dinero: Dinero guardado durante el año en la natillera.
        """

        porcentaje = sum(self.ahorro) / dinero

        print("\t" + str(self))
        print("\t\tAhorro:", str(sum(self.ahorro)) + "$")
        print("\t\tDinero entregado de las arcas:", str(arcas * porcentaje) + "$")
        print("\t\tTotal:", str(sum(self.ahorro) + arcas * porcentaje) + "$")


class Natillera:
    """Clase para la natillera.

    Attributes:
        socios           : Lista con los socios participantes en la natillera.
        aporte_mensual   : Cantidad minima a aportar por mes.
        dinero_rifa      : Dinero guardado para las rifas mensuales.
        arcas            : Dinero guardado de rifas sin ganadores e intereses
                           obtenidos del banco.
        historial_aportes: Lista con el total de dinero recaudado por mes.
    """

    def __init__(self, socios: List[Socio], aporte: float):
        self.socios: List[Socio] = socios
        self.aporte_mensual: float = aporte

        self.dinero_rifa: float = 0.0
        self.arcas: float = 0.0
        self.historial_aportes: List[float] = [0.0] * 11

    def obtenerSocio(self) -> Socio:
        """Obtener un socio seleccionandolo por indice.

        Returns:
            socio: Socio seleccionado.
        """

        for (i, socio) in enumerate(self.socios):
            print("\t" + str(i), socio)

        index = int(input("<<< Seleccionar indice del socio: ").strip())
        if index < 0 or index >= len(self.socios):
            raise IndiceInvalido(index)

        return self.socios[index]

    def rifa(self) -> (Socio, float):
        """Realizar rifa mensual.

        Returns:
            ganador: Socio que se gano el dinero rifado.
            premio : Dinero que se lleva el ganador.
        """

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
        """Liquidar los ahorros de los socios y darles parte del dinero en las arcas.

        Returns:
            dinero: Total del dinero recaudado por los socios.
            arcas : Dinero a repartir con los socios.
        """

        intereses = [
            mes + mes * 0.01 for mes in self.historial_aportes
        ]
        dinero = sum(intereses)

        if dinero < 1:
            raise CantidadDineroInvalida(dinero)

        return dinero, self.arcas

    def mostrarBoletos(self):
        """Mostrar los socios y sus boletos de la rifa."""

        for (i, socio) in enumerate(self.socios):
            print("\t" + str(i), socio)
            print("\t\tBoleto:", socio.boleto_rifa)