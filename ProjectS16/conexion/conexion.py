import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",       # el servidor de la BD
    user="root",            # el usuario de MySQL
    password="tu_contraseña", # la contraseña de MySQL
    database="harta_pinta"  # el nombre de la BD
)

cursor = conexion.cursor()