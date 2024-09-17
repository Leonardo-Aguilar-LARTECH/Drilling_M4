import modules.logics as lg
from modules.classes import *

repetir = False

while not repetir:
    lg.leer_automoviles()
    repetir = lg.ingreso_vehiculos()
    if repetir:
        salida = input("desea continuar (s)?")
        if salida.lower() == "s":
            repetir = False
        else:
            lg.clear_screen()
            lg.imprimir_automoviles()
            lg.guardar_automoviles()
            repetir = True