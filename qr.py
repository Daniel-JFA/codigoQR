import qrcode
from datetime import datetime, timedelta

def generar_qr(url):
    # Obtener el timestamp actual (momento de creación)
    timestamp_creacion = datetime.now().timestamp()
    #test
    # Agregar el timestamp de creación a la URL
    url_con_timestamp = f"{url}?creacion={timestamp_creacion}"
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_con_timestamp)
    qr.make(fit=True)

    # Crear y guardar la imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")
    print(f"Código QR generado y guardado como 'codigo_qr.png'. Creado en: {datetime.fromtimestamp(timestamp_creacion)}")

def verificar_caducidad(url_escaneada):
    # Extraer el timestamp de creación de la URL
    if "?creacion=" in url_escaneada:
        url, timestamp_creacion = url_escaneada.split("?creacion=")
        timestamp_creacion = float(timestamp_creacion)
        
        # Calcular si ha pasado una hora desde la creación
        tiempo_transcurrido = datetime.now().timestamp() - timestamp_creacion
        if tiempo_transcurrido > 3600:  # 3600 segundos = 1 hora
            print("El código QR ha caducado.")
        else:
            print("El código QR es válido.")
    else:
        print("El código QR no tiene información de creación.")

# Ejemplo de uso
url = "https://forms.gle/VNv8XghTZbiaeDV46"
generar_qr(url)

# Simular el escaneo del código QR después de un tiempo
url_escaneada = "https://forms.gle/VNv8XghTZbiaeDV46?creacion=1697041200.0"  # Ejemplo de URL escaneada
verificar_caducidad(url_escaneada)