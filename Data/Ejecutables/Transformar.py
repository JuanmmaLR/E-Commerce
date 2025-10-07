import os
import xlwings as xw
from datetime import datetime

# Ruta de trabajo
BASE_RUTA_TRABAJO = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"

def transformar_archivos():
    # Obtener la fecha actual en el formato YYYY-MM-DD
    fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Usar YYYY-MM-DD

    # Crear la ruta dinámica
    ruta_trabajo = os.path.join(BASE_RUTA_TRABAJO, fecha_actual.split('-')[0], fecha_actual.split('-')[1], fecha_actual.split('-')[2])

    # Verificar si la ruta existe
    if not os.path.exists(ruta_trabajo):
        print(f"La ruta {ruta_trabajo} no existe.")
        return

    # Recorremos todos los archivos en la carpeta de trabajo
    for archivo in os.listdir(ruta_trabajo):
        archivo_completo = os.path.join(ruta_trabajo, archivo)

        # Verificamos si el archivo es de Excel o CSV
        if archivo.endswith('.xlsx') or archivo.endswith('.csv'):
            try:
                # Abrir el archivo usando xlwings si es .xlsx o .csv
                with xw.App(visible=False) as app:
                    wb = app.books.open(archivo_completo)

                    # Determinamos el nuevo nombre del archivo como .xlsm
                    archivo_nuevo = archivo_completo.replace('.xlsx', '.xlsm').replace('.csv', '.xlsm')
                    wb.save(archivo_nuevo)
                    print(f"Archivo transformado: {archivo_nuevo}")

                    wb.close()

                    # Eliminar el archivo original .xlsx o .csv después de la conversión
                    os.remove(archivo_completo)
                    print(f"Archivo original eliminado: {archivo_completo}")

            except Exception as e:
                print(f"Error al procesar el archivo {archivo_completo}: {e}")

if __name__ == "__main__":
    transformar_archivos()

