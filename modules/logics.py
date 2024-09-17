# from .classes import Automovil, Bicicleta, Carga, Motocicleta, Particular, EnteroError
import time
import csv
from .classes import *
from os import name, path, system as st
listado_vehiculos = []
listado_automoviles = []
listado_motocicletas = []
listado_biciletas = []
listado_veh_carga = []
listado_veh_particular = []


def clear_screen():
    if name == "nt":
        st("cls")
    else:
        st("clear")

def new_automovil():
    clear_screen()
    print("Ingrese Marca del Automovil")
    marca = input()
    print("Ingrese Modelo del Automovil")
    modelo = input()
    print("Ingrese Numero de Ruedas del Automovil")
    nroRuedas = int(input())
    if not isinstance(nroRuedas, int):
        raise EnteroError(nroRuedas)
    print("Ingrese Velocidad del Automovil")
    velocidad = int(input())
    if not isinstance(velocidad, int):
        raise EnteroError(velocidad)
    print("Ingrese Cilindrada del Automovil")
    cilindrada = int(input())
    if not isinstance(cilindrada, int):
        raise EnteroError(cilindrada)

    try:
        automovil = Automovil(marca, modelo, nroRuedas, velocidad, cilindrada)
        listado_veh_particular.append(automovil)
        return listado_veh_particular
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def ingreso_vehiculos():
    print("ingrese el numero de vehiculos a ingresar")
    try:
        contador = 0
        valor = input()
        if valor.isdigit():
            contador = int(valor)
        else:
            raise EnteroError(valor)

        for i in range(1, contador + 1):
            clear_screen()
            print(f"para vehiculo nº {i} Seleccione el tipo de vehiculo a registrar")
            print("1.- Automoviles Particulares")
            print("2.- Automoviles de carga")
            print("3.- Bicicleta")
            print("4.- Motocicleta")
            opcion = int(input())
            if opcion == 1:
                print("opcion 1")
                time.sleep(0.5)
                new_automovil()
        return True
    except EnteroError as e:
        print(e)
        return False

def imprimir_automoviles():
    cont = 0
    for auto in listado_veh_particular:
        # return len(listado_veh_particular)
        cont += 1
        print(f"automovil {cont}: marca {auto.marca} modelo {auto.modelo} cilindrada {auto.cilindrada}cc")

def guardar_automoviles():
    Vehiculo.guardar_Vehiculos()
    Automovil.guardar_Automovil()
    Particular.guardar_veh_particular()
    Carga.guardar_veh_carga()
    Bicicleta.guardar_bicicletas()
    Motocicleta.guardar_motocicletas()

def leer_automoviles():
    Vehiculo.leer_vehiculos()
    Automovil.leer_automoviles()
    Particular.leer_veh_particular()
    Carga.leer_veh_carga()
    Bicicleta.leer_bicicletas()
    Motocicleta.leer_motocicletas()
