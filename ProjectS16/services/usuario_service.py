from conexion.conexion import obtener_conexion
from models.usuario import Usuario

def listar_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_usuario, nombre, email, password FROM usuarios")
    usuarios = []
    for fila in cursor.fetchall():
        usuarios.append(Usuario(id_usuario=fila[0], nombre=fila[1], email=fila[2], password=fila[3]))
    conexion.close()
    return usuarios

def obtener_usuario(id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_usuario, nombre, email, password FROM usuarios WHERE id_usuario = %s", (id_usuario,))
    fila = cursor.fetchone()
    conexion.close()
    if fila:
        return Usuario(id_usuario=fila[0], nombre=fila[1], email=fila[2], password=fila[3])
    return None

def crear_usuario(usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                   (usuario.nombre, usuario.email, usuario.password))
    conexion.commit()
    conexion.close()

def actualizar_usuario(usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre=%s, email=%s, password=%s WHERE id_usuario=%s",
                   (usuario.nombre, usuario.email, usuario.password, usuario.id_usuario))
    conexion.commit()
    conexion.close()

def eliminar_usuario(id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s", (id_usuario,))
    conexion.commit()
    conexion.close()