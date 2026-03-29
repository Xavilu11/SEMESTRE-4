# Importamos la función para obtener conexión a la base de datos
from conexion.conexion import obtener_conexion
# Importamos el modelo Producto
from models.producto import Producto

# ---------------------------------------------------
# LISTAR PRODUCTOS
# ---------------------------------------------------
def listar_productos():
    """
    Devuelve una lista de todos los productos en la tabla 'productos'.
    Cada fila se convierte en un objeto Producto.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)  # dictionary=True devuelve filas como diccionario
    cursor.execute("SELECT * FROM productos")
    productos = [Producto(**row) for row in cursor.fetchall()]  # Mapea cada fila a Producto
    conexion.close()
    return productos

# ---------------------------------------------------
# OBTENER PRODUCTO POR ID
# ---------------------------------------------------
def obtener_producto(id):
    """
    Devuelve un objeto Producto según su id_producto.
    Si no existe, devuelve None.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE id_producto=%s", (id,))
    row = cursor.fetchone()
    conexion.close()
    return Producto(**row) if row else None

# ---------------------------------------------------
# CREAR PRODUCTO
# ---------------------------------------------------
def crear_producto(producto):
    """
    Inserta un nuevo producto en la tabla 'productos'.
    Recibe un objeto Producto con nombre, precio y stock.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
        (producto.nombre, producto.precio, producto.stock)
    )
    conexion.commit()  # Guarda cambios en la BD
    conexion.close()

# ---------------------------------------------------
# ACTUALIZAR PRODUCTO
# ---------------------------------------------------
def actualizar_producto(producto):
    """
    Actualiza los datos de un producto existente.
    Recibe un objeto Producto con id_producto, nombre, precio y stock.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s",
        (producto.nombre, producto.precio, producto.stock, producto.id_producto)
    )
    conexion.commit()
    conexion.close()

# ---------------------------------------------------
# ELIMINAR PRODUCTO
# ---------------------------------------------------
def eliminar_producto(id):
    """
    Elimina un producto de la tabla 'productos' según su id_producto.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id,))
    conexion.commit()
    conexion.close()