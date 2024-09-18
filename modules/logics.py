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
        listado_automoviles.append(automovil)
        return listado_automoviles
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def new_veh_particular():
    clear_screen()
    print("Ingrese Marca del vehiculo")
    marca = input()
    print("Ingrese Modelo del vehiculo")
    modelo = input()
    print("Ingrese Numero de Ruedas del vehiculo")
    nroRuedas = int(input())
    if not isinstance(nroRuedas, int):
        raise EnteroError(nroRuedas)
    print("Ingrese Velocidad del vehiculo")
    velocidad = int(input())
    if not isinstance(velocidad, int):
        raise EnteroError(velocidad)
    print("Ingrese Cilindrada del vehiculo")
    cilindrada = int(input())
    if not isinstance(cilindrada, int):
        raise EnteroError(cilindrada)
    print("ingrese numero de puestos del Vehiculo")
    puestos = int(input())
    if not isinstance(puestos, int):
        raise EnteroError(puestos)

    try:
        particular = Particular(marca, modelo, nroRuedas, velocidad, cilindrada,puestos)
        listado_veh_particular.append(particular)
        return listado_veh_particular
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def new_veh_carga():
    clear_screen()
    print("Ingrese Marca del vehiculo")
    marca = input()
    print("Ingrese Modelo del vehiculo")
    modelo = input()
    print("Ingrese Numero de Ruedas del vehiculo")
    nroRuedas = int(input())
    if not isinstance(nroRuedas, int):
        raise EnteroError(nroRuedas)
    print("Ingrese Velocidad del vehiculo")
    velocidad = int(input())
    if not isinstance(velocidad, int):
        raise EnteroError(velocidad)
    print("Ingrese Cilindrada del vehiculo")
    cilindrada = int(input())
    if not isinstance(cilindrada, int):
        raise EnteroError(cilindrada)
    print("ingrese capacidad de carga del Vehiculo")
    carga = int(input())
    if not isinstance(carga, int):
        raise EnteroError(carga)

    try:
        carga = Carga(marca, modelo, nroRuedas, velocidad, cilindrada,carga)
        listado_veh_carga.append(carga)
        return listado_veh_carga
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def new_bicicleta():
    clear_screen()
    print("Ingrese Marca de la bicicleta")
    marca = input()
    print("Ingrese Modelo de la bicicleta")
    modelo = input()
    print("Ingrese Numero de Ruedas de la bicicleta")
    nroRuedas = int(input())
    if not isinstance(nroRuedas, int):
        raise EnteroError(nroRuedas)
    print("Ingrese tipo de la bicicleta\n debe elegir entre 'urbana' o 'carrera'")
    tipo = input()
    if not tipo in ("urbana", "carrera"):
        raise ValueError(f"valor no Valido, debe ser 'urbana' o 'carrera'")

    try:
        bicicleta = Bicicleta(marca, modelo, nroRuedas, tipo)
        listado_bicicletas.append(bicicleta)
        return listado_bicicletas
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def new_motocicleta():
    clear_screen()
    print("Ingrese Marca de la motocicleta")
    marca = input()
    print("Ingrese Modelo de la motocicleta")
    modelo = input()
    print("Ingrese Numero de Ruedas de la motocicleta")
    nroRuedas = int(input())
    if not isinstance(nroRuedas, int):
        raise EnteroError(nroRuedas)
    print("Ingrese tipo de la motocicleta\n debe elegir entre 'urbana' o 'carrera'")
    tipo = input()
    if not tipo in ("urbana", "carrera"):
        raise ValueError(f"valor no Valido, debe ser 'urbana' o 'carrera'")
    print("Ingrese numero de radios de la motocicleta")
    nroRadios = input()
    if not isinstance(nroRadios, int):
        raise EnteroError(nroRadios)
    print("Ingrese tipo de cuadro de la motocicleta\n debe elegir entre 'doble cuna' 'multitubular' o 'doble viga'")
    cuadro = input()
    if not cuadro in ("doble cuna", "multitubular", "doble viga"):
        raise ValueError(f"valor no Valido, debe ser 'doble cuna' 'multitubular' o 'doble viga'")
    print("Ingrese tipo de motor de la motocicleta\n debe elegir entre '2t' o '4t'")
    motor = input()
    if not motor in ("2t", "4t"):
        raise ValueError(f"valor no Valido, debe ser '2t' o '4t'")
    
    try:
        motocicleta = Motocicleta(marca, modelo, nroRuedas,tipo, nroRadios, cuadro, motor)
        listado_motocicletas.append(Motocicleta)
        return listado_motocicletas
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)
    else:
        print("todo OK")

def ingreso_vehiculos():
    clear_screen()
    print("*****BIENVENIDO*****")
    print("indique operacion a realizar:")
    print("1.- Ingresar Vehiculo (general)")
    print("2.- ingresar vehiculo, segun tipo")
    print("3.- Consultar Vehiculos Ingresados")
    opcion = 0
    valor = input()
    if valor.isdigit():
        opcion = int(valor)
    
    if opcion == 1:
        new_automovil()
    if opcion == 2:
        ingreso_vehiculos_f2()
    if opcion == 3:
        imprimir_Vehiculos()

def ingreso_vehiculos_f1():
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
            new_automovil()
            return True
    except EnteroError as e:
        print(e)
        return False
    
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
                new_veh_particular()
            elif opcion == 2:
                new_veh_carga()
            elif opcion == 3:
                new_bicicleta()
            elif opcion == 4:
                new_motocicleta()
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

def imprimir_Vehiculos():
    clear_screen()
    print("vehiculos a consultar: (seleccione opcion correspondiente)")
    print("1.- Vehiculos Particulares")
    print("2.- Vehiculos de Carga")
    print("3.- Bicicletas")
    print("4.- Motocicletas")
    print("5.- Todos los Vehiculos Ingresados")
    opcion = 0
    valor = input()
    if valor.isdigit():
        opcion = valor
    
    if opcion == 1:
        imprimir_Veh_particulares()
    elif opcion == 2:
        imprimir_Veh_carga()
    elif opcion == 3:
        imprimir_bicicletas()
    elif opcion == 4:
        imprimir_motocicletas()
    elif opcion == 5:
        imprimir_Veh_particulares()
        imprimir_Veh_carga()
        imprimir_bicicletas()
        imprimir_motocicletas()
        time.sleep(5)

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
