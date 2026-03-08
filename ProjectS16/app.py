# app.py
from flask import Flask, render_template, request, redirect, url_for
import inventario.bd as bd   # Persistencia en TXT, JSON, CSV
from models import Base, Producto   # ORM con SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# -------------------------------
# Configuración SQLAlchemy
# -------------------------------
engine = create_engine("sqlite:///inventario.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# Rutas principales
# -------------------------------
@app.route('/')
def index():
    # Mostrar productos desde SQLite con ORM
    productos = session.query(Producto).all()
    return render_template("index.html", productos=productos)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=["POST"])
def add():
    id = request.form["id"]
    nombre = request.form["nombre"]
    color = request.form["color"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    nuevo_producto = Producto(
        id=id,
        nombre=nombre,
        color=color,
        cantidad=cantidad,
        precio=precio
    )
    session.add(nuevo_producto)
    session.commit()
    return redirect(url_for("index"))

# -------------------------------
# Rutas de persistencia en TXT, JSON, CSV
# -------------------------------
@app.route('/datos/txt')
def datos_txt():
    productos = bd.leer_txt()
    return render_template("datos.html", productos=productos, formato="Archivo de Texto")

@app.route('/datos/json')
def datos_json():
    productos = bd.leer_json()
    return render_template("datos.html", productos=productos, formato="Archivo JSON")

@app.route('/datos/csv')
def datos_csv():
    productos = bd.leer_csv()
    return render_template("datos.html", productos=productos, formato="Archivo CSV")

# -------------------------------
# Rutas con SQLAlchemy
# -------------------------------
@app.route('/datos/sqlalchemy')
def datos_sqlalchemy():
    productos = session.query(Producto).all()
    return render_template("productos.html", productos=productos)

@app.route('/add/sqlalchemy', methods=["POST"])
def add_sqlalchemy():
    id = request.form["id"]
    nombre = request.form["nombre"]
    color = request.form["color"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    nuevo_producto = Producto(
        id=id,
        nombre=nombre,
        color=color,
        cantidad=cantidad,
        precio=precio
    )
    session.add(nuevo_producto)
    session.commit()
    return redirect(url_for("datos_sqlalchemy"))

# -------------------------------
# Ejecución
# -------------------------------
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)# app.py
from flask import Flask, render_template, request, redirect, url_for
import database
import inventario.bd as bd   # Persistencia en TXT, JSON, CSV
from models import Base, Producto   # ORM con SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# -------------------------------
# Configuración SQLAlchemy
# -------------------------------
engine = create_engine("sqlite:///inventario.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# Rutas
# -------------------------------
@app.route('/')
def index():
    # Usar SQLAlchemy directamente para mostrar productos
    productos = session.query(Producto).all()
    return render_template("index.html", productos=productos)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=["POST"])
def add():
    id = request.form["id"]
    nombre = request.form["nombre"]
    color = request.form["color"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    nuevo_producto = Producto(
        id=id,
        nombre=nombre,
        color=color,
        cantidad=cantidad,
        precio=precio
    )
    session.add(nuevo_producto)
    session.commit()
    return redirect(url_for("index"))

# -------------------------------
# Rutas de persistencia en TXT, JSON, CSV
# -------------------------------
@app.route('/datos/txt')
def datos_txt():
    productos = bd.leer_txt()
    return render_template("datos.html", productos=productos, formato="Archivo de Texto")

@app.route('/datos/json')
def datos_json():
    productos = bd.leer_json()
    return render_template("datos.html", productos=productos, formato="Archivo JSON")

@app.route('/datos/csv')
def datos_csv():
    productos = bd.leer_csv()
    return render_template("datos.html", productos=productos, formato="Archivo CSV")

@app.route('/datos/sqlalchemy')
def datos_sqlalchemy():
    productos = session.query(Producto).all()
    return render_template("productos.html", productos=productos)

@app.route('/add/sqlalchemy', methods=["POST"])
def add_sqlalchemy():
    id = request.form["id"]
    nombre = request.form["nombre"]
    color = request.form["color"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    nuevo_producto = Producto(
        id=id,
        nombre=nombre,
        color=color,
        cantidad=cantidad,
        precio=precio
    )
    session.add(nuevo_producto)
    session.commit()
    return redirect(url_for("datos_sqlalchemy"))

# -------------------------------
# Ejecución
# -------------------------------
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)