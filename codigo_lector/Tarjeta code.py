import board
import mfrc522

# La URL a la que deseas redirigir
URL_REDIRECCION = "http://192.168.42.22"

def leer_tarjeta():
    """
    Función que detecta una tarjeta RFID y muestra la URL deseada.

    Esta función se encarga de:
      - Configurar el lector MFRC522.
      - Solicitar la lectura de la tarjeta.
      - Obtener el identificador único (UID) de la tarjeta.
      - Mostrar la URL deseada cuando se detecta una tarjeta.

    No retorna ningún valor.
    """

    # Crea una instancia del lector MFRC522
    lector = mfrc522.MFRC522(
        board.SCK,  # Pin SCK
        board.MOSI,  # Pin MOSI
        board.MISO,  # Pin MISO
        board.IO4,   # Pin RST
        board.IO5,   # Pin SDA
    )

    # Configura la ganancia de la antena
    lector.set_antenna_gain(0x07 << 4)

    # Mensaje de bienvenida
    print('')
    print("Acerque la tarjeta al lector para mostrar la URL")
    print('')

    try:
        while True:
            # Solicita la lectura de una tarjeta compatible
            estado, tipo_tarjeta = lector.request(lector.REQIDL)

            if estado == lector.OK:
                # Obtiene el identificador único (UID) de la tarjeta
                estado, uid = lector.anticoll()

                if estado == lector.OK:
                    # Imprime el UID leído en un formato que puedas verificar
                    uid_leido = "0x%02x%02x%02x%02x" % (uid[0], uid[1], uid[2], uid[3])
                    print("Tarjeta detectada")
                    print("  - Tipo de tarjeta: 0x%02x" % tipo_tarjeta)
                    print("  - UID leído: " + uid_leido)
                    print('')

                    # Muestra la URL deseada
                    print(f"Redirigiendo a: {URL_REDIRECCION}")

    except KeyboardInterrupt:
        print("Detenido por Ctrl+C")

# Bucle infinito para leer la tarjeta
while True:
    leer_tarjeta()
