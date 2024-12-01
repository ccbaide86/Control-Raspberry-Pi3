import time
import RPi.GPIO as GPIO

# Pines a utilizar
LED_PINS = [17, 22, 27]

# Variables globales
pwm = {}  # Diccionario para almacenar objetos PWM
fade_running = False
current_brightness = 50  # Nivel inicial de brillo

# Función para inicializar los pines y PWM si no están configurados
def initialize_pwm():
    global pwm
    if not pwm:  # Si el PWM no ha sido configurado aún
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in LED_PINS:
            GPIO.setup(pin, GPIO.OUT)
            pwm[pin] = GPIO.PWM(pin, 1000)  # 1000Hz de frecuencia
            pwm[pin].start(current_brightness)  # Iniciar con el brillo actual

# Función para el efecto de fade
def fade():
    global fade_running, pwm
    fade_running = True

    # Asegurarse de que PWM esté inicializado
    initialize_pwm()

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
        # Apagar LEDs y detener PWM
        for pin in LED_PINS:
            pwm[pin].ChangeDutyCycle(0)
            pwm[pin].stop()
        pwm.clear()  # Limpiar diccionario PWM
        GPIO.cleanup()  # Restablecer configuración de los pines

# Función para detener el efecto de fade
def stop_fade():
    global fade_running
    fade_running = False

# Función para ajustar el brillo
def adjust_brightness(amount):
    global current_brightness
    # Asegurarse de que PWM esté inicializado
    initialize_pwm()

    # Ajustar el nivel de brillo
    current_brightness = max(0, min(100, current_brightness + amount))
    for pin in LED_PINS:
        pwm[pin].ChangeDutyCycle(current_brightness)
    print(f"Brillo ajustado a: {current_brightness}%")
