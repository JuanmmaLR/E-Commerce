import os
from datetime import datetime

# Ruta base de la estructura de carpetas
BASE_PATH = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"

def crear_estructura_directorios():
    # Obtener la fecha actual para definir AAAA, MM y DD
    fecha_actual = datetime.now()
    anio = fecha_actual.strftime("%Y")
    mes = fecha_actual.strftime("%m")
    dia = fecha_actual.strftime("%d")

    # Construir la ruta completa
    ruta_completa = os.path.join(BASE_PATH, anio, mes, dia)

    # Crear cada nivel de directorio si no existe
    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        print(f"Ruta creada: {ruta_completa}")
    else:
        print(f"La ruta ya existe: {ruta_completa}")

if __name__ == "__main__":
    crear_estructura_directorios()
