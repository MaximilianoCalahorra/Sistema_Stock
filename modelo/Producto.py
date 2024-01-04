#Clase Producto:
class Producto:
    #Constructor:
    def __init__(self, id_producto, codigo, nombre, precio):
        self.__id_producto = id_producto
        self.codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    #Getters:
    @property
    def id_producto(self):
        return self.__id_producto
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    #Setters:
    @id_producto.setter
    def id_producto(self, nuevo_id_producto):
        self.__id_producto = nuevo_id_producto
    
    #CU 1:
    @codigo.setter
    def codigo(self, nuevo_codigo):
        if len(nuevo_codigo) != 10:
            raise Exception("Error! El código del producto es inválido.\n")
        self.__codigo = nuevo_codigo
        
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        
    #__str__:
    def __str__(self):
        producto = "Producto:\n"
        producto += f"ID: #{self.__id_producto}\n"
        producto += f"Código: #{self.__codigo}\n"
        producto += f"Nombre: {self.__nombre}\n"
        producto += f"Precio: ${self.__precio}\n"
        return producto