import os
import shutil
from datetime import datetime

# Rutas base
BASE_MACROS = "C:\\Users\\juanl\\Documents\\WEIDE\\Data\\Macros"
BASE_RUTA_TRABAJO = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"
BASE_RUTA_TIENDA = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"

def renombrar_archivos():
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    anio = fecha_actual.strftime("%Y")
    mes = fecha_actual.strftime("%m")
    dia = fecha_actual.strftime("%d")

    # Crear la ruta completa para el directorio de trabajo
    ruta_trabajo = os.path.join(BASE_RUTA_TRABAJO, anio, mes, dia)
    
    # Archivos de macros y otros
    archivo_macro = os.path.join(BASE_MACROS, "CIERRE_Ripley.xlsm")
    archivo_extra = os.path.join(BASE_MACROS, "TTTTT_DD-MM_NN.xlsm")
    
    archivo_destino_macro = os.path.join(ruta_trabajo, f"CIERRE_Ripley_{dia}-{mes}_01.xlsm")
    archivo_destino_extra = os.path.join(ruta_trabajo, f"Ripley_{dia}-{mes}_01.xlsm")

    # Archivos de la tienda
    archivo_orders = os.path.join(BASE_RUTA_TIENDA, f"Orders_01.xlsx")
    archivo_seller = os.path.join(BASE_RUTA_TIENDA, f"Seller_01.csv")

    # Verificar si los archivos existen y copiar
    if os.path.exists(archivo_macro):
        shutil.copy(archivo_macro, archivo_destino_macro)
        print(f"Archivo copiado y renombrado: {archivo_destino_macro}")
    else:
        print(f"No se encontró el archivo de macros: {archivo_macro}")

    if os.path.exists(archivo_extra):
        shutil.copy(archivo_extra, archivo_destino_extra)
        print(f"Archivo copiado y renombrado: {archivo_destino_extra}")
    else:
        print(f"No se encontró el archivo extra: {archivo_extra}")
    
    # Copiar los archivos Orders y Seller
    if os.path.exists(archivo_orders):
        shutil.copy(archivo_orders, os.path.join(ruta_trabajo, f"Orders_{dia}-{mes}_01.xlsx"))
        print(f"Archivo copiado: {archivo_orders}")
    else:
        print(f"No se encontró el archivo Orders: {archivo_orders}")

    if os.path.exists(archivo_seller):
        shutil.copy(archivo_seller, os.path.join(ruta_trabajo, f"Seller_{dia}-{mes}_01.csv"))
        print(f"Archivo copiado: {archivo_seller}")
    else:
        print(f"No se encontró el archivo Seller: {archivo_seller}")

if __name__ == "__main__":
    renombrar_archivos()
