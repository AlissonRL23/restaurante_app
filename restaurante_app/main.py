from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante("Sabor Casero")


# Crear productos
producto1 = Producto("Hamburguesa", "Comida rápida", 5.50)
producto2 = Producto("Jugo natural", "Bebida", 2.00)


# Crear clientes
cliente1 = Cliente("Carlos Pérez", "0999999999")
cliente2 = Cliente("Ana López", "0988888888")


# Agregar información al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

restaurante.registrar_cliente(cliente1)
restaurante.registrar_cliente(cliente2)


# Mostrar información
print("Restaurante:", restaurante.nombre)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()
