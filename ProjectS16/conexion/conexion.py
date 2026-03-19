import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # vacío si el root no tiene contraseña
    database="harta_pinta"
)

cursor = conexion.cursor()