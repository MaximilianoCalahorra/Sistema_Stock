from Stock import Stock
from Lote import Lote

#Clase Almacen:
class Almacen(Stock):
    #Constructor:
    def __init__(self, id_stock, producto, unidades_deseable, unidades_minima):
        super().__init__(id_stock, producto)
        self.__unidades_deseable = unidades_deseable
        self.__unidades_minima = unidades_minima
        self.__lotes = []
        
    #Getters:
    @property
    def unidades_deseable(self):
        return self.__unidades_deseable
    
    @property
    def unidades_minima(self):
        return self.__unidades_minima
    
    @property
    def lotes(self):
        return self.__lotes
    
    #Setters:
    @unidades_deseable.setter
    def unidades_deseable(self, nuevas_unidades_deseable):
        self.__unidades_deseable = nuevas_unidades_deseable
    
    @unidades_minima.setter
    def unidades_minima(self, nuevas_unidades_minima):
        self.__unidades_minima = nuevas_unidades_minima
        
    #__str__:
    def __str__(self):
        almacen = "Almacén:\n"
        almacen += super().__str__()
        almacen += f"Unidades deseables: {self.__unidades_deseable}\n"
        almacen += f"Unidades mínimas: {self.__unidades_minima}\n"
        almacen += "Lotes:\n"
        for lote in self.__lotes:
            almacen += lote.__str__()
        return almacen
    
    #CU 9:
    def agregar_lote(self, fecha, cant_inicial):
        return self.__lotes.append(Lote(fecha, cant_inicial, cant_inicial))