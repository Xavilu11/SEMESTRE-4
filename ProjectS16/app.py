# app.py
from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    productos = database.obtener_productos()
    return render_template("index.html", productos=productos)

# Página "Acerca de"
@app.route('/about')
def about():
    return render_template("about.html")

# Ruta para añadir un producto desde el formulario
@app.route('/add', methods=["POST"])
def add():
    # Obtener datos del formulario
    id = request.form["id"]
    nombre = request.form["nombre"]
    color = request.form["color"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    # Insertar producto en la base de datos
    database.insertar_producto(id, nombre, color, cantidad, precio)

    # Redirigir de nuevo a la página principal
    return redirect(url_for("index"))

if __name__ == '__main__':
    import os
    database.crear_tabla()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)