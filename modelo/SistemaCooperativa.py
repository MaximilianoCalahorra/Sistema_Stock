from Producto import Producto
from Pedido import Pedido
from Almacen import Almacen

#Clase SistemaCooperativa:
class SistemaCooperativa:
    #Constructor:
    def __init__(self):
        self.__stocks = []
        self.__productos = []
        
    #Getters:
    @property
    def stocks(self):
        return self.__stocks

    @property
    def productos(self):
        return self.__productos
    
    #__str__:
    def __str__(self):
        sistema_cooperativa = "Sistema de la cooperativa:\n"
        sistema_cooperativa += "Stocks:\n"
        for stock in self.__stocks:
            sistema_cooperativa += stock.__str__()
        sistema_cooperativa += "Productos:\n"
        for producto in self.__productos:
            sistema_cooperativa += producto.__str__()
        return sistema_cooperativa
    
    #Métodos:
    #CU 2:
    def agregar_producto(self, codigo, nombre, precio):
        id_producto = 1
        if len(self.__productos) > 0:
            tamanio = len(self.__productos)
            id_producto = self.__productos[tamanio - 1].id_producto + 1
        return self.__productos.append(Producto(id_producto, codigo, nombre, precio))
    
    #CU 3:
    def traer_producto(self, codigo):
        producto_auxiliar = None
        producto_buscado = None
        i = 0
        while i < len(self.__productos) and producto_buscado == None:
            producto_auxiliar = self.__productos[i]
            if producto_auxiliar.codigo == codigo:
                producto_buscado = producto_auxiliar
            i += 1
        return producto_buscado
    
    #CU 4:
    def agregar_pedido(self, producto):
        id_stock = 1
        if len(self.__stocks) > 0:
            tamanio = len(self.__stocks)
            id_stock = self.__stocks[tamanio - 1].id_stock + 1
        return self.__stocks.append(Pedido(id_stock, producto))
    
    #CU 5:
    def agregar_almacen(self, producto, unidades_deseable, unidades_minima):
        id_stock = 1
        if len(self.__stocks) > 0:
            tamanio = len(self.__stocks)
            id_stock = self.__stocks[tamanio - 1].id_stock + 1
        return self.__stocks.append(Almacen(id_stock, producto, unidades_deseable, unidades_minima))
    
    #CU 6:
    def traer_stocks(self, producto):
        stocks = []
        for stock in self.__stocks:
            if stock.producto.codigo == producto.codigo:
                stocks.append(stock)
        return stocks
    
    #CU 7:
    def traer_stock(self, id_stock):
        stock_auxiliar = None
        stock_buscado = None
        i = 0
        while i < len(self.__stocks) and stock_buscado == None:
            stock_auxiliar = self.__stocks[i]
            if stock_auxiliar.id_stock == id_stock:
                stock_buscado = stock_auxiliar
            i += 1
        return stock_buscado