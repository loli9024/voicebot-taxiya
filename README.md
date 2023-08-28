# voicebot-taxiya creado por Lorena Diaz
Chatbot construido con DialogFlow para la automatizacion por llamadas telefonicas de servicios de taxi

![image](https://github.com/loli9024/voicebot-taxiya/assets/54463078/2a28ff1e-ba44-491a-a32f-8e9d06f4a463)

# Voicebot para Automatizar Reservas de Taxis

Este es un proyecto que implementa un voicebot creado con Dialogflow CX y Twilio para automatizar las reservas de taxis. Utiliza una base de datos Spanner para almacenar información sobre las solicitudes y direcciones y un webhook para integrar el bot con la base de datos.

## Características

- Automatiza el proceso de reserva de taxis a través de llamadas telefónicas.
- Utiliza Dialogflow CX para la comprensión del lenguaje natural y la generación de respuestas.
- Twilio se encarga de manejar las llamadas telefónicas entrantes y salientes.
- La base de datos Spanner almacena información sobre los usuarios como su direccion, numero de contacto y nombre.
- El webhook se utiliza para interactuar con la base de datos y otros sistemas externos.

## Requisitos

- Cuenta en Dialogflow CX y proyecto configurado.
- Cuenta en Twilio y configuración de números telefónicos.
- Cuenta en Google Cloud Platform y base de datos Spanner configurada.
- Python 3.x instalado.
- Dependencias especificadas en `requirements.txt`.

## Configuración

1. Clona este repositorio a tu máquina local.
2. Configura tu proyecto en Dialogflow CX y obtén las credenciales.
3. Configura tu cuenta en Twilio y obtén los tokens y números telefónicos.
4. Configura tu base de datos Spanner y obtén las credenciales.
5. Crea un entorno virtual y ejecuta `pip install -r requirements.txt`.
6. Configura las credenciales en los archivos relevantes (Dialogflow, Twilio, Spanner).
7. Implementa tu webhook de acuerdo a tus necesidades y endpoints.

## Uso

1. Ejecuta la aplicación localmente: `python app.py`.
2. Configura el webhook URL en Dialogflow CX para apuntar a tu servidor.
3. Prueba el voicebot realizando llamadas y realizando reservas de taxis.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras errores o mejoras potenciales, no dudes en abrir un problema o enviar un pull request.

---

¡Esperamos que este proyecto sea útil y ayude a automatizar las reservas de taxis de manera efectiva! Siéntete libre de personalizar este README según tus necesidades y detalles específicos del proyecto.


