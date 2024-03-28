from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @property
    def productos(self):
        return self.__productos

    def agregar_producto(self, nombre, precio, stock=0):
        # Comprueba si el producto ya existe
        for prod in self.__productos:
            if prod.nombre == nombre:
                prod.modificar_stock(stock)
                return
        self.__productos.append(Producto(nombre, precio, stock)) 

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def agregar_producto(self, nombre, precio, stock=0):
        super().agregar_producto(nombre, precio, 0)  # Los productos siempre se crean con stock 0

    def listar_productos(self):
        for producto in self.productos:
            print(f"{producto.nombre} a ${producto.precio}")  # No muestra el stock

    def realizar_venta(self, nombre_producto, cantidad):
        print(f"Venta realizada: {cantidad} de {nombre_producto}")

class Supermercado(Tienda):
    def listar_productos(self):
        for producto in self.productos:
            stock_msg = "Pocos productos disponibles" if producto.stock < 10 else f"Stock: {producto.stock}"
            print(f"{producto.nombre} a ${producto.precio} - {stock_msg}")

    def realizar_venta(self, nombre_producto, cantidad):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto and producto.stock >= cantidad:
            producto.stock -= cantidad
            print(f"Venta realizada: {cantidad} de {nombre_producto}")
        else:
            print("No hay suficiente stock o el producto no existe.")

class Farmacia(Tienda):
    def listar_productos(self):
        for producto in self.productos:
            envio_msg = "Envío gratis al solicitar este producto" if producto.precio > 15000 else ""
            print(f"{producto.nombre} a ${producto.precio} - {envio_msg}")

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print("No se puede vender más de 3 unidades por producto.")
            return
        super().realizar_venta(nombre_producto, cantidad)
