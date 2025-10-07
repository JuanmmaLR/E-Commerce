import os
import xlwings as xw
from datetime import datetime

# Ruta de trabajo base
BASE_RUTA_TRABAJO = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"

def copiar_hoja_tercera():
    # Obtener la fecha actual en el formato DD-MM
    fecha_actual = datetime.now().strftime("%d-%m")
    numeracion = "01"  # Por ejemplo, numeración inicial para el proceso; puedes ajustarlo según sea necesario

    # Crear la ruta dinámica usando la fecha actual
    ruta_trabajo = os.path.join(BASE_RUTA_TRABAJO, datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d"))

    # Ruta de los archivos de origen con el formato de nombre actualizado
    archivo_cierre_ripley = os.path.join(ruta_trabajo, f"CIERRE_Ripley_{fecha_actual}_{numeracion}.xlsm")

    # Ruta del archivo de destino (Ripley_DD-MM_NN.xlsm)
    archivo_destino = os.path.join(ruta_trabajo, f"Ripley_{fecha_actual}_{numeracion}.xlsm")

    try:
        with xw.App(visible=False) as app:
            # Abrir el archivo origen (CIERRE_Ripley_DD-MM_NN.xlsm)
            wb_cierre = app.books.open(archivo_cierre_ripley)
            
            # Identificar la tercera hoja de derecha a izquierda
            hoja_tercera = wb_cierre.sheets[-7]  # La tercera hoja de derecha a izquierda

            # Abrir el archivo destino (Ripley_DD-MM_NN.xlsm)
            wb_destino = app.books.open(archivo_destino)

            # Eliminar la hoja "hoja" si existe en el archivo de destino
            if "hoja" in [sheet.name for sheet in wb_destino.sheets]:
                wb_destino.sheets["hoja"].delete()
                print("Hoja 'hoja' eliminada exitosamente.")

            # Insertar la tercera hoja de CIERRE_Ripley en el archivo de destino
            hoja_tercera.copy(after=wb_destino.sheets[-1])  # Insertar al final de las hojas en el archivo destino

            # Guardar los cambios en el archivo de destino
            wb_destino.save()
            wb_destino.close()

            # Cerrar el archivo origen
            wb_cierre.close()

            print(f"La tercera hoja de {archivo_cierre_ripley} fue copiada exitosamente a {archivo_destino}.")

    except Exception as e:
        print(f"Error al copiar la hoja: {e}")

if __name__ == "__main__":
    copiar_hoja_tercera()
