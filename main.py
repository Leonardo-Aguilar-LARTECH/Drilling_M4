import modules.logics as lg
from modules.classes import *
import time

repetir = False

while not repetir:
    lg.leer_automoviles()
    print(lg.listado_automoviles)
    print(lg.listado_bicicletas)
    print(lg.listado_veh_carga)
    print(lg.listado_veh_particular)
    print(lg.listado_vehiculos)
    print(lg.listado_motocicletas)
    time.sleep(5)
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