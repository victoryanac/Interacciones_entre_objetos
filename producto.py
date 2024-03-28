
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)  # Asegura que el stock no sea negativo

    # Getter para el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Getter para el precio
    @property
    def precio(self):
        return self.__precio

    # Getter y Setter para el stock
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        self.__stock = max(valor, 0)

    def modificar_stock(self, cantidad):
        nuevo_stock = self.__stock + cantidad
        self.__stock = max(nuevo_stock, 0)