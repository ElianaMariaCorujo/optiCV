from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm # Para usar centímetros
import io # Para manejar el archivo en memoria

def crear_cv_pdf(datos):
    
    # Creamos un "buffer" en memoria para guardar el PDF
    buffer = io.BytesIO()

    # Creamos el lienzo (canvas) del PDF, tamaño A4
    c = canvas.Canvas(buffer, pagesize=A4)

    # Obtenemos el ancho y alto de la página
    ancho, alto = A4

    # --- AQUÍ IRÁ TODA LA LÓGICA PARA DIBUJAR EL CV ---

    # Configuramos el título del documento
    c.setTitle(f"CV de {datos.get('nombre_completo', 'Candidato')}")

    # Definimos una posición inicial (ej: 2cm del borde superior)
    y = alto - (2 * cm)
    x = 2 * cm

    # Escribimos el nombre (ejemplo)
    c.setFont("Helvetica-Bold", 18) # Fuente y tamaño
    c.drawString(x, y, datos.get('nombre_completo', 'Nombre no proporcionado'))

    # Bajamos la posición para el siguiente texto
    y = y - (1 * cm) 

    c.setFont("Helvetica", 12)
    c.drawString(x, y, datos.get('email', 'Email no proporcionado'))

    # --- FIN DE LA LÓGICA DE DIBUJO ---

    # Guardamos el PDF en el lienzo
    c.showPage()
    c.save()

    # Rebobinamos el buffer al principio
    buffer.seek(0)

    return buffer