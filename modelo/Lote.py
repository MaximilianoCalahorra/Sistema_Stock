#Clase Lote:
class Lote:
    #Constructor:
    def __init__(self, fecha, cant_inicial, cant_existente):
        self.__fecha = fecha
        self.__cant_inicial = cant_inicial
        self.__cant_existente = cant_existente
        
    #Getters:
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def cant_inicial(self):
        return self.__cant_inicial
    
    @property
    def cant_existente(self):
        return self.__cant_existente
    
    #Setters:
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
        
    @cant_inicial.setter
    def cant_inicial(self, nueva_cant_inicial):
        self.__cant_inicial = nueva_cant_inicial
    
    @cant_existente.setter
    def cant_existente(self, nueva_cant_existente):
        self.__cant_existente = nueva_cant_existente
        
    #__str__:
    def __str__(self):
        lote = "Lote:\n"
        lote += f"Fecha: {self.__fecha}\n"
        lote += f"Cantidad inicial: {self.__cant_inicial}\n"
        lote += f"Cantidad existente: {self.__cant_existente}\n"
        return lote