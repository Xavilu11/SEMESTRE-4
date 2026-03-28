import mysql.connector

# Función que devuelve una conexión activa a la base de datos
def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,          # Se ajusta según el puerto de MySQL en XAMPP (normalmente 3307)
        user="root",
        password="",        # vacío si root no tiene contraseña
        database="sistema_tienda"  # base de datos en phpMyAdmin
    )
    return conexion