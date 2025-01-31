from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def agregar_imagen_a_pagina(pdf_original, imagen, pagina_destino, salida_pdf):
    reader = PdfReader(pdf_original)
    writer = PdfWriter()

    temp_pdf = "temp_image.pdf"
    c = canvas.Canvas(temp_pdf, pagesize=letter)
    c.drawImage(imagen, 0, 0, width=letter[0], height=letter[1])
    c.save()

    for i, page in enumerate(reader.pages):
        if i + 1 == pagina_destino:
            image_reader = PdfReader(temp_pdf)
            page.merge_page(image_reader.pages[0])
        writer.add_page(page)
    with open(salida_pdf, "wb") as f:
        writer.write(f)
        os.remove(temp_pdf)
        print(f"Imagen agregada en la página {pagina_destino} y guardada en: {salida_pdf}")
pdf_original = r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\Modificado0113.pdf"
salida_pdf = r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\M011325.pdf"

imagenes = {
    22: r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\images_AI\octaedro 3.png",
    24: r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\images_AI\Granate Rojo.png",
    29: r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\images_AI\columna1.png",
  108: r"C:\Users\Lenovo\Documents\Amy_imagenes_AI\images_AI\pais de rodocrosita.png"
  } 

pdf_actual = pdf_original
for pagina, imagen in imagenes.items():
    salida_pdf = salida_pdf.replace(".pdf", f"_{pagina}.pdf")
    agregar_imagen_a_pagina(pdf_actual, imagen, pagina, salida_pdf)
    pdf_actual = salida_pdf
os.rename(pdf_actual, salida_pdf)
print(f"Proceso completo. PDF final guardado en: {salida_pdf}")