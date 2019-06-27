
# Crea una clase que se llame Persona, tendrá edad y nombre y podrá correr, saltar y
# caminar. Crea a Esteban como objeto de la clase Persona y añadele las propiedades
# correspondientes y los cuando llame a los métodos estos indicarán en una frase que puede hacer
# (correr, saltar...).

# nota: si no pones get and setters y pones solo
# el init con los metodos y funciona
# y sino creas el init y solo le pones nombre y edad como variables
# más los metodos funciona
class Persona(object):
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getnombre(self):
         return self.__nombre

    def getedad(self):
        return self.__edad

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        self.__edad = edad

    def correr(self):
        return "corre muy rapido"

    def saltar(self):
        return "sabe saltar"

    def caminar(self):
        return "cuando camina cojea"