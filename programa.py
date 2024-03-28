from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    nombre = input("Ingres el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery de la tienda: "))
    tipo = input("Ingrese el tipo de tienda (restaurante, supermercado, farmacia): ").lower()

    if tipo == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "farmacia":
        return Farmacia(nombre, costo_delivery)

def ingresar_productos(tienda):
    while True:
        print("Ingresar un nuevo producto")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del produto: "))
        stock = int(input("Stock del producto (opcional, por defecto es 0): ") or "0")
        tienda.agregar_producto(nombre, precio, stock)
        break

def listar_productos(tienda):
    print("Listado de productos")
    tienda.listar_productos()

def realizar_venta(tienda):
    print("Realizar una venta")
    nombre_producto = input("Nombre del producto a vender: ")
    cantidad = int(input("Cantidad a vender: "))
    tienda.realizar_venta(nombre_producto, cantidad)

def main():
    tienda = crear_tienda()
    if tienda is None:
        return

    while True:
        print("¿Qué acción desea realizar?")
        print("1. Ingresar producto")
        print("2. Listar productos existentes")
        print("3. Realizar una venta")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_productos(tienda)
        elif opcion == "2":
            listar_productos(tienda)
        elif opcion == "3":
            realizar_venta(tienda)
        elif opcion == "4":
            break
if __name__ == "__main__":
    main()
