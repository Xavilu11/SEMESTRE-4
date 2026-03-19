# models.py
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base
from flask_login import UserMixin

Base = declarative_base()

# -------------------------------
# Clase Producto (tabla productos)
# -------------------------------
class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Producto(id_producto={self.id_producto}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})>"

# -------------------------------
# Clase Usuario (tabla usuarios)
# -------------------------------
class Usuario(UserMixin, Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def get_id(self):
        return str(self.id_usuario)

    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', email='{self.email}')>"