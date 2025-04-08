# Lista predefinida de interfaces activas
interfaces_activas = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "FastEthernet1/0"
]

# Solicita al usuario el nombre de la interfaz
interfaz = input("Ingresa el nombre de la interfaz de red (por ejemplo, GigabitEthernet0/0): ")

# Verifica si la interfaz está activa
if interfaz in interfaces_activas:
    print(f"La interfaz {interfaz} está ACTIVA (up).")
else:
    print(f"La interfaz {interfaz} está INACTIVA (down).")
