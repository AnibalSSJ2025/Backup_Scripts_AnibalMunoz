# Solicitar dirección IP al usuario
ip = input("Ingresa una dirección IP en formato x.x.x.x (por ejemplo, 192.168.1.1): ")

try:
    # Dividir la IP en octetos
    octetos = ip.split(".")

    # Validar que haya 4 octetos y que cada uno esté entre 0 y 255
    if len(octetos) != 4 or not all(o.isdigit() and 0 <= int(o) <= 255 for o in octetos):
        raise ValueError

    primer_octeto = int(octetos[0])

    # Clasificar la IP según el primer octeto
    if 1 <= primer_octeto <= 126:
        clase = "Clase A"
        descripcion = "Clase A: direcciones para redes muy grandes (hasta 16 millones de hosts)."
    elif 128 <= primer_octeto <= 191:
        clase = "Clase B"
        descripcion = "Clase B: direcciones para redes medianas (hasta 65,000 hosts)."
    elif 192 <= primer_octeto <= 223:
        clase = "Clase C"
        descripcion = "Clase C: direcciones para redes pequeñas (hasta 254 hosts)."
    else:
        clase = "Fuera de la clasificación estándar"
        descripcion = "La IP ingresada no pertenece a una clase A, B o C. Puede ser reservada (como 127.x.x.x o 224+)."

    # Mostrar resultado al usuario
    print("\n📡 Resultado de la clasificación:")
    print(f"📍 Dirección IP ingresada: {ip}")
    print(f"📁 Clasificación: {clase}")
    print(f"ℹ️ Descripción: {descripcion}")

except ValueError:
    print("\n❌ Dirección IP no válida. Asegúrate de ingresarla en el formato correcto (por ejemplo, 192.168.1.1) con valores numéricos entre 0 y 255.")
