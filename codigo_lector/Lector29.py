import board
import mfrc522

# UID de la tarjeta permitida en formato de lista de bytes
UID_PERMITIDO = [0xA3, 0x34, 0x0B, 0x30, 0xAC]  # Reemplaza este UID con el UID correcto de tu tarjeta

def verificar_acceso():
    """
    Función que verifica si una tarjeta tiene acceso permitido.

    Esta función se encarga de:
      - Configurar el lector MFRC522.
      - Solicitar la lectura de la tarjeta.
      - Obtener el identificador único (UID) de la tarjeta.
      - Comparar el UID leído con el UID permitido.
      - Mostrar un mensaje de acceso permitido o denegado.

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
    print("Acerque la tarjeta al lector para verificar el acceso")
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

                    # Verifica si el UID leído coincide con el UID permitido
                    if uid == UID_PERMITIDO:
                        print("Acceso Permitido")
                    else:
                        print("Acceso Denegado")
                        print(f"UID esperado: {UID_PERMITIDO}")
                        print(f"UID leído: {uid}")

    except KeyboardInterrupt:
        print("Detenido por Ctrl+C")

# Bucle infinito para verificar el acceso
while True:
    verificar_acceso()
