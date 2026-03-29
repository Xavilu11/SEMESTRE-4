# Importamos la función para obtener conexión a la base de datos
from conexion.conexion import obtener_conexion
# Importamos el modelo Usuario
from models.usuario import Usuario

# ---------------------------------------------------
# LISTAR USUARIOS
# ---------------------------------------------------
def listar_usuarios():
    """
    Devuelve una lista de todos los usuarios en la tabla 'usuarios'.
    Cada fila se convierte en un objeto Usuario.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)  # dictionary=True devuelve filas como diccionario
    cursor.execute("SELECT * FROM usuarios")
    usuarios = [Usuario(**row) for row in cursor.fetchall()]  # Mapea cada fila a Usuario
    conexion.close()
    return usuarios

# ---------------------------------------------------
# OBTENER USUARIO POR ID
# ---------------------------------------------------
def obtener_usuario(id):
    """
    Devuelve un objeto Usuario según su id_usuario.
    Si no existe, devuelve None.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario=%s", (id,))
    row = cursor.fetchone()
    conexion.close()
    return Usuario(**row) if row else None

# ---------------------------------------------------
# CREAR USUARIO
# ---------------------------------------------------
def crear_usuario(usuario):
    """
    Inserta un nuevo usuario en la tabla 'usuarios'.
    Recibe un objeto Usuario con nombre, email y password.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
        (usuario.nombre, usuario.email, usuario.password)
    )
    conexion.commit()  # Guarda cambios en la BD
    conexion.close()

# ---------------------------------------------------
# ACTUALIZAR USUARIO
# ---------------------------------------------------
def actualizar_usuario(usuario):
    """
    Actualiza los datos de un usuario existente.
    Recibe un objeto Usuario con id_usuario, nombre, email y password.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE usuarios SET nombre=%s, email=%s, password=%s WHERE id_usuario=%s",
        (usuario.nombre, usuario.email, usuario.password, usuario.id_usuario)
    )
    conexion.commit()
    conexion.close()

# ---------------------------------------------------
# ELIMINAR USUARIO
# ---------------------------------------------------
def eliminar_usuario(id):
    """
    Elimina un usuario de la tabla 'usuarios' según su id_usuario.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s", (id,))
    conexion.commit()
    conexion.close()