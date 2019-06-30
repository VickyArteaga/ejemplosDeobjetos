"""Basándote en el siguiente esquema de clases crea las respectivas clases con
las herencias correspondientes. Ten en cuenta que el peso es privado y tendrás que
poder acceder a el mismo para cambiarlo."""


class Animal(object):

    __peso = 0

    #def __init__(self, valor): # Primero naces.
    #   self.__peso = valor

    def getpeso(self):
        return self.__peso

    def setpeso(self, valorquequiero):  # Vas cambiando en valor.
        self.__peso = valorquequiero

    def comer(self):
        return "le gusta comer"

    def saltar(self):
        return "saltar"


class Oviparo(Animal):

    def poner_huevos(self):
        return ("pone huevos")


class Mamifero(Animal):

    sangre_caliente = True

    def parir(self):
        return "Parir"

    def amamantar(self):
        return "amantar"


class Delfin(Mamifero):
    def nadar(self):
        return "Le encanta nadar"


class Perro(Mamifero):
    color_de_pelo = ""

    def ladrar(self):
        return "ladrar"

    def correr(self):
        return "corre"

