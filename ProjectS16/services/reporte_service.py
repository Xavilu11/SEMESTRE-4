from fpdf import FPDF
from services.producto_service import listar_productos

def generar_reporte_productos(nombre_archivo="reporte_productos.pdf"):
    productos = listar_productos()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Reporte de Productos", ln=True, align="C")
    pdf.ln(10)

    # Encabezados
    pdf.cell(40, 10, "ID", 1)
    pdf.cell(80, 10, "Nombre", 1)
    pdf.cell(40, 10, "Precio", 1)
    pdf.cell(30, 10, "Stock", 1)
    pdf.ln()

    # Filas
    for p in productos:
        pdf.cell(40, 10, str(p.id_producto), 1)
        pdf.cell(80, 10, p.nombre, 1)
        pdf.cell(40, 10, str(p.precio), 1)
        pdf.cell(30, 10, str(p.stock), 1)
        pdf.ln()

    pdf.output(nombre_archivo)
    return nombre_archivo