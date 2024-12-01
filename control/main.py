import flet as ft
import paho.mqtt.client as mqtt

# Configuración MQTT para el broker público
BROKER = "test.mosquitto.org"  # Broker público
PORT = 1883  # Puerto estándar de MQTT
TOPIC = "flet/control"  # Cambia este topic si lo necesitas

# Función para publicar mensajes al broker
def enviar_mensaje(mensaje):
    try:
        client = mqtt.Client()
        client.connect(BROKER, PORT)
        client.publish(TOPIC, mensaje)
        client.disconnect()
        print(f"Mensaje enviado: {mensaje}")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")

# Crear la interfaz gráfica con Flet
def main(page: ft.Page):
    page.title = "Control MQTT con Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Label para mostrar el texto relacionado con el botón pulsado
    accion_container = ft.Container(
        content=ft.Text(
            value="",  # Texto inicial vacío
            size=24,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        width=275,
        height=75,
        bgcolor=ft.colors.BLUE_GREY_900,
        alignment=ft.alignment.center,
        border=ft.border.all(  # Añadir bordes al rectángulo
            color=ft.colors.WHITE,  # Color del borde
            width=2,
        
    )
)

    # Espaciador entre el rectángulo y los botones
    espacio = ft.Container(height=75)

    # Función para manejar el evento de los botones
    def boton_pulsado(e):
        mensaje = e.control.data  # Obtener el mensaje asociado al botón
        accion_container.content.value = mensaje  # Actualizar el texto dentro del rectángulo
        page.update()  # Actualizar la interfaz
        enviar_mensaje(mensaje)  # Enviar el mensaje como MQTT

    # Especificaciones de los botones
    botones = [
        {"color": ft.colors.RED, "texto": None, "icono": None, "accion": "RED_LED_ON"},
        {"color": ft.colors.YELLOW, "texto": None, "icono": None, "accion": "YELLOW_LED_ON"},
        {"color": ft.colors.BLUE_GREY, "texto": None, "icono": ft.icons.BRIGHTNESS_HIGH, "accion": "BRIGHTNESS_HIGH"},
        {"color": ft.colors.GREEN, "texto": None, "icono": None, "accion": "GREEN_LED_ON"},
        {"color": ft.colors.BLUE_GREY, "texto": None, "icono": ft.icons.VOLUME_UP, "accion": "BUZZER_ON"},
        {"color": ft.colors.BLUE_GREY, "texto": None, "icono": ft.icons.BRIGHTNESS_LOW, "accion": "BRIGHTNESS_LOW"},
        {"color": ft.colors.BLUE_GREY, "texto": "FADE", "icono": None, "accion": "FADE"},
        {"color": ft.colors.BLUE_GREY, "texto": "BLINK", "icono": None, "accion": "BLINK"},
        {"color": ft.colors.BLUE_GREY, "texto": "CLEAR", "icono": None, "accion": "CLEAR"},
    ]

    # Crear la matriz de botones según las especificaciones
    botones_ui = [
        ft.Container(
            content=ft.Text(
                value=b["texto"] if b["texto"] else "",
                color=ft.colors.WHITE if b["texto"] else None,
                size=16 if b["texto"] else None,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            )
            if b["texto"]
            else ft.Icon(
                name=b["icono"],
                size=30,
                color=ft.colors.WHITE,
            ),
            bgcolor=b["color"],
            width=80,
            height=80,
            border_radius=40,  # Hacerlo circular
            alignment=ft.alignment.center,  # Centrar contenido
            data=b["accion"],  # Pasar texto de la acción como dato
            on_click=boton_pulsado,
            tooltip=f"Botón {b['accion']}",
        )
        for b in botones
    ]

    # Organizar los botones en una matriz 3x3
    matriz_botones = ft.Column(
        [
            ft.Row(botones_ui[:3], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row(botones_ui[3:6], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row(botones_ui[6:], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Añadir el Label, el espaciador y la matriz de botones a la página
    page.add(
        ft.Column(
            [
                accion_container,
                espacio,  # Espacio entre el rectángulo y los botones
                matriz_botones,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Ejecutar la aplicación de Flet
if __name__ == "__main__":
    ft.app(target=main)
