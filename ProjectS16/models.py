# models.py

# -------------------------------
# Clase Producto
# -------------------------------
# Representa un artículo del inventario de Harta Pinta.
# Cada producto tiene un identificador único, un nombre, un color,
# una cantidad en stock y un precio.
class Producto:
    def __init__(self, id, nombre, color, cantidad, precio):
        self.id = id                # Identificador único del producto
        self.nombre = nombre        # Nombre del producto (ej: "Camiseta básica")
        self.color = color          # Color del producto (ej: "Amarillo", "Lila", "Rojo")
        self.cantidad = cantidad    # Cantidad disponible en inventario
        self.precio = precio        # Precio unitario del producto

    # Métodos GET: obtener valores de los atributos
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_color(self):
        return self.color
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio

    # Métodos SET: modificar valores de los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_color(self, color):
        self.color = color
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio

    # Representación en texto del producto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Color: {self.color}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# -------------------------------
# Clase Inventario
# -------------------------------
# Administra los productos de Harta Pinta usando un diccionario.
# Clave: ID del producto, Valor: objeto Producto.
class Inventario:
    def __init__(self):
        # Diccionario vacío para almacenar los productos
        self.productos = {}

    def agregar_producto(self, producto):
        # Añadir un nuevo producto al inventario
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        # Eliminar un producto por su ID
        if id in self.productos:
            del self.productos[id]
            return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Actualizar cantidad o precio de un producto
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            return True
        return False

    def buscar_por_nombre(self, nombre):
        # Buscar productos por nombre (ignora mayúsculas/minúsculas)
        resultados = []
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        # Mostrar todos los productos del inventario
        return list(self.productos.values())