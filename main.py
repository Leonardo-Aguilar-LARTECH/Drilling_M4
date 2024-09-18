import modules.logics as lg
from modules.classes import *
import time

repetir = False

lg.leer_automoviles()

while not repetir:
    repetir = lg.ingreso_vehiculos()
    if repetir:
        lg.guardar_automoviles()
        repetir = True