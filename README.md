# Proyecto OrionTek - Prueba Técnica

Bienvenido al repositorio de la Prueba Técnica del Proyecto OrionTek, una aplicación web desarrollada con Django para demostrar habilidades básicas en la gestión de usuarios y sus direcciones.

## Características

- **Gestión de Usuarios:** Permite la creación y visualización de usuarios.
- **Gestión de Direcciones:** Cada usuario puede tener asociadas una o más direcciones.
- **Listado de Usuarios:** Muestra una lista de usuarios junto con sus direcciones asociadas.

## Tecnologías Utilizadas

- Django: Framework de desarrollo web en Python.
- SQLite: Sistema de gestión de bases de datos para almacenar la información de usuarios y direcciones.
- HTML & CSS: Para la estructura y estilo de la interfaz de usuario.

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona el repositorio:
git clone git@github.com:Keysie27/OriontekTest.git

2. Navega al directorio del proyecto:
cd OriontekTest

3. Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate

4. Instala las dependencias:
pip install -r requirements.txt

5. Realiza las migraciones de la base de datos:
python manage.py migrate

6. Ejecuta el servidor de desarrollo:
python manage.py runserver

7. Abre un navegador y visita `http://127.0.0.1:8000/` o el puerto asignado para interactuar con la aplicación.
