Proyecto ExpoCenfo 2024 
Integrantes:  Ariela Jiménez Rodriguez
              Allison Romero Jiménez
              Axel Chavez Olazo
              Anthony


Este proyecto tiene como objetivo desarrollar un visor de aves innovador que va más allá de las funciones de un comedero convencional. Este dispositivo multifuncional no solo atraerá a las aves, sino que también servirá como una herramienta avanzada para la observación y estudio de diversas especies. A través de este visor, los usuarios podrán realizar muestreos de aves de manera precisa y sistemática, lo que permitirá determinar las condiciones de vida de las poblaciones de aves en diferentes entornos.

Además, el visor facilitará la recopilación de datos sobre el comportamiento de las aves, su alimentación, patrones migratorios, y otros aspectos clave que son esenciales para la investigación ecológica. La capacidad de realizar mediciones detalladas permitirá a los investigadores monitorear la salud y la diversidad de las poblaciones de aves a lo largo del tiempo, contribuyendo a la identificación de nuevas especies y la comprensión de la dinámica de las poblaciones existentes.

Este dispositivo será una herramienta invaluable para estudios de conservación, proporcionando datos precisos y de alta calidad sobre las aves en su hábitat natural. Al combinar la observación directa con la recopilación de datos, el visor ayudará a los científicos y conservacionistas a tomar decisiones informadas para la protección de la biodiversidad. De esta manera, el proyecto no solo enriquecerá el conocimiento científico, sino que también promoverá la conservación de las aves y sus ecosistemas, contribuyendo al equilibrio ecológico y al bienestar de nuestro planeta.

Explicación del codigo

Codigo camara:
  Este código configura y utiliza una cámara ESP32 conectada a una red WiFi para transmitir video. A continuación se detalla lo que hace:

Configuración Inicial:
Librerías: Incluye las librerías necesarias para manejar la cámara (esp_camera.h) y para la conexión WiFi (WiFi.h). También incluye un archivo con la configuración de pines de la cámara (camera_pins.h).
Credenciales de WiFi: Define el nombre de la red WiFi (ssid) y la contraseña (password) para conectar el ESP32.
Función setup():
Inicializa la Comunicación Serial: Configura la velocidad de comunicación a 115200 baudios para la depuración y muestra un mensaje inicial.
Configuración de la Cámara: Define y configura los parámetros de la cámara, como los pines utilizados, el tamaño del marco, y la calidad de la imagen. Verifica si el ESP32 tiene PSRAM disponible para ajustar la configuración de la cámara.
Inicializa la Cámara: Intenta inicializar la cámara con la configuración dada. Si hay un error, muestra un mensaje de error en la consola.
Conexión WiFi: Conecta el ESP32 a la red WiFi usando las credenciales proporcionadas. Muestra puntos en la consola mientras espera a que la conexión sea exitosa y luego muestra un mensaje indicando que está conectado.
Inicia el Servidor de la Cámara: Llama a startCameraServer() para iniciar un servidor web que permitirá acceder a la transmisión de video de la cámara.
Muestra la Dirección IP: Imprime la dirección IP local del ESP32 en la consola, que puedes usar para ver la transmisión de video en un navegador web.
Función loop():
Bucle Inactivo: Esta función se ejecuta continuamente pero no realiza ninguna acción específica, ya que todo el procesamiento relacionado con la cámara se maneja en el servidor web.
En resumen, el código configura una cámara ESP32, se conecta a una red WiFi y transmite video a través de un servidor web. Puedes ver el video accediendo a la dirección IP local del ESP32 desde un navegador web.

