import time
import csv
from .classes import *
from os import name, path, system as st
listado_vehiculos = []
listado_automoviles = []
listado_motocicletas = []
listado_bicicletas = []
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

def ingreso_vehiculos_f2():
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
    for auto in listado_automoviles:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc")

def imprimir_Veh_particulares():
    cont = 0
    print("Listado Vehiculos Particulares")
    for auto in listado_veh_particular:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc, {auto.puestos} asientos")

def imprimir_Veh_carga():
    cont = 0
    print("Listado Vehiculos de Carga")
    for auto in listado_veh_carga:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc, capacidad de carga {auto.carga}kg.")

def imprimir_bicicletas():
    cont = 0
    print("Listado Bicicletas")
    for bici in listado_bicicletas:
        cont += 1
        print(f"datos del bicimovil #{cont}: marca: {bici.marca}, modelo: {bici.modelo}, {bici.nroRuedas} Ruedas, tipo: {bici.tipo}")

def imprimir_motocicletas():
    cont = 0
    print("Listado motocicletas")
    for moto in listado_motocicletas:
        cont += 1
        print(f"datos del motomovil #{cont}: marca: {moto.marca}, modelo: {moto.modelo}, {moto.nroRuedas} Ruedas, tipo: {moto.tipo}, {moto.nroRadios} radios, cuadro: {moto.cuadro}, motor: {moto.motor}")

def imprimir_Vehiculos()
    imprimir_Veh_particulares()
    imprimir_Veh_carga()
    imprimir_bicicletas()
    imprimir_motocicletas()

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
