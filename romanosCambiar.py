# Ejercicio 1
# Escribir una clase en python que convierta un número entero a número romano

class Romano(object):
    entero = 0
    romano = " "

    def __init__(self, valor): # Primero naces.
        self.entero = valor

    def getentero(self):
        return self.entero

    def setentero(self,valorquequiero): #Vas cambiando en valor.
        self.entero = valorquequiero


    def cambiar(self):
        if self.entero == 10:
            self.romano = "X"
        return self.romano


