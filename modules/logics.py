import time
import csv
from modules.classes import *
from os import name, path, system as st
'''
importacion de las librerias necesarias para la operacion de la logica del programa
'''
listado_vehiculos = []
listado_automoviles = []
listado_motocicletas = []
listado_bicicletas = []
listado_veh_carga = []
listado_veh_particular = []
'''
creaccion variables tipo lista donde se almacenaran los datos de los vehiculos registrados por el sistema
'''

def clear_screen():
    '''
    Funcion dedicada a limpiar la consola para imprimir nueva informacion en ella
    '''
    if name == "nt":
        st("cls")
    else:
        st("clear")

def new_automovil():
    """
        Funcion para Crear una nueva instancia de clase Automovil
        solicitando los parametros al usuario y luego generando la nueva instancia
        finalmente almacenando la nueva instancia en el listado de automoviles
    """
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
    nroRadios = int(input())
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
        listado_motocicletas.append(motocicleta)
        return listado_motocicletas
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("ha ocurrido un error:", e)

def ingreso_vehiculos():
    clear_screen()
    print("*****BIENVENIDO*****")
    print("indique operacion a realizar:")
    print("1.- Ingresar Vehiculo (general)")
    print("2.- ingresar vehiculo, segun tipo")
    print("3.- Consultar Vehiculos Ingresados")
    print("4.- Salir del sistema")
    opcion = 0
    valor = input()
    if valor.isdigit():
        opcion = int(valor)
    
    if opcion == 1:
        ingreso_vehiculos_f1()
    elif opcion == 2:
        ingreso_vehiculos_f2()
    elif opcion == 3:
        imprimir_Vehiculos()
    elif opcion == 4:
        return True

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
            guardar_automoviles()
        imprimir_automoviles()
        print("\nPara volver al menu principal presione [Enter]")
        input()
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
        guardar_automoviles()
        return True
    except EnteroError as e:
        print(e)
        return False

def imprimir_automoviles():
    cont = 0
    print()
    print("Listado de Automoviles Ingresados")
    print()
    for auto in listado_automoviles:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc")

def imprimir_Veh_particulares():
    cont = 0
    print()
    print("Listado Vehiculos Particulares")
    print()
    for auto in listado_veh_particular:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc, {auto.puestos} asientos")

def imprimir_Veh_carga():
    cont = 0
    print()
    print("Listado Vehiculos de Carga")
    print()
    for auto in listado_veh_carga:
        cont += 1
        print(f"datos del automovil #{cont}: marca: {auto.marca}, modelo: {auto.modelo}, {auto.nroRuedas} Ruedas, {auto.velocidad} km/h, cilindrada: {auto.cilindrada}cc, capacidad de carga {auto.carga}kg.")

def imprimir_bicicletas():
    cont = 0
    print()
    print("Listado Bicicletas")
    print()
    for bici in listado_bicicletas:
        cont += 1
        print(f"datos de la bicicleta #{cont}: marca: {bici.marca}, modelo: {bici.modelo}, {bici.nroRuedas} Ruedas, tipo: {bici.tipo}")

def imprimir_motocicletas():
    cont = 0
    print()
    print("Listado motocicletas")
    print()
    for moto in listado_motocicletas:
        cont += 1
        print(f"datos del motocicleta #{cont}: marca: {moto.marca}, modelo: {moto.modelo}, {moto.nroRuedas} Ruedas, tipo: {moto.tipo}, {moto.nroRadios} radios, cuadro: {moto.cuadro}, motor: {moto.motor}")

def imprimir_Vehiculos():
    """
    Funcion que imprime los datos de los vehiculos 
    segun la preferencia indicada
    [1] imprime listado de automoviles particulares
    [2] imprime listado de automoviles de carga
    [3] imprime listado de bicicletas
    [4] imprime listado de motocicletas
    [5] imprime listado de todos los vehiculos
    
    """
    clear_screen()
    print("vehiculos a consultar: (seleccione opcion correspondiente)")
    print("[1].- Vehiculos Particulares")
    print("[2].- Vehiculos de Carga")
    print("[3].- Bicicletas")
    print("[4].- Motocicletas")
    print("[5].- Todos los Vehiculos Ingresados")
    opcion = 0
    valor = input()
    if valor.isdigit():
        opcion = int(valor)
    else:
        raise EnteroError(valor)
    
    if opcion == 1:
        imprimir_Veh_particulares()
        print("\nPara volver al menu principal presione [Enter]")
        input()
    elif opcion == 2:
        imprimir_Veh_carga()
        print("\nPara volver al menu principal presione [Enter]")
        input()
    elif opcion == 3:
        imprimir_bicicletas()
        print("\nPara volver al menu principal presione [Enter]")
        input()
    elif opcion == 4:
        imprimir_motocicletas()
        print("\nPara volver al menu principal presione [Enter]")
        input()
    elif opcion == 5:
        imprimir_Veh_particulares()
        imprimir_Veh_carga()
        imprimir_bicicletas()
        imprimir_motocicletas()
        print("\nPara volver al menu principal presione [Enter]")
        input()
    else:
        print("Valor ingresado no es valido, debe indicar uno de los valores listados")
        print("Presione [Enter] para volver a intentar")
        input()
        imprimir_Vehiculos()
    
def guardar_automoviles():
    """
    Funcion de llamado a los metodos de cada clase que vuelcan 
    los datos de los vehiculos ingresados en las variables listas 
    correspondiente a cada clase, las cuales seran leidas en el 
    proximo acceso al programa
    """
    Vehiculo.guardar_Vehiculos()
    Automovil.guardar_Automovil()
    Particular.guardar_veh_particular()
    Carga.guardar_veh_carga()
    Bicicleta.guardar_bicicletas()
    Motocicleta.guardar_motocicletas()

def leer_automoviles():
    '''
    Funcion de llamado a todos los metodos de clases que leen los datos del archivo data base, 
    y lo vuelcan a las variables de listas especificas de cada clase
    '''
    Vehiculo.leer_vehiculos()
    Automovil.leer_automoviles()
    Particular.leer_veh_particular()
    Carga.leer_veh_carga()
    Bicicleta.leer_bicicletas()
    Motocicleta.leer_motocicletas()
    
    """_summary_
    """