# database.py
import sqlite3

# -------------------------------
# Conexión y creación de tabla
# -------------------------------
def conectar():
    # Conecta a la base de datos SQLite (se crea si no existe)
    return sqlite3.connect("inventory.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            color TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

# -------------------------------
# Operaciones CRUD
# -------------------------------

def insertar_producto(id, nombre, color, cantidad, precio):
    """Inserta un nuevo producto en la tabla productos"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (id, nombre, color, cantidad, precio) VALUES (?, ?, ?, ?, ?)",
        (id, nombre, color, cantidad, precio)
    )
    conexion.commit()
    conexion.close()

def obtener_productos():
    """Obtiene todos los productos de la tabla"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos

def actualizar_producto(id, cantidad=None, precio=None):
    """Actualiza cantidad o precio de un producto"""
    conexion = conectar()
    cursor = conexion.cursor()
    if cantidad is not None:
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
    if precio is not None:
        cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id))
    conexion.commit()
    conexion.close()

def eliminar_producto(id):
    """Elimina un producto por su ID"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()