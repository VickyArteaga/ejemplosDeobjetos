from persona import *
from reloj import *

# Crea una clase que se llame Persona, tendrá edad y nombre y podrá correr, saltar y
# caminar. Crea a Esteban como objeto de la clase Persona y añadele las propiedades
# correspondientes y los cuando llame a los métodos estos indicarán en una frase que puede hacer
# (correr, saltar...).

print("--------Ejercicio clase persona que se llama Esteban----------")
miPersona = Persona("Esteban", 19)
print(miPersona.getnombre(), miPersona.getedad())
print(miPersona.getnombre(), miPersona.saltar())
print(miPersona.getnombre(), miPersona.caminar())
print(miPersona.getnombre(), miPersona.correr())

# Escribir una clase que represente un Reloj que señale la hora, el minuto y el segundo.
# Podemos poner por defecto los parámetros a 0:0:0 o pasarle la hora, los minutos y los
# segundos.
# ○ Los atributos serán tres enteros: para la hora, los minutos y los segundos.
# ○ Existirá un método que da la hora, que se llamará dame_hora() y la devolverá como
# un objeto string.
# ○ La hora, los minutos y los segundos serán representados en todos los casos con
# valores del tipo int. No obstante, se comprobarán los rangos adecuados (p.e. no
# poner hora 35 horas).

print("-------clase reloj que da la hora---------")

relojito = Reloj()
comprueba = False
while comprueba == False:
    hora = int(input("Dame la hora: "))
    minutos = int(input("Dame los minutos: "))
    segundos = int(input("Dame los segundos: "))
    if relojito.comprobar(hora,minutos,segundos)==True:
        comprueba=True


relojito.set_hora(hora,minutos,segundos)
print(relojito.dame_hora())
