from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importa los modelos para que SQLAlchemy los reconozca
from .producto import Producto
