from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import io

def crear_cv_pdf(datos):

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    ancho, alto = A4

    c.setTitle(f"CV de {datos.get('nombre_completo', 'Candidato')}")

    y = alto - (2 * cm)
    x = 2 * cm

    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, datos.get('nombre_completo', 'Nombre no proporcionado'))

    y = y - (1 * cm) 
    c.setFont("Helvetica", 12)
    c.drawString(x, y, datos.get('email', 'Email no proporcionado'))

    # (Aquí puedes añadir más lógica para dibujar el resto de los datos)
    # por ejemplo:
    y = y - (0.5 * cm)
    c.drawString(x, y, datos.get('telefono', ''))

    y = y - (1 * cm)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Resumen Profesional")
    y = y - (0.5 * cm)
    c.setFont("Helvetica", 10)

    # Lógica simple para texto multi-línea (ReportLab es complejo para esto)
    resumen_lineas = datos.get('resumen', '').split('\n')
    for linea in resumen_lineas:
        c.drawString(x, y, linea)
        y = y - (0.4 * cm) # Espacio entre líneas del resumen

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer