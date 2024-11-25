import time
import RPi.GPIO as GPIO

# Configuración de los pines
LED_PINS = [17, 22, 27]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Configuración PWM para los LEDs
pwm = {}
for pin in LED_PINS:
    pwm[pin] = GPIO.PWM(pin, 1000)  # 1000Hz de frecuencia
    pwm[pin].start(100)  # Comienza con brillo apagado

# Variables globales
fade_running = False
current_brightness = 50  # Nivel inicial de brillo

# Función para el efecto de fade
def fade():
    global fade_running
    fade_running = True
    try:
        while fade_running:
            for dc in range(0, 101, 5):  # Subir brillo
                if not fade_running:
                    break
                for pin in LED_PINS:
                    pwm[pin].ChangeDutyCycle(dc)
                time.sleep(0.25)
            for dc in range(100, -1, -5):  # Bajar brillo
                if not fade_running:
                    break
                for pin in LED_PINS:
                    pwm[pin].ChangeDutyCycle(dc)
                time.sleep(0.25)
    finally:
        for pin in LED_PINS:
            pwm[pin].ChangeDutyCycle(0)

# Función para detener el efecto de fade
def stop_fade():
    global fade_running
    fade_running = False

# Función para ajustar el brillo
def adjust_brightness(amount):
    global current_brightness
    current_brightness = max(0, min(100, current_brightness + amount))
    for pin in LED_PINS:
        pwm[pin].ChangeDutyCycle(current_brightness)
    print(f"Brillo ajustado a: {current_brightness}%")
