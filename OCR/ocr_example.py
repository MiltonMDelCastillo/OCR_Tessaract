import pytesseract
from PIL import Image
import os

# 🔹 Solo necesario en Windows: indicar dónde está tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🔹 Ruta absoluta de la imagen
ruta_imagen = r"C:\Users\milto\Desktop\OCR\factura-2.png"

# 🔹 Validar si el archivo existe
if not os.path.exists(ruta_imagen):
    print(f"⚠️ No se encontró la imagen en: {ruta_imagen}")
else:
    img = Image.open(ruta_imagen)
    texto = pytesseract.image_to_string(img, lang="spa")
    print("Texto extraído:\n")
    print(texto)
