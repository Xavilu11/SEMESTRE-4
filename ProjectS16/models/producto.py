class Producto:
    def __init__(self, id_producto=None, nombre=None, precio=None, stock=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"<Producto {self.id_producto} - {self.nombre}>"