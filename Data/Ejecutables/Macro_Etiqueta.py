import os
import datetime
import win32com.client as win32

# Formato de la fecha actual
today = datetime.datetime.today()
year = today.year
month = today.strftime('%m')  # Mes con dos dígitos
day = today.strftime('%d')    # Día con dos dígitos

# Número correlativo que se puede incrementar según se necesite (en este caso es 01)
correlativo = "01"

# Ruta de los archivos
file_path = f"C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley\\{year}\\{month}\\{day}"

# Nombre del archivo con la fecha y el número correlativo
file_name = f"CIERRE_Ripley_{day}-{month}_{correlativo}.xlsm"
file_full_path = os.path.join(file_path, file_name)

# Verificar si el archivo existe
if not os.path.exists(file_full_path):
    print(f"El archivo {file_full_path} no existe.")
else:
    # Abrir Excel
    excel = win32.Dispatch('Excel.Application')
    excel.Visible = False  # No mostrar la ventana de Excel

    # Abrir el archivo
    wb = excel.Workbooks.Open(file_full_path)

    try:
        # Ejecutar la macro
        excel.Application.Run('Generar_Etiquetas')

        # Guardar los cambios (si los hubo) y cerrar
        wb.Save()
    except Exception as e:
        print(f"Error al ejecutar la macro: {e}")
    finally:
        # Cerrar el archivo y Excel
        wb.Close(False)
        excel.Quit()

    print(f"Macro 'Generar_Etiquetas' ejecutada con éxito en {file_full_path}")