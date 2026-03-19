# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import inventario.bd as bd
from models import Base, Producto, Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"

# -------------------------------
# Configuración SQLAlchemy con MySQL
# -------------------------------
engine = create_engine("mysql+mysqlconnector://root:@localhost/sistema_tienda", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# Configuración Flask-Login
# -------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return session.query(Usuario).get(int(user_id))

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

# -------------------------------
# CRUD Productos
# -------------------------------
@app.route('/add', methods=["POST"])
@login_required
def add():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
    session.add(nuevo_producto)
    session.commit()
    return redirect(url_for("index"))
@app.route('/datos/sqlalchemy')
@login_required
def datos_sqlalchemy():
    productos = session.query(Producto).all()
    return render_template("productos.html", productos=productos)

# -------------------------------
# CRUD Usuarios
# -------------------------------
@app.route('/usuarios')
@login_required
def mostrar_usuarios():
    usuarios = session.query(Usuario).all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/add_usuario', methods=["POST"])
def add_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])

    nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
    session.add(nuevo_usuario)
    session.commit()
    flash("Usuario registrado correctamente")
    return redirect(url_for("login"))

@app.route('/edit_usuario/<int:id>', methods=["GET", "POST"])
@login_required
def edit_usuario(id):
    usuario = session.query(Usuario).get(id)
    if request.method == "POST":
        usuario.nombre = request.form["nombre"]
        usuario.email = request.form["email"]
        usuario.password = generate_password_hash(request.form["password"])
        session.commit()
        return redirect(url_for("mostrar_usuarios"))
    return render_template("usuario_form.html", usuario=usuario)

@app.route('/delete_usuario/<int:id>', methods=["POST"])
@login_required
def delete_usuario(id):
    usuario = session.query(Usuario).get(id)
    session.delete(usuario)
    session.commit()
    return redirect(url_for("mostrar_usuarios"))

# -------------------------------
# Autenticación
# -------------------------------
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        usuario = session.query(Usuario).filter_by(email=email).first()
        if usuario and check_password_hash(usuario.password, password):
            login_user(usuario)
            flash("Inicio de sesión exitoso")
            return redirect(url_for("index"))
        else:
            flash("Credenciales inválidas")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada")
    return redirect(url_for("login"))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        session.add(nuevo_usuario)
        session.commit()
        flash("Registro exitoso, ahora puedes iniciar sesión")
        return redirect(url_for("login"))
    return render_template("register.html")

# -------------------------------
# Ejecución
# -------------------------------
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)