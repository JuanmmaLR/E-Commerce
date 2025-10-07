import os
import xlwings as xw
from datetime import datetime

# Ruta de trabajo
BASE_RUTA_TRABAJO = "C:\\Users\\juanl\\Documents\\WEIDE\\Tiendas\\Ripley"

def copiar_hojas():
    # Obtener la fecha actual en el formato DD-MM
    fecha_actual = datetime.now().strftime("%d-%m")
    numeracion = "01"  # Por ejemplo, numeración inicial para el proceso; puedes ajustarlo según sea necesario

    # Crear la ruta dinámica usando la fecha actual
    ruta_trabajo = os.path.join(BASE_RUTA_TRABAJO, datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d"))

    # Ruta de los archivos de origen con el formato de nombre actualizado
    archivo_orders = os.path.join(ruta_trabajo, f"Orders_{fecha_actual}_{numeracion}.xlsm")
    archivo_seller = os.path.join(ruta_trabajo, f"Seller_{fecha_actual}_{numeracion}.xlsm")

    # Ruta del archivo destino con el formato actualizado
    archivo_destino = os.path.join(ruta_trabajo, f"CIERRE_Ripley_{fecha_actual}_{numeracion}.xlsm")

    try:
        with xw.App(visible=False) as app:
            # Abrir el archivo destino (CIERRE_Ripley_DD-MM_NN.xlsm)
            wb_destino = app.books.open(archivo_destino)

            # Eliminar la hoja "Packing SVC" si existe
            if "Packing SVC" in [sheet.name for sheet in wb_destino.sheets]:
                wb_destino.sheets["Packing SVC"].delete()

            # Abrir el archivo Orders_DD-MM_NN.xlsm y copiar su contenido
            wb_orders = app.books.open(archivo_orders)
            hoja_orders = wb_orders.sheets[0]  # La primera hoja en el archivo de Orders
            datos_orders = hoja_orders.range('A1').expand().value  # Copiar todo el rango con datos
            wb_orders.close()

            # Pegar los datos de Orders en la hoja "Ordenes Mirakl" del archivo de destino
            hoja_destino_orders = wb_destino.sheets["Ordenes Mirakl"]
            hoja_destino_orders.range('A1').value = datos_orders  # Pegamos los datos en la hoja de destino

            # Copiar la hoja "Seller" desde Seller_DD-MM_NN.xlsm
            wb_seller = app.books.open(archivo_seller)
            hoja_seller = wb_seller.sheets[0]  # La primera hoja en el archivo de Seller
            hoja_seller.copy(after=wb_destino.sheets["Ordenes Mirakl"])  # Insertar después de "Ordenes Mirakl"
            wb_seller.close()

            # Renombrar la segunda hoja copiada como "Packing SVC"
            hoja_copiada = wb_destino.sheets[1]  # La segunda hoja es la que acabamos de copiar
            hoja_copiada.name = "Packing SVC"

            # Guardar los cambios en el archivo de destino
            wb_destino.save()
            wb_destino.close()

            print(f"Las hojas de {archivo_orders} y {archivo_seller} fueron copiadas con éxito a {archivo_destino} y renombrada la segunda hoja como 'Packing SVC'")

    except Exception as e:
        print(f"Error al copiar las hojas: {e}")

if __name__ == "__main__":
    copiar_hojas()
