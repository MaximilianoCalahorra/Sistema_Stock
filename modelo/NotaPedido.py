#Clase NotaPedido:
class NotaPedido:
    #Constructor:
    def __init__(self, fecha, cantidad, cliente):
        self.__fecha = fecha
        self.__cantidad = cantidad
        self.__cliente = cliente
        
    #Getters:
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def cliente(self):
        return self.__cliente
    
    #Setters:
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
        
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
    
    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente
        
    #__str__:
    def __str__(self):
        nota_pedido = "Nota del pedido:\n"
        nota_pedido += f"Fecha: {self.__fecha}\n"
        nota_pedido += f"Cantidad: {self.__cantidad}\n"
        nota_pedido += f"Cliente: {self.__cliente}\n"
        return nota_pedido