import qrcode
import qrcode.image.svg

def generar_qr_svg():
    url=input("Introduzca URL: ")
    nombre_archivo="qr_code.svg"
    # Configuramos la factoría para que exporte directamente en formato SVG vectorial
    factory = qrcode.image.svg.SvgPathImage
    # Generamos el código QR
    img = qrcode.make(url, image_factory=factory)
    # Guardamos el archivo
    img.save(nombre_archivo)
    print(f"¡Código QR generado con éxito y guardado como '{nombre_archivo}'!")
    

print("MENU")
print("1.URL to SVG QR")
print("2.IMG to SVG")
fun=input("Select num (1,2,3,...): ")

if fun == "1":
    generar_qr_svg()
        