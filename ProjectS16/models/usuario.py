class Usuario:
    def __init__(self, id_usuario=None, nombre=None, email=None, password=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<Usuario {self.id_usuario} - {self.nombre}>"