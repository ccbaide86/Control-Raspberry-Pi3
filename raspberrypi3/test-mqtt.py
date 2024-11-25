import paho.mqtt.client as mqtt

# Configuración MQTT
BROKER = "test.mosquitto.org"  # Usamos el mismo broker
PORT = 1883  # Puerto estándar de MQTT
TOPIC = "flet/control"  # El mismo topic que en tu aplicación Flet

# Función de callback cuando el mensaje es recibido
def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}")  # Mostrar el mensaje en consola

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
