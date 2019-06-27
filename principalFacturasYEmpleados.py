from facturas import *
from empleado import *
compra1 = Factura(12, 110)   # 12 unidad, 110 precio
print(compra1.unidad)
print(compra1.precio)
print(compra1. a_pagar(), "euros")
#print(compra1.__tasa)
    # Error:
    # AttributeError: type object 'Factura' has no attribute'__tasa'

empleado1 = Empleado("Francisco", 30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco Jose")
print(empleado1.getnombre())
print(empleado1.getnombre(),", ",empleado1.getsalario())



