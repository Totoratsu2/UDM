class Error(Exception):
    pass


class FechaInvalida(Error):
    def __init__(self, fecha):
        self.fecha = fecha


class IndiceInvalido(Error):
    def __init__(self, indice):
        self.indice = indice


class AporteInvalido(Error):
    def __init__(self, valor):
        self.valor = valor


class PrestamoInvalido(AporteInvalido):
    pass


class CantidadDineroInvalida(AporteInvalido):
    pass
