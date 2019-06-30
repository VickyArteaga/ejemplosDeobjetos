# Ejercicio 1
# Escribir una clase en python que convierta un número entero a número romano

class CambiarAEnteros(object):
    entero = 0
    romano = " "

    def __init__(self, valor): # Primero naces.
        self.romano = valor

    def getentero(self):
        return self.romano

    def setentero(self, valorquequiero): #Vas cambiando en valor.
        self.romano = valorquequiero


    def cambiar(self):
        if self.romano == "I":
            self.entero = 1

        if self.romano == "II":
            self.entero = 2

        if self.romano == "III":
            self.entero = 3

        if self.romano == "IV":
            self.entero = 4

        if self.romano == "V":
            self.entero = 5

        if self.romano == "VI":
            self.entero = 6

        if self.romano == "VII":
            self.entero = 7

        if self.romano == "VIII":
            self.entero = 8

        if self.romano == "IX":
            self.entero = 8

        if self.romano == "X":
            self.entero = 10

        return self.entero