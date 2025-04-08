import json
import os

# Ruta al archivo datos.json en el escritorio del usuario
ruta_archivo = os.path.join(os.path.expanduser("~"), "Desktop", "datos.json")

try:
    # Abrir y cargar el archivo JSON
    with open(ruta_archivo, 'r') as archivo:
        contenido_json = json.load(archivo)
    
    # Mostrar el contenido (opcional)
    print("✅ Archivo JSON cargado correctamente.\nContenido:")
    print(contenido_json)

except FileNotFoundError:
    print(f"❌ No se encontró el archivo en: {ruta_archivo}")
except json.JSONDecodeError:
    print("❌ Error: El archivo no contiene un JSON válido.")
except Exception as e:
    print(f"❌ Ocurrió un error: {e}")
