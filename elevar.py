#autor: vicky arteaga
"""Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente

Entrada: pow(2, -3)
Salida: 0.125

Entrada: pow(3, 5)
Salida: 243"""

class Calcule(object):

    resultado1 = 0
    valor1 = 0
    valor2 = 0

    def elevar(self, valor1, valor2):
        resultado1 = pow(valor1, valor2)
        return resultado1

