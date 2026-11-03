from pathlib import Path
import os
import qrcode
import qrcode.image.svg

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_qr_svg():
    # 1. Definimos la ruta de la carpeta 'qr' en el mismo directorio del script
    directorio_script = Path(__file__).resolve().parent
    carpeta_qr = directorio_script / "qr"
    
    # Creamos la carpeta 'qr' si no existe
    carpeta_qr.mkdir(exist_ok=True)
    
    url = input("Introduzca URL: ").strip()
    if not url:
        print("\n[Error] La URL no puede estar vacía.")
        return

    # Pedimos un nombre opcional para que no se sobrescriban los archivos
    nombre_usuario = input("Nombre para el archivo (pulsa Enter para usar 'qr_code.svg'): ").strip()
    
    if not nombre_usuario:
        nombre_archivo = "qr_code.svg"
    else:
        # Aseguramos que termine en .svg
        nombre_archivo = nombre_usuario if nombre_usuario.endswith(".svg") else f"{nombre_usuario}.svg"

    # Ruta final completa dentro de la carpeta 'qr'
    ruta_salida = carpeta_qr / nombre_archivo

    # Configuramos la factoría para que exporte directamente en formato SVG vectorial
    factory = qrcode.image.svg.SvgPathImage
    
    # Generamos el código QR
    img = qrcode.make(url, image_factory=factory)
    
    # Guardamos el archivo
    img.save(str(ruta_salida))
    print(f"\n¡Código QR generado con éxito y guardado en: '{ruta_salida}'!")

def mostrar_menu():
    while True:
        limpiar_pantalla()
        print("================================")
        print("          MENÚ QR SVG           ")
        print("================================")
        print("1. URL to SVG QR")
        print("2. IMG to SVG")
        print("3. Salir")
        
        fun = input("\nSelect num (1, 2, 3...): ").strip()
        
        if fun == "1":
            limpiar_pantalla()
            print("--- Generar QR desde URL ---")
            generar_qr_svg()
            input("\nPresiona Enter para volver al menú...")
            
        elif fun == "2":
            limpiar_pantalla()
            print("--- IMG to SVG ---")
            print("Próximamente...")
            input("\nPresiona Enter para volver al menú...")
            
        elif fun == "3":
            print("\n¡Saliendo del programa!")
            break
        else:
            input("\nOpción no válida. Presiona Enter para reintentar...")

if __name__ == "__main__":
    mostrar_menu()