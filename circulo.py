# vicky arteaga
"""Ejercicio 11
Escribir una clase en python llamada círculo que contenga un radio,
con un método que devuelva el área y otro que devuelva el perímetro del círculo."""


class Circulo(object):

    def area(self, diametro):
        radio = diametro /2
        area = 3.14 * radio**2
        return area

    def perimetro(self, diametro):
        perimetro = 3.14 * diametro
        return perimetro