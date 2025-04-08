# Solicitar datos al usuario
nombre = input("Ingresa el nombre del dispositivo: ")
ip = input("Ingresa la dirección IP del dispositivo: ")
sistema_operativo = input("Ingresa el sistema operativo del dispositivo: ")
tipo_dispositivo = input("Ingresa el tipo de dispositivo (Router/Switch): ")

# Crear un diccionario con la información
info = {
    "Nombre del dispositivo": nombre,
    "Dirección IP": ip,
    "Sistema Operativo": sistema_operativo,
    "Tipo de dispositivo": tipo_dispositivo
}

# Mostrar la información
print("\nInformación del dispositivo:")
for clave, valor in info.items():
    print(f"{clave}: {valor}")
