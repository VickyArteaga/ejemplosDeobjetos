"""vicky arteaga"""
"""Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi" """


class Cadena(object):

    #cadenaInvertida = ""

    def laCadenaEs(self):
        return "mi diario python"

    def invertirCadena(self, cadena):
        cadenaInvertida = cadena.split(" ")
        return cadenaInvertida[2] + " " + cadenaInvertida[1] + " " + cadenaInvertida[0]


"""-----------------------------------------------
    def invertirCadena(self, cadena):
        cadenaInvertida = cadena.split(" ")

        texto1 = str(cadenaInvertida[2])
        texto2 = str(cadenaInvertida[1])
        texto3 = str(cadenaInvertida[0])
        textoFinal = texto1 + " " + texto2 + " " + texto3
        return textoFinal"""


"""--------------------------------------------
 def invertirCadena(self, cadena):
        lista = cadena.split(" ")
        print(lista)
        listaInvertida = lista.reverse()
        print(listaInvertida)
        return listaInvertida"""