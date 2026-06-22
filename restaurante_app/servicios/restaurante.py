class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\nClientes registrados:")
        for cliente in self.clientes:
            print(cliente)
