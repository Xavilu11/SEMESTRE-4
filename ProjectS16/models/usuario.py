# Importamos UserMixin de Flask-Login
# UserMixin nos da métodos básicos como:
# - is_authenticated
# - is_active
# - is_anonymous
# - get_id
# Esto facilita que Flask-Login maneje sesiones de usuario.
from flask_login import UserMixin

class Usuario(UserMixin):
    """
    Clase que representa a un usuario del sistema.
    Hereda de UserMixin para integrarse con Flask-Login.
    """

    def __init__(self, id_usuario=None, nombre=None, email=None, password=None):
        # ID único del usuario en la base de datos
        self.id_usuario = id_usuario
        # Nombre del usuario
        self.nombre = nombre
        # Correo electrónico del usuario (campo clave para login)
        self.email = email
        # Contraseña encriptada (hash)
        self.password = password

    def get_id(self):
        """
        Flask-Login requiere este método.
        Debe devolver el ID del usuario como string.
        """
        return str(self.id_usuario)

    def __repr__(self):
        """
        Representación en texto del objeto Usuario.
        Útil para depuración y logs.
        """
        return f"<Usuario {self.id_usuario} - {self.email}>"