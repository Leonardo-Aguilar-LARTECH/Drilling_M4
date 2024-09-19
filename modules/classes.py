import modules.logics as lg
from os import path

class Vehiculo:
    def __init__(self, marca: str, modelo: str, nroRuedas: int) -> None:
        self.marca = marca
        self.modelo = modelo
        if not isinstance(nroRuedas, int):
            raise TypeError("Tipo de Dato Incorrecto, debe ser un entero")
        else:
            self.nroRuedas = nroRuedas
        
    @staticmethod
    def guardar_Vehiculos():
        with open("modules/db/db_vehiculos.csv", "w", encoding="UTF-8") as archivo:
            for vehiculo in lg.listado_vehiculos:
                archivo.write(f"{vehiculo.marca};{vehiculo.modelo};{vehiculo.nroRuedas}\n")
        
    @staticmethod
    def leer_vehiculos():
        if not path.exists("modules/db/db_vehiculos.csv"):
            archivo = open("modules/db/db_vehiculos.csv", "w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_vehiculos.csv", "r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas = auto_data
                vehiculo = Automovil(marca, modelo, int(nroRuedas))
                lg.listado_vehiculos.append(vehiculo)
        archivo.close()
        return lg.listado_vehiculos

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int) :
        super().__init__(marca, modelo, nroRuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    @staticmethod
    def guardar_Automovil():
        with open("modules/db/db_automoviles.csv", "w", encoding="UTF-8") as archivo:
            for auto in lg.listado_veh_particular:
                archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.velocidad};{auto.cilindrada}\n")
    
    @staticmethod
    def leer_automoviles():
        if not path.exists("modules/db/db_automoviles.csv"):
            archivo = open("modules/db/db_automoviles.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_automoviles.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, velocidad, cilindrada = auto_data
                automovil = Automovil(marca, modelo, int(nroRuedas), int(velocidad), int(cilindrada))
                lg.listado_automoviles.append(automovil)
        archivo.close()
        return lg.listado_automoviles

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int, puestos: int) -> None:
        super().__init__(marca, modelo, nroRuedas, velocidad, cilindrada)
        self.puestos = puestos
    
    @staticmethod
    def guardar_veh_particular():
        with open("modules/db/db_veh_particular.csv", "w", encoding="UTF-8") as archivo:
            for auto in lg.listado_veh_particular:
                archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.velocidad};{auto.cilindrada};{auto.puestos}\n")
        
    @staticmethod
    def leer_veh_particular():
        if not path.exists("modules/db/db_veh_particular.csv"):
            archivo = open("modules/db/db_veh_particular.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_veh_particular.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, velocidad, cilindrada, puestos = auto_data
                particular = Particular(marca, modelo, int(nroRuedas), int(velocidad), int(cilindrada), int(puestos))
                lg.listado_veh_particular.append(particular)
        archivo.close()
        return lg.listado_veh_particular

class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int, carga: int) -> None:
        super().__init__(marca, modelo, nroRuedas, velocidad, cilindrada)
        self.carga = carga
        
    @staticmethod
    def guardar_veh_carga():
        with open("modules/db/db_veh_carga.csv", "w", encoding="UTF-8") as archivo:
            for auto in lg.listado_veh_carga:
                archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.velocidad};{auto.cilindrada};{auto.carga}\n")
    
    @staticmethod
    def leer_veh_carga():
        if not path.exists("modules/db/db_veh_carga.csv"):
            archivo = open("modules/db/db_veh_carga.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_veh_carga.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, velocidad, cilindrada, carga = auto_data
                automovil = Carga(marca, modelo, int(nroRuedas), int(velocidad), int(cilindrada), int(carga))
                lg.listado_veh_carga.append(automovil)
        archivo.close()
        return lg.listado_veh_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, tipo: str) -> None:
        super().__init__(marca, modelo, nroRuedas)
        tipos_permitidos = ("urbana", "carrera")
        if tipo in tipos_permitidos:
            self.tipo = tipo
        else:
            raise ValueError(f"valor no Valido, {tipos_permitidos}")
    
    @staticmethod
    def guardar_bicicletas():
        with open("modules/db/db_bicicletas.csv", "w", encoding="UTF-8") as archivo:
            for bici in lg.listado_bicicletas:
                archivo.write(f"{bici.marca};{bici.modelo};{bici.nroRuedas};{bici.tipo}\n")
    
    @staticmethod
    def leer_bicicletas():
        if not path.exists("modules/db/db_bicicletas.csv"):
            archivo = open("modules/db/db_bicicletas.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_bicicletas.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, tipo = auto_data
                bicicleta = Bicicleta(marca, modelo, int(nroRuedas), tipo)
                lg.listado_bicicletas.append(bicicleta)
        archivo.close()
        return lg.listado_bicicletas

class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, nroRuedas: int,tipo: str, nroRadios: int, cuadro: str, motor: str) -> None:
        super().__init__(marca, modelo, nroRuedas, tipo)
        self.nroRadios = nroRadios
        
        cuadros_permitidos = ("doble cuna","multitubular","doble viga")
        if cuadro in cuadros_permitidos:
            self.cuadro = cuadro
        else:
            raise ValueError(f"valor no Valido, {cuadros_permitidos}")
        
        motores_disponibles = ("2T","4T")
        if motor.upper() in motores_disponibles:
            self.motor = motor.upper()
        else:
            raise ValueError(f"valor no valido, {motores_disponibles}")
    
    @staticmethod
    def guardar_motocicletas():
        with open("modules/db/db_motocicletas.csv", "w", encoding="UTF-8") as archivo:
            for auto in lg.listado_motocicletas:
                archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.tipo};{auto.nroRadios};{auto.cuadro};{auto.motor}\n")
        
    @staticmethod
    def leer_motocicletas():
        if not path.exists("modules/db/db_motocicletas.csv"):
            archivo = open("modules/db/db_motocicletas.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_motocicletas.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, tipo, nroRadios, cuadro, motor  = auto_data
                motocicleta = Motocicleta(marca, modelo, int(nroRuedas), tipo, int(nroRadios), cuadro, motor)
                lg.listado_motocicletas.append(motocicleta)
        archivo.close()
        return lg.listado_motocicletas

class EnteroError(Exception):
    def __init__(self, valor, mensaje = "Error de Valor, valor ingresado no es un Entero") -> None:
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(f"{mensaje}:  {valor}")
