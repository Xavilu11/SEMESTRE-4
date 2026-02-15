from flask import Flask

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return "Bienvenido a Harta Pinta – Tu espacio creativo"

# Ruta dinámica para productos
@app.route('/producto/<nombre>')
def producto(nombre):
    return f"Producto: {nombre} – disponible en Harta Pinta."

# Catálogo general
@app.route('/catalogo')
def catalogo():
    return "Catálogo de Harta Pinta – Explora nuestras colecciones."

# Ofertas dinámicas
@app.route('/oferta/<codigo>')
def oferta(codigo):
    return f"Oferta especial {codigo} – válida en Harta Pinta."

# Contacto
@app.route('/contacto')
def contacto():
    return "Contáctanos en Harta Pinta – Estamos aquí para ayudarte."

if __name__ == '__main__':
    app.run(debug=True)