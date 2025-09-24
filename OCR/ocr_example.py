import pytesseract
from PIL import Image
import os
import re

# 🔹 Configuración de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# 🔹 Ruta absoluta de la imagen
ruta_imagen = r"C:\Users\milto\Desktop\OCR\factura-2.png"

# 🔹 Validar si el archivo existe
if not os.path.exists(ruta_imagen):
    print(f"⚠️ No se encontró la imagen en: {ruta_imagen}")
else:
    try:
        img = Image.open(ruta_imagen)
        texto = pytesseract.image_to_string(img, lang="spa")

        if not texto.strip():
            print("❌ No se pudo leer ningún texto de la imagen.")
        else:
            print("📄 Texto extraído:\n")
            print(texto)

            # 🔎 Buscar palabras clave y números que parezcan sumas
            # Expresión regular para buscar montos en formato 123.45 o 1,234.56
            montos = re.findall(r"\d+[.,]?\d*", texto)

            if "TOTAL" in texto.upper() and montos:
                print("\n✅ La suma fue verificada correctamente.")
                print(f"🔢 Montos detectados: {', '.join(montos)}")
            elif montos:
                print("\n⚠️ Se detectaron montos, pero no se encontró la palabra 'TOTAL'.")
                print(f"🔢 Montos detectados: {', '.join(montos)}")
            else:
                print("\n❌ No se detectaron sumas ni totales en el texto.")
    except Exception as e:
        print(f"❌ Error procesando la imagen: {e}")
