# Control de FLET con Mensajería MQTT y NODE-RED en Raspberry Pi

Este proyecto implementa un sistema de control utilizando **FLET**, **MQTT**, **Node-RED** y una **Raspberry Pi 3**. La Raspberry recibe mensajes MQTT y ejecuta scripts de shell para realizar diversas tareas.

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos Previos](#requisitos-previos)
3. [Uso del Proyecto](#uso-del-proyecto)
   - [Interfaz FLET](#interfaz-flet)
   - [Configuración Node-RED](#configuración-node-red)
   - [Ejecución en Raspberry Pi](#ejecución-en-raspberry-pi)


---

## Descripción del Proyecto

Este proyecto permite la integración de una interfaz gráfica hecha con **FLET** para enviar comandos mediante **MQTT** hacia un servidor **Node-RED**. Los comandos son procesados en una Raspberry Pi, que ejecuta scripts de shell según el mensaje recibido. Es ideal para automatización y control remoto de tareas.

---

## Requisitos Previos

Antes de usar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior** (en la máquina con FLET y en la Raspberry Pi).
- **FLET** (para la interfaz gráfica).
- **Node-RED** (para gestionar los flujos de mensajes MQTT).
- **Mosquitto MQTT Broker** (o cualquier broker MQTT que prefieras).
- **Scripts de Shell** configurados en la Raspberry.
- **Permisos sudo** en la Raspberry para ejecutar comandos específicos.

---

## Uso del Proyecto

### Interfaz FLET
pip install flet 
pip install paho-mqtt


### Interfaz FLET para dispositivo movil 
python.exe -m venv .venv
.venv\Scripts\activate.bat

cd mi-app - **Colocar el directorio de tu app de flet**

flet run --android - **Escanea el codigo QR y no olvides instalar la app de FLET para un mejor uso en movil**

### Configuración Node-RED

#### Dependencias

**Node.js**: Node-RED requiere Node.js para funcionar. Instálalo en tu máquina (Linux, macOS o Windows):
   - En Linux:
     ```bash
     sudo apt update
     sudo apt install -y nodejs npm
     ```
   - En macOS (con Homebrew):
     ```bash
     brew install node
     ```
   - En Windows:
     - Descarga e instala Node.js desde [Node.js Downloads](https://nodejs.org).

### Ejecutar Node-RED y Pegar el Flow

#### Pasos para usar Node-RED

1. Abre tu **Command Prompt** o terminal.
2. Ejecuta el siguiente comando para iniciar Node-RED:
   ```bash
   node-red
3. Espera a que el servidor de Node-RED se inicie. Deberías ver un mensaje indicando que la interfaz está disponible en http://127.0.0.
En la interfaz de Node-RED, haz clic en el ícono del Menú (esquina superior derecha, representado por tres líneas horizontales).
Selecciona Import > Clipboard.
Abre el archivo flows.json ubicado en la carpeta node-red de tu repositorio con un editor de texto, copia todo su contenido, y pégalo en la ventana emergente de Node-RED.
Haz clic en Importar para cargar el flujo.
4. Configurar y Desplegar el Flujo
Verifica que todos los nodos estén correctamente configurados, especialmente los nodos MQTT (broker, puerto, credenciales, etc.).
Haz clic en el botón Deploy (esquina superior derecha) para desplegar los cambios.
5. Probar el Flujo
Tu flujo ahora está activo y listo para recibir mensajes. Puedes probar su funcionalidad enviando mensajes MQTT desde herramientas como mosquitto_pub o desde la interfaz de FLET.

### Configuracion de la RASPBERRY-PI3

# Exportar Proyecto a Raspberry Pi

Este README detalla los pasos para transferir las carpetas necesarias del repositorio a una Raspberry Pi y configurarlas correctamente para el usuario `sa`.

---

## Archivos a Exportar

Del repositorio, debes transferir las siguientes carpetas y archivos:

1. **Carpeta `raspberry3`**: Contiene los scripts y configuraciones necesarios para la ejecución del proyecto.
2. **Carpeta `sh`**: Contiene los scripts de shell que se ejecutarán en la Raspberry Pi.

---

## Requisitos Previos

1. Asegúrate de tener acceso al usuario `sa` en la Raspberry Pi con permisos `sudo`.
2. Habilita SSH en la Raspberry Pi para transferir los archivos desde tu máquina local:










