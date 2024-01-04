import sys
sys.path.append("D:\\Curso POO Python\\Sistema de Stock\\modelo")

import datetime

from SistemaCooperativa import SistemaCooperativa

#Test:
sistema_cooperativa = SistemaCooperativa()

#Test 1:
print("Test 1:")
sistema_cooperativa.agregar_producto("1111111111", "Producto 1", 100.0)
sistema_cooperativa.agregar_producto("2222222222", "Producto 2", 200.0)
sistema_cooperativa.agregar_producto("3333333333", "Producto 3", 300.0)
sistema_cooperativa.agregar_producto("4444444444", "Producto 4", 400.0)
print("Productos:\n")
for producto in sistema_cooperativa.productos:
    print(producto)
    
#Test 2:
print("Test 2:")
try:
    sistema_cooperativa.agregar_producto("111", "Producto 6", 300.0)
except Exception as e:
    print(e)

try:
    sistema_cooperativa.agregar_producto("222", "Producto 7", 400.0)
except Exception as e:
    print(e)
    
#Test 3:
print("Test 3:")
sistema_cooperativa.agregar_pedido(sistema_cooperativa.traer_producto("1111111111"))
sistema_cooperativa.agregar_pedido(sistema_cooperativa.traer_producto("2222222222"))
print("Pedidos:\n")
for pedido in sistema_cooperativa.stocks:
    print(pedido)
    
#Test 4:
print("Test 4:")
sistema_cooperativa.agregar_almacen(sistema_cooperativa.traer_producto("2222222222"), 100, 80)
sistema_cooperativa.agregar_almacen(sistema_cooperativa.traer_producto("3333333333"), 120, 100)
sistema_cooperativa.agregar_almacen(sistema_cooperativa.traer_producto("4444444444"), 220, 200)
print("Almacenes:\n")
for almacen in sistema_cooperativa.stocks:
    print(almacen)
    
#Test 5:
print("Test 5:")
stocks = sistema_cooperativa.traer_stocks(sistema_cooperativa.traer_producto("2222222222"))
print("Stocks del producto con código #22222222:\n")
for stock in stocks:
    print(stock)

#Test 6:
print("Test 6:")
pedido = sistema_cooperativa.traer_stock(1)
pedido.agregar_nota_pedido(datetime.date(2021, 7, 14), 100, "Cliente 1")
pedido.agregar_nota_pedido(datetime.date(2021, 7, 14), 120, "Cliente 2")
pedido.agregar_nota_pedido(datetime.date(2021, 7, 14), 150, "Cliente 3")
print(pedido)

#Test 7:
print("Test 7:")
almacen = sistema_cooperativa.traer_stock(3)
almacen.agregar_lote(datetime.date(2021, 7, 14), 1000)
almacen.agregar_lote(datetime.date(2021, 7, 14), 1200)
almacen.agregar_lote(datetime.date(2021, 7, 14), 1500)
print(almacen)