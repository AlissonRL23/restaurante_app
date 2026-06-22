class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_producto(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"

    def __str__(self):
        return self.mostrar_producto()
