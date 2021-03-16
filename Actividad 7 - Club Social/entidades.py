from typing import List


class Factura:
    def __init__(self, concepto: str, nombre: str, valor: float):
        self.concepto = concepto
        self.nombre = nombre
        self.valor: float = valor

    def __str__(self):
        return self.concepto+" $"+str(self.valor)

    def pagar(self):
        return "Valor a pagar: " + str(self.valor)+"$"


class Socio:
    def __init__(self, nombre: str, cedula: int, autorizados=None, facturas=None):
        if facturas is None:
            facturas = []
        if autorizados is None:
            autorizados = []

        self.nombre: str = nombre
        self.cedula: int = cedula

        self.autorizados: List[str] = autorizados

        self.facturas: List[Factura] = facturas

    def __str__(self):
        return self.nombre+"    C.C "+str(self.cedula)

    def autorizar(self, nombre: str):
        self.autorizados.append(nombre)

        return "\t" + nombre + " fue autorizado"

    def pagarFactura(self, concepto: str):
        resultado = "Error: Factura no encontrada"

        for factura in self.facturas:
            if factura.concepto == concepto:
                resultado = factura.pagar()
                self.facturas.remove(factura)

        return resultado

    def consumir(self, concepto: str, valor: float):
        factura = Factura(concepto, self.nombre, valor)

        self.facturas.append(factura)

    def verFacturas(self):
        for (i, factura) in enumerate(self.facturas):
            print("\t"+str(i), factura)


class Club:
    def __init__(self):
        self.socios: List[Socio] = []

    def afiliarSocio(self, socio: Socio):
        self.socios.append(socio)
