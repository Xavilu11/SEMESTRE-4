# -------------------------------
# Importaciones principales
# -------------------------------
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

# Importamos modelos y servicios
from models.producto import Producto
from models.usuario import Usuario
from services.producto_service import listar_productos, obtener_producto, crear_producto, actualizar_producto, eliminar_producto
from services.usuario_service import listar_usuarios, obtener_usuario, crear_usuario, actualizar_usuario, eliminar_usuario
from services.reporte_service import generar_reporte_productos

# -------------------------------
# Configuración de la aplicación
# -------------------------------
app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"  # Necesaria para sesiones y mensajes flash

# -------------------------------
# Configuración Flask-Login
# -------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Si no está logueado, redirige a /login

@login_manager.user_loader
def load_user(user_id):
    # Flask-Login necesita esta función para cargar un usuario por su ID
    return obtener_usuario(int(user_id))

# -------------------------------
# Rutas principales
# -------------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

# -------------------------------
# CRUD Productos
# -------------------------------
@app.route('/productos')
@login_required
def listar_productos_view():
    # Obtiene todos los productos de la BD
    productos = listar_productos()
    # Renderiza la plantilla con la lista
    return render_template("productos.html", productos=productos)

@app.route('/productos/crear', methods=["POST"])
@login_required
def crear_producto_view():
    # Recibe datos del formulario HTML
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    # Crea un objeto Producto y lo guarda
    nuevo = Producto(nombre=nombre, precio=precio, stock=stock)
    crear_producto(nuevo)

    flash("Producto creado correctamente")
    return redirect(url_for("listar_productos_view"))

@app.route('/productos/editar/<int:id>', methods=["GET", "POST"])
@login_required
def editar_producto_view(id):
    producto = obtener_producto(id)
    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = request.form["precio"]
        producto.stock = request.form["stock"]
        actualizar_producto(producto)
        flash("Producto actualizado correctamente")
        return redirect(url_for("listar_productos_view"))
    return render_template("producto_form.html", producto=producto)

@app.route('/productos/eliminar/<int:id>', methods=["POST"])
@login_required
def eliminar_producto_view(id):
    eliminar_producto(id)
    flash("Producto eliminado correctamente")
    return redirect(url_for("listar_productos_view"))

# -------------------------------
# Reporte PDF
# -------------------------------
@app.route('/reporte/productos')
@login_required
def reporte_productos():
    archivo = generar_reporte_productos()
    flash("Reporte generado correctamente")
    return send_file(archivo, as_attachment=True)

# -------------------------------
# CRUD Usuarios
# -------------------------------
@app.route('/usuarios')
@login_required
def mostrar_usuarios():
    usuarios = listar_usuarios()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/add_usuario', methods=["POST"])
def add_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
    crear_usuario(nuevo_usuario)
    flash("Usuario registrado correctamente")
    return redirect(url_for("login"))

@app.route('/edit_usuario/<int:id>', methods=["GET", "POST"])
@login_required
def edit_usuario(id):
    usuario = obtener_usuario(id)
    if request.method == "POST":
        usuario.nombre = request.form["nombre"]
        usuario.email = request.form["email"]
        usuario.password = generate_password_hash(request.form["password"])
        actualizar_usuario(usuario)
        return redirect(url_for("mostrar_usuarios"))
    return render_template("usuario_form.html", usuario=usuario)

@app.route('/delete_usuario/<int:id>', methods=["POST"])
@login_required
def delete_usuario_view(id):
    eliminar_usuario(id)
    return redirect(url_for("mostrar_usuarios"))

# -------------------------------
# Autenticación
# -------------------------------
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Busca el usuario en la BD
        usuarios = listar_usuarios()
        usuario = next((u for u in usuarios if u.email == email), None)

        # Verifica contraseña
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
        crear_usuario(nuevo_usuario)
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