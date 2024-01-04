from abc import ABC, abstractclassmethod

#Clase Stock:
class Stock(ABC):
    #Constructor:
    def __init__(self, id_stock, producto):
        self._id_stock = id_stock
        self._producto = producto
        
    #Getters:
    @property
    def id_stock(self):
        return self._id_stock
    
    @property
    def producto(self):
        return self._producto
    
    #Setters:
    @id_stock.setter
    def id_stock(self, nuevo_id_stock):
        self._id_stock = nuevo_id_stock
        
    @producto.setter
    def producto(self, nuevo_producto):
        self._producto = nuevo_producto
    
    #__str__:
    def __str__(self):
        stock = f"ID: #{self._id_stock}\n"
        stock += self._producto.__str__()
        return stock