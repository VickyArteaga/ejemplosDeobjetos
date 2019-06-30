from herencia import *

"""Una vez creadas las clases crearemos a varios
animales:
● flipper un delfín que pesa 1800 kg y le
encanta nadar.
● Chueca una gallina que pesa 1 kilo,
come y pone huevos.
● toby un perro al que le encanta comer,
ladrar pero también correr ¿Donde
pondremos el método correr?
● ¿Se te ocurren nuevos métodos?"""

print("----------------------el delfin ---------------------------")

flipper = Delfin()
print("A Flipper", flipper.nadar())
flipper.setpeso(1800)
print("y pesa ", flipper.getpeso())
print("ademas de ", flipper.saltar(), "muy alto")

print("----------------------la gallina ---------------------------")

chueca = Oviparo()
print("Chueca es una gallina")
chueca.setpeso(1)
print("que pesa", chueca.getpeso(), " kl")
print(chueca.comer(), "y")
print(chueca.poner_huevos())
print("y le gusta", chueca.saltar(), "de rama en rama")

print("----------------------el perro ---------------------------")

print("Tengo un perro llamado Toby")
toby = Perro()
print(toby.comer())
print(toby.ladrar())
print("pero tambien", toby.correr())
#print(toby.color_de_pelo("marron"))
print("y", toby.saltar(), "cuando le lanzo un hueso")





