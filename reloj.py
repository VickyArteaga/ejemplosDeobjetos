# Escribir una clase que represente un Reloj que señale la hora, el minuto y el segundo.
# Podemos poner por defecto los parámetros a 0:0:0 o pasarle la hora, los minutos y los
# segundos.
# ○ Los atributos serán tres enteros: para la hora, los minutos y los segundos.
# ○ Existirá un método que da la hora, que se llamará dame_hora() y la devolverá como
# un objeto string.
# ○ La hora, los minutos y los segundos serán representados en todos los casos con
# valores del tipo int. No obstante, se comprobarán los rangos adecuados (p.e. no
# poner hora 35 horas).

class Reloj (object):
    hora = 0
    minutos = 0
    segundos = 0

    def dame_hora(self):
        return "Son las " + str(self.hora)+":" + str(self.minutos) + ":" + str(self.segundos)

    def comprobar(self, hora ,minutos, segundos):
        if 0 < hora < 23 and 0 < minutos < 60 and 0 < segundos < 60:
            return True
        else:
            return False

    def set_hora(self, hora, minutos, segundos):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos


