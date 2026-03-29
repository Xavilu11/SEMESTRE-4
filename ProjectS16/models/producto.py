class Producto:
    """
    Clase que representa un producto dentro del sistema.
    Se usa como modelo para mapear filas de la tabla 'productos'
    a objetos Python que luego se manejan en la aplicación.
    """

    def __init__(self, id_producto=None, nombre=None, precio=None, stock=None):
        # ID único del producto en la base de datos
        self.id_producto = id_producto
        # Nombre del producto
        self.nombre = nombre
        # Precio del producto (numérico, puede ser float o decimal)
        self.precio = precio
        # Cantidad disponible en inventario
        self.stock = stock

    def __repr__(self):
        """
        Representación en texto del objeto Producto.
        Útil para depuración y logs.
        """
        return f"<Producto {self.id_producto} - {self.nombre}>"