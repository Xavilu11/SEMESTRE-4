from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

# Definimos el formulario para productos
class ProductoForm(FlaskForm):
    # Campo para el nombre del producto
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(min=2, max=100, message="El nombre debe tener entre 2 y 100 caracteres")
    ])

    # Campo para el precio del producto
    precio = DecimalField("Precio", validators=[
        DataRequired(message="El precio es obligatorio"),
        NumberRange(min=0, message="El precio debe ser mayor o igual a 0")
    ])

    # Campo para el stock del producto
    stock = IntegerField("Stock", validators=[
        DataRequired(message="El stock es obligatorio"),
        NumberRange(min=0, message="El stock debe ser mayor o igual a 0")
    ])

    # Botón para enviar el formulario
    submit = SubmitField("Guardar")