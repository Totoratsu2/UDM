from random import randint


class Pago:
    def __init__(self, val: int, pago: list, factura: list):
        self.valor: int = val
        self.fecha_pago: list = pago
        self.fecha_factura: list = factura


class Prestamo:
    def __init__(self, valor: float, fecha: list):
        self.valor: float = valor
        self.fecha: list = fecha

    def cancelar(self, ahorro: float, fecha: list):
        if ahorro < self.valor:
            print('El socio no tiene suficiente dinero para pagar el prestamo')
            return

        dif_mes = abs(fecha[1] - self.fecha[1])

        # Nueva cantidad de dinero del socio despues de cancelar el prestamo
        return ahorro - self.valor - (self.valor*0.02)*dif_mes


class Socio:
    ahorro: list[Pago]
    prestamos: list[Prestamo]
    atraso_pagos: list[list]

    def __init__(self, nombre: str, telefono: int):
        self.nombre: str = nombre
        self.telefono: int = telefono


class Natillera:
    dinero_natillera: float = 0.0
    dinero_rifa: float = 0.0
    liquidacion: float = 0.0
    interes_banco: float = 0.0

    def __init__(self, socios: list[Socio], aporte: float):
        self.socios: list[Socio] = socios
        self.aporte_mensual: float = aporte

    def aporteMensual(self, aportes: list, fecha: list):
        rifa = self.aporte_mensual * 0.05
        aporte_mes = 0.0

        for (aporte, socio) in zip(aportes, self.socios):
            if aporte < self.aporte_mensual:
                if aporte == 0:
                    socio.atraso_pagos.append(fecha)
                    print('El socio', socio.nombre, 'no aporto este mes')
                else:
                    print('El socio', socio.nombre,
                          'dio un aporte menor a', self.aporte_mensual)
            else:
                socio.ahorro -= aporte + rifa
                self.dinero_rifa += rifa
                aporte_mes += aporte

        self.interes_banco += aporte_mes * 0.01 
        self.dinero_natillera += aporte_mes

    def rifa(self):
        boletos = [randint(0, 999) for y in range(len(self.socios))]

        for (socio, boleto) in zip(self.socios, boletos):
            print('El Socio', socio.nombre, 'tiene el boleto n', boleto)

        numero_ganador = boletos.index(randint(0, len(boletos)))

        if numero_ganador == len(boletos):
            self.liquidacion += self.dinero_rifa
            self.dinero_rifa = 0.0

            print('Nadie gano la rifa, el dinero va a la liquidacion')
        else:
            ganador = self.socios[numero_ganador]
            ganador.aportes_natillera += self.dinero_rifa
            self.dinero_rifa = 0.0

            print('El ganador de la rifa es el socio', ganador.nombre)
