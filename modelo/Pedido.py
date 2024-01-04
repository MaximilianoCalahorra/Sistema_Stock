from Stock import Stock
from NotaPedido import NotaPedido

#Clase Pedido:
class Pedido(Stock):
    #Constructor:
    def __init__(self, id_stock, producto):
        super().__init__(id_stock, producto)
        self.__notas_pedidos = []
        
    #Getter:
    @property
    def notas_pedidos(self):
        return self.__notas_pedidos
    
    #__str__:
    def __str__(self):
        pedido = "Pedido:\n"
        pedido += super().__str__()
        pedido += "Notas del pedido:\n"
        for nota_pedido in self.__notas_pedidos:
            pedido += nota_pedido.__str__()
        return pedido
    
    #CU 8:
    def agregar_nota_pedido(self, fecha, cantidad, cliente):
        return self.__notas_pedidos.append(NotaPedido(fecha, cantidad, cliente))