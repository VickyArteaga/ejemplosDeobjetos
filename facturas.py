class Factura(object):
    __tasa = 19

    def __init__(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio

    def a_pagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura.__tasa/1000
        return total + impuesto



