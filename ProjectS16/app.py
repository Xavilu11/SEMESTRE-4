# app.py
from flask import Flask, render_template, request, redirect, url_for
import inventario.bd as bd   # Persistencia en TXT, JSON, CSV
from models import Base, Producto, Usuario   # ORM con SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# -------------------------------
# Configuración SQLAlchemy
# -------------------------------
# Cambiar a MySQL si se lo desea, asegurándose de tener el conector instalado y la BD configurada
# engine = create_engine("mysql+mysqlconnector://root:tu_contraseña@localhost/harta_pinta", echo=True)
engine = create_engine("sqlite:///inventario.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# Rutas principales
# -------------------------------
@app.route('/')
def index():
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
# Rutas con SQLAlchemy (Productos)
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
# Rutas con SQLAlchemy (Usuarios)
# -------------------------------
@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = session.query(Usuario).all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/add_usuario', methods=["POST"])
def add_usuario():
    nombre = request.form["nombre"]
    mail = request.form["mail"]
    password = request.form["password"]

    nuevo_usuario = Usuario(nombre=nombre, mail=mail, password=password)
    session.add(nuevo_usuario)
    session.commit()
    return redirect(url_for("mostrar_usuarios"))

@app.route('/edit_usuario/<int:id>', methods=["GET", "POST"])
def edit_usuario(id):
    usuario = session.query(Usuario).get(id)
    if request.method == "POST":
        usuario.nombre = request.form["nombre"]
        usuario.mail = request.form["mail"]
        usuario.password = request.form["password"]
        session.commit()
        return redirect(url_for("mostrar_usuarios"))
    return render_template("usuario_form.html", usuario=usuario)

@app.route('/delete_usuario/<int:id>', methods=["POST"])
def delete_usuario(id):
    usuario = session.query(Usuario).get(id)
    session.delete(usuario)
    session.commit()
    return redirect(url_for("mostrar_usuarios"))

# -------------------------------
# Ejecución
# -------------------------------
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)