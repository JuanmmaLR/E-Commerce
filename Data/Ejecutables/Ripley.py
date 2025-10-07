import os
import subprocess

# Ruta base para los scripts
BASE_PATH = "C:\\Users\\juanl\\Documents\\WEIDE\\Data\\Ejecutables"
PROCESOS_RIPLEY = [
    "Automático", "Crear_ambiente", "Renombrar", "Transformar",
    "Copiado", "Macro_productos", "Macro_Etiqueta", "Macro_Cierre", "Packing", "Envio_WhatSapp"
]

def mostrar_menu_ripley():
    print("Seleccione el proceso de Ripley que desea ejecutar:")
    for idx, proceso in enumerate(PROCESOS_RIPLEY, 1):
        print(f"{idx}. {proceso}")
    opcion = int(input("Ingrese el número del proceso que desea ejecutar: "))
    return opcion

def ejecutar_proceso_ripley(opcion):
    if 1 <= opcion <= len(PROCESOS_RIPLEY):
        proceso = PROCESOS_RIPLEY[opcion - 1]
        # Si la opción es "Automático", ejecuta todos los pasos en orden
        if proceso == "Automático":
            for proc in PROCESOS_RIPLEY[1:]:
                script_path = os.path.join(BASE_PATH, f"{proc}.py")
                if os.path.exists(script_path):
                    print(f"Ejecutando {proc}.py...")
                    subprocess.run(["python", script_path])
                else:
                    print(f"No se encontró el script: {proc}.py")
        else:
            # Ejecuta un proceso específico
            script_path = os.path.join(BASE_PATH, f"{proceso}.py")
            if os.path.exists(script_path):
                subprocess.run(["python", script_path])
            else:
                print(f"No se encontró el script: {proceso}.py")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    opcion = mostrar_menu_ripley()
    ejecutar_proceso_ripley(opcion)
