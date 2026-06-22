class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def realizar_pedido(self):
        return f"El cliente {self.nombre} realizó un pedido."

    def __str__(self):
        return f"Cliente: {self.nombre} - Teléfono: {self.telefono}"