Codigo Lector
Importaciones: Se importan las librerías board y mfrc522. La librería board se usa para definir los pines de conexión del lector RFID, y mfrc522 es la librería específica para manejar el lector MFRC522.
URL de Redirección: Se define la URL (URL_REDIRECCION) que se mostrará cuando se detecte una tarjeta RFID.
Función leer_tarjeta():
Configuración del Lector: Se crea una instancia del lector MFRC522 usando los pines SCK, MOSI, MISO, RST, y SDA.
Configuración de Antena: Se configura la ganancia de la antena para el lector RFID.
Mensaje de Bienvenida: Se muestra un mensaje inicial que indica que el lector está listo para leer tarjetas.
Bucle de Lectura: En un bucle infinito, el lector solicita la lectura de una tarjeta. Si detecta una tarjeta, obtiene el UID (identificador único) de la tarjeta y lo muestra junto con el tipo de tarjeta.
Mostrar URL: Muestra la URL de redirección cada vez que se detecta una tarjeta.
Manejo de Interrupción: Si el usuario interrumpe el programa (Ctrl+C), se muestra un mensaje indicando que el programa se detuvo.
Bucle Principal: Se ejecuta el bucle infinito llamando a la función leer_tarjeta() para mantener el programa en ejecución y continuamente buscando tarjetas RFID.

Codigo Sensor

Importaciones:
time: Se utiliza para pausar la ejecución del programa entre lecturas.
adafruit_dht: Biblioteca para interactuar con sensores de temperatura y humedad DHT.
board: Define los pines del microcontrolador, aquí se utiliza para especificar el pin al que está conectado el sensor DHT11.
Configuración del Sensor:

Se crea una instancia del sensor DHT11 usando el pin IO27 del microcontrolador.
Bucle Principal:

Lectura de Datos: En cada iteración del bucle, se intenta leer la temperatura y la humedad del sensor.
Impresión de Datos: Se imprimen los valores de temperatura y humedad en la consola con un formato específico.
Manejo de Errores: Si ocurre un error al leer los datos (por ejemplo, si el sensor no está conectado correctamente), se captura y se muestra un mensaje de error.
Espera: El programa espera 1 segundo antes de intentar leer los datos nuevamente para no sobrecargar el sensor con lecturas continuas.
Este código se ejecuta continuamente, leyendo y mostrando la temperatura y humedad cada segundo, y maneja cualquier error que pueda ocurrir durante la lectura del sensor.



Como Utilizarlo

El visor de aves está diseñado para ser una herramienta eficaz en el estudio y monitoreo de aves, combinando un comedero convencional con tecnología avanzada para la captura de datos. A continuación, se describen las características y el uso del visor:

Estructura y Camuflaje: El visor está construido con una estructura diseñada para integrarse de manera natural en el entorno. Su diseño camuflado asegura que el visor sea atractivo para las aves, imitando un comedero común. Este camuflaje ayuda a minimizar la perturbación en el hábitat natural de las aves y maximiza la tasa de visita.

Comedero Interno: En el interior del visor se encuentra un comedero que proporciona alimento a las aves. El diseño del comedero está optimizado para atraer a una variedad de especies, incentivando su presencia y facilitando el muestreo.

Sensor RFID: El visor está equipado con un sensor RFID que permite la detección de aves durante un muestreo de captura y recaptura. Cuando un ave es capturada, se le coloca un dispositivo de reconocimiento RFID con información única. Este dispositivo permite que el sensor registre la presencia del ave cada vez que regresa al comedero.

Cámara de Visualización: El visor incluye una cámara integrada que proporciona una vista en tiempo real de las aves mientras se alimentan. La cámara permite a los investigadores observar el comportamiento de las aves y registrar datos visuales que complementan la información recopilada por el sensor RFID.

Registro y Análisis de Datos: Cada vez que un ave es detectada por el sensor RFID, la información es registrada y almacenada para su análisis posterior. Esto incluye detalles sobre la frecuencia de visitas, la identificación de aves individuales y cualquier otro dato relevante. La cámara también puede capturar imágenes o videos que se utilizan para estudios de comportamiento y salud de las aves.

Mantenimiento y Configuración: Para asegurar un funcionamiento óptimo del visor, es importante realizar un mantenimiento regular. Esto incluye la revisión del comedero para reponer el alimento, verificar el funcionamiento del sensor RFID y la cámara, y asegurarse de que la estructura camuflada se mantenga en buen estado. Además, se recomienda calibrar el sensor y la cámara según sea necesario para ajustar a las condiciones del entorno.

  Pruebas:

