# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Declarative Base
Base = declarative_base()

# Clase Producto como modelo ORM
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    color = Column(String)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', color='{self.color}', cantidad={self.cantidad}, precio={self.precio})>"