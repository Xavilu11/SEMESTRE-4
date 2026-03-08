import json
import csv

# -------------------------------
# Persistencia en TXT
# -------------------------------
def guardar_txt(productos, ruta="inventario/data/datos.txt"):
    """
    Guarda los productos en un archivo TXT.
    Cada producto se escribe en una línea con formato simple.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        for producto in productos:
            # Convertimos cada producto a texto plano
            archivo.write(f"{producto['id']}, {producto['nombre']}, {producto['color']}, {producto['cantidad']}, {producto['precio']}\n")

def leer_txt(ruta="inventario/data/datos.txt"):
    """
    Lee los productos desde un archivo TXT.
    Devuelve una lista de diccionarios.
    """
    productos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            productos.append({
                "id": int(partes[0]),
                "nombre": partes[1].strip(),
                "color": partes[2].strip(),
                "cantidad": int(partes[3]),
                "precio": float(partes[4])
            })
    return productos


# -------------------------------
# Persistencia en JSON
# -------------------------------
def guardar_json(productos, ruta="inventario/data/datos.json"):
    """
    Guarda los productos en un archivo JSON.
    Convierte la lista de productos a diccionario antes de almacenarla.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

def leer_json(ruta="inventario/data/datos.json"):
    """
    Lee los productos desde un archivo JSON.
    Devuelve una lista de diccionarios.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# -------------------------------
# Persistencia en CSV
# -------------------------------
def guardar_csv(productos, ruta="inventario/data/datos.csv"):
    """
    Guarda los productos en un archivo CSV.
    Cada producto se escribe como una fila.
    """
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        # Escribimos encabezados
        escritor.writerow(["id", "nombre", "color", "cantidad", "precio"])
        # Escribimos cada producto
        for producto in productos:
            escritor.writerow([producto["id"], producto["nombre"], producto["color"], producto["cantidad"], producto["precio"]])

def leer_csv(ruta="inventario/data/datos.csv"):
    """
    Lee los productos desde un archivo CSV.
    Devuelve una lista de diccionarios.
    """
    productos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                "id": int(fila["id"]),
                "nombre": fila["nombre"],
                "color": fila["color"],
                "cantidad": int(fila["cantidad"]),
                "precio": float(fila["precio"])
            })
    return productos