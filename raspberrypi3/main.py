import threading
import os
import subprocess
import paho.mqtt.client as mqtt
from fade import fade, stop_fade, adjust_brightness  # Importar funciones de fade.py

# Configuración MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "flet/control"

# Función para manejar acciones basadas en mensajes MQTT
def handle_message(mensaje):
    print(f"Procesando mensaje: {mensaje}")
    try:
        if mensaje == "RED_LED_ON":
            print("Encendiendo el LED Rojo...")
            os.system("sudo /home/sa/sh/off17.sh")
            os.system("sudo /home/sa/sh/on21.sh")
            os.system("sudo /home/sa/sh/on22.sh")
            os.system("sudo /home/sa/sh/on27.sh")
        elif mensaje == "YELLOW_LED_ON":
            print("Encendiendo el LED Amarillo...")
            os.system("sudo /home/sa/sh/on22.sh")
        elif mensaje == "GREEN_LED_ON":
            print("Encendiendo el LED Verde...")
            os.system("sudo /home/sa/sh/on27.sh")
        elif mensaje == "BUZZER_ON":
            print("Encendiendo el Timbre...")
            os.system("sudo /home/sa/sh/off21.sh")
            time.sleep(0.3)
            os.system("sudo /home/sa/sh/on21.sh")
        elif mensaje == "BLINK":
            print("Parpadeando las LEDs...")
            subprocess.Popen(["sudo", "/home/sa/sh/onoff.sh"])
        elif mensaje == "CLEAR":
            print("Deteniendo todas las acciones...")
            stop_fade()
            os.system("sudo pkill -f '/home/sa/sh/onoff.sh'")
        elif mensaje == "FADE":
            print("Ejecutando Fade...")
            threading.Thread(target=fade).start()
        elif mensaje == "BRIGHTNESS_LOW":
            print("Disminuyendo brillo...")
            adjust_brightness(-10)
        elif mensaje == "BRIGHTNESS_HIGH":
            print("Aumentando brillo...")
            adjust_brightness(10)
        else:
            print("Mensaje desconocido. Ninguna acción tomada.")
    except Exception as e:
        print(f"Error al procesar el mensaje '{mensaje}': {e}")

# Función de callback cuando el mensaje es recibido
def on_message(client, userdata, msg):
    mensaje = msg.payload.decode().strip()
    print(f"Mensaje recibido: {mensaje}")
    handle_message(mensaje)

# Crear el cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)

# Iniciar el loop para recibir mensajes
print(f"Escuchando en el topic: {TOPIC}")
client.loop_forever()
