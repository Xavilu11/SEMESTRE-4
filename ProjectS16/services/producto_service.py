from conexion.conexion import obtener_conexion
from models.producto import Producto

# Servicio para listar todos los productos
def listar_productos():
    # Abrimos conexión a la base
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Ejecutamos consulta para traer todos los productos
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos")
    productos = []
    # Convertimos cada fila en un objeto Producto
    for fila in cursor.fetchall():
        productos.append(Producto(id_producto=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3]))
    # Cerramos conexión
    conexion.close()
    return productos

# Servicio para obtener un producto por su ID
def obtener_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Consulta con parámetro para evitar inyección SQL
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos WHERE id_producto = %s", (id_producto,))
    fila = cursor.fetchone()
    conexion.close()
    # Si existe, lo devolvemos como objeto Producto
    if fila:
        return Producto(id_producto=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3])
    return None

# Servicio para crear un nuevo producto
def crear_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Insertamos un nuevo registro en la tabla productos
    cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
                   (producto.nombre, producto.precio, producto.stock))
    conexion.commit()  # Guardamos cambios
    conexion.close()

# Servicio para actualizar un producto existente
def actualizar_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Actualizamos los campos del producto según su ID
    cursor.execute("UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s",
                   (producto.nombre, producto.precio, producto.stock, producto.id_producto))
    conexion.commit()
    conexion.close()

# Servicio para eliminar un producto
def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Eliminamos el producto según su ID
    cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id_producto,))
    conexion.commit()
    conexion.close()