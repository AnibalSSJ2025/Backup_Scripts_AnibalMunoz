#!/bin/bash

# Ruta al escritorio del usuario actual
ESCRITORIO="/home/devasc/Desktop"

# Buscar archivos .log en /var/log
find /var/log -type f -name "*.log" | while read archivo; do
    # Obtener el nombre base del archivo
    nombre_archivo=$(basename "$archivo")

    # Copiar el archivo al escritorio
    cp "$archivo" "$ESCRITORIO/$nombre_archivo"

    # Cambiar los permisos a solo lectura para todos (444)
    chmod 444 "$ESCRITORIO/$nombre_archivo"
done

echo "Todos los archivos .log han sido copiados al escritorio con permisos de solo lectura."
