import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        port=3306,   # También se puede usar 3307 si XAMPP usa ese puerto
        user="root",
        password="", # vacío si root no tiene contraseña
        database="sistema_tienda"
    )