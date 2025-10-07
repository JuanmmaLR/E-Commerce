import os
import subprocess

# Rutas de los ejecutables
BASE_PATH = "C:\\Users\\juanl\\Documents\\WEIDE\\Data\\Ejecutables"
TIENDAS = ["WEIDE", "Ripley", "Falabella", "Paris", "Dafiti", "Hites", "SAC", "Cierre"]

def mostrar_menu():
    print("Seleccione una opción:")
    for idx, tienda in enumerate(TIENDAS, 1):
        print(f"{idx}. {tienda}")
    opcion = int(input("Ingrese el número de la tienda que desea procesar: "))
    return opcion

def ejecutar_opcion(opcion):
    if 1 <= opcion <= len(TIENDAS):
        tienda = TIENDAS[opcion - 1]
        script_path = os.path.join(BASE_PATH, f"{tienda}.py")
        if os.path.exists(script_path):
            print(f"Ejecutando proceso para la tienda: {tienda}...")
            subprocess.run(["python", script_path])
            print(f"Felicitaciones, proceso terminado y picking {tienda} enviado.")
        else:
            print(f"No se encontró el script para la tienda seleccionada: {tienda}")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    opcion = mostrar_menu()
    ejecutar_opcion(opcion)
