import paho.mqtt.client as mqtt
import os
import subprocess
import time 

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
        print("Desvaneciendo el brillo de las LEDS...")
        subprocess.Popen(["sudo", "/home/sa/sh/fade.sh"])
    if mensaje == "BRIGHTNESS_HIGH":
        print("Aumentando el Brillo...")
        subprocess.Popen(["sudo", "/home/sa/sh/high.sh"])
    if mensaje == "BRIGHTNESS_LOW":
        print("Disminuyendo el Brillo...")
        subprocess.Popen(["sudo", "/home/sa/sh/low.sh"])
    if mensaje == "CLEAR":
        print("Limpiando...")
        os.system("sudo /home/sa/sh/on17.sh")  
        os.system("sudo /home/sa/sh/on21.sh")
        os.system("sudo /home/sa/sh/on22.sh")
        os.system("sudo /home/sa/sh/on27.sh")
        os.system("sudo pkill -f '/home/sa/sh/onoff.sh'")
        os.system("sudo pkill -f '/home/sa/sh/fade.sh'")
        os.system("sudo pkill -f '/home/sa/sh/high.sh'")
        os.system("sudo pkill -f '/home/sa/sh/low.sh'")
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