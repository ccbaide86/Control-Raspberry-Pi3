import paho.mqtt.client as mqtt
import time 
import os
import subprocess
import threading
from fade import fade, stop_fade, adjust_brightness  # Importar funciones de fade.py

# Configuración MQTT
BROKER = "test.mosquitto.org"  # Usamos el mismo broker
PORT = 1883  # Puerto estándar de MQTT
TOPIC = "flet/control"  # El mismo topic que en tu aplicación Flet

# Función de callback cuando el mensaje es recibido
def on_message(client, userdata, msg):
    mensaje = msg.payload.decode().strip()
    print(f"Mensaje recibido: {mensaje}")  # Mostrar el mensaje en consola

    # Evaluar el mensaje y tomar acción
    if mensaje == "RED_LED_ON":
        print("Encendiendo el LED Rojo...")
        os.system("sudo /home/sa/sh/off17.sh") 
        os.system("sudo /home/sa/sh/on21.sh")
        os.system("sudo /home/sa/sh/on22.sh")
        os.system("sudo /home/sa/sh/on27.sh")
    if mensaje == "YELLOW_LED_ON":
        print("Encendiendo el LED Amarillo...")
        os.system("sudo /home/sa/sh/off22.sh")
        os.system("sudo /home/sa/sh/on21.sh")
        os.system("sudo /home/sa/sh/on17.sh")
        os.system("sudo /home/sa/sh/on27.sh")
    if mensaje == "GREEN_LED_ON":
        print("Encendiendo el LED Verde...")
        os.system("sudo /home/sa/sh/off27.sh")
        os.system("sudo /home/sa/sh/on21.sh")
        os.system("sudo /home/sa/sh/on22.sh")
        os.system("sudo /home/sa/sh/on17.sh")
    if mensaje == "BUZZER_ON":
        print("Encendiendo el Timbre...")
        os.system("sudo /home/sa/sh/off21.sh")
        time.sleep(0.3)
        print("Apagando el Timbre...")
        os.system("sudo /home/sa/sh/on21.sh")
    if mensaje == "BLINK":
        print("Parpadeando las LEDS...")
        subprocess.Popen(["sudo", "/home/sa/sh/onoff.sh"])
    if mensaje == "FADE":
            print("Ejecutando Fade...")
            threading.Thread(target=fade).start()
    if mensaje == "BRIGHTNESS_HIGH":
            print("Aumentando brillo...")
            adjust_brightness(10)        
    if mensaje == "BRIGHTNESS_LOW":
            print("Disminuyendo brillo...")
            adjust_brightness(-10)    
    if mensaje == "CLEAR":
        print("Limpiando...")
        os.system("sudo /home/sa/sh/on17.sh")  
        os.system("sudo /home/sa/sh/on21.sh")
        os.system("sudo /home/sa/sh/on22.sh")
        os.system("sudo /home/sa/sh/on27.sh")
        os.system("sudo pkill -f '/home/sa/sh/onoff.sh'")
        stop_fade()
    else:
        print("Mensaje desconocido. Ninguna acción tomada.")

# Crear el cliente MQTT
client = mqtt.Client()

# Establecer la función de callback
client.on_message = on_message

# Conectarse al broker
client.connect(BROKER, PORT)

# Suscribirse al topic
client.subscribe(TOPIC)

# Iniciar el loop para recibir mensajes
print(f"Escuchando en el topic: {TOPIC}")
client.loop_forever()
