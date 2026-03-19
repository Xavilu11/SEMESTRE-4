# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Declarative Base
Base = declarative_base()

# -------------------------------
# Clase Producto (tabla productos)
# -------------------------------
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    color = Column(String)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return (f"<Producto(id={self.id}, nombre='{self.nombre}', "
                f"color='{self.color}', cantidad={self.cantidad}, precio={self.precio})>")

# -------------------------------
# Clase Usuario (tabla usuarios)
# -------------------------------
class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    mail = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return (f"<Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', "
                f"mail='{self.mail}')>") 