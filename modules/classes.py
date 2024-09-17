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
        archivo = open("modules/db/db_vehiculos.csv", "w", encoding="UTF-8")
        cont = 0
        for vehiculo in lg.listado_vehiculos:
            archivo.write(f"{vehiculo.marca};{vehiculo.modelo};{vehiculo.nroRuedas}\n")
        else:
            archivo.close()
    
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
                automovil = Automovil(marca, modelo, int(nroRuedas))
                lg.listado_vehiculos.append(automovil)
        archivo.close()
        return lg.listado_vehiculos

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int) :
        super().__init__(marca, modelo, nroRuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def guardar_Automovil():
        archivo = open("modules/db/db_automoviles.csv", "w", encoding="UTF-8")
        cont = 0
        for auto in lg.listado_veh_particular:
            archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.velocidad};{auto.cilindrada}\n")
        else:
            archivo.close()
    
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
                automovil = Automovil(marca, modelo, int(
                    nroRuedas), int(velocidad), int(cilindrada))
                lg.listado_automoviles.append(automovil)
        archivo.close()
        return lg.listado_automoviles

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int, puestos: int) -> None:
        super().__init__(marca, modelo, nroRuedas, velocidad, cilindrada)
        self.puestos = puestos
    
    def guardar_veh_particular():
        archivo = open("modules/db/db_veh_particular.csv", "w", encoding="UTF-8")
        cont = 0
        for auto in lg.listado_veh_particular:
            archivo.write(f"{auto.marca};{auto.modelo};{auto.nroRuedas};{auto.velocidad};{auto.cilindrada}\n")
        else:
            archivo.close()
    
    def leer_veh_particular():
        if not path.exists("modules/db/db_veh_particular.csv"):
            archivo = open("modules/db/db_veh_particular.csv","w", encoding="UTF-8")
        else:
            archivo = open("modules/db/db_veh_particular.csv","r", encoding="UTF-8")
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                auto_data = linea.split(";")
                marca, modelo, nroRuedas, velocidad, cilindrada = auto_data
                automovil = Automovil(marca, modelo, int(
                    nroRuedas), int(velocidad), int(cilindrada))
                lg.listado_veh_particular.append(automovil)
        archivo.close()
        return lg.listado_veh_particular

class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, velocidad: int, cilindrada: int, carga: int) -> None:
        super().__init__(marca, modelo, nroRuedas, velocidad, cilindrada)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, nroRuedas: int, tipo: str) -> None:
        super().__init__(marca, modelo, nroRuedas)
        tipos_permitidos = ("urbana", "carrera")
        if tipo in tipos_permitidos:
            self.tipo = tipo
        else:
            raise ValueError(f"valor no Valido, {tipos_permitidos}")
        
    def __str__(self) -> str:
        return "class: Bicicleta"

class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, nroRuedas: int,nroRadios: int, cuadro: str, motor: str) -> None:
        super().__init__(marca, modelo, nroRuedas)
        self.nroRadios = nroRadios
        
        cuadros_permitidos = ("doble cuna","multitubolar","doble viga")
        if cuadro in cuadros_permitidos:
            self.cuadro = cuadro
        else:
            raise ValueError(f"valor no Valido, {cuadros_permitidos}")
        
        motores_disponibles = ("2T","4T")
        if motor.upper() in motores_disponibles:
            self.motor = motor.upper()
        else:
            raise ValueError(f"valor no valido, {motores_disponibles}")

class EnteroError(Exception):
    def __init__(self, valor, mensaje = "Error de Valor, valor ingresado no es un Entero") -> None:
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(f"{mensaje}:  {valor}")
