from pruebas import *

# et = Objeto()
# print(et.color)
# print(et.tamanio)
# print(et.aspecto)
# et.color = "rosa"
# print(et.color)

print("-----------------OBJETO 1")
miObjeto = Objeto()
print(miObjeto.tamanio)
miObjeto.aspecto = "Guapo"
print(miObjeto.aspecto)
miVariable = miObjeto.flotar()
print(miVariable)
print(miObjeto.flotar())

print("-----------------OBJETO 2")

miObjeto2 = NuevoObjeto()
print(miObjeto2.pie.color)
miObjeto2.pie.color = "rojo"
print(miObjeto2.pie.color)
miVariable2 = miObjeto2.pie.amputar()
print(miVariable2)
print(miObjeto2.pie.amputar())

print("-----------------OBJETO 2.1")

miObjeto2 = NuevoObjeto()
print(miObjeto2.pie.dedos.color)
miObjeto2.pie.dedos.color = "rojo"
print(miObjeto2.pie.dedos.color)
miVariable2 = miObjeto2.pie.amputar()
print(miVariable2)
print(miObjeto2.pie.amputar())
print(miObjeto2.saltar())
