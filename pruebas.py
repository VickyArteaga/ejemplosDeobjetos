class Antena(object):
    color = ""
    longitud = ""

class Pelo(object):
    color = ""
    textura = ""

class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""

class Objeto(object):
    color = "verde"
    tamanio = "12"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        return "floto"

class Dedo(object):
    longitud = "12"
    forma = "rara"
    color = "azul"

    def tener(self):
        return "tengo dedos"

class Pie(object):
    forma = "churro"
    color = "verde"
    dedos = Dedo()

    def amputar(self):
        return "te he cortado el pie"

# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()

    def saltar(self):
        return "yo salto muy lejos"

