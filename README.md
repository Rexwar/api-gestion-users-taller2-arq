# 🚀 Configuración del Proyecto

Este proyecto utiliza un archivo `.env` para almacenar configuraciones sensibles y específicas del entorno. Sigue los pasos a continuación para inicializar correctamente el proyecto.

## 📋 Requisitos Previos
- Python 3.8 o superior.
- RabbitMQ instalado o ejecutándose en Docker.

## 🛠 Instalación

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```

2. **Crea un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/MacOS
    .\venv\Scripts\activate   # En Windows
    ```

3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura el archivo `.env`:**
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Copia y completa el siguiente contenido:
      ```env
      FLASK_ENV=development
      FLASK_APP=app.py
      FLASK_DEBUG=1

      RABBITMQ_HOST=localhost
      RABBITMQ_PORT=5672
      RABBITMQ_USER=guest
      RABBITMQ_PASSWORD=guest

      SECRET_KEY=your-secret-key
      ```
    - Cambia los valores según sea necesario para tu entorno.

5. **Inicia RabbitMQ:**
    - Si usas Docker:
      ```bash
      docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
      ```

6. **Prueba la configuración:**
    ```bash
    python tests/test_rabbitmq.py
    ```

## ▶️ Ejecución

Para iniciar la aplicación Flask:
```bash
flask run
```

## 📦 Cargar Variables del `.env` en el Código

Usa la librería `python-dotenv` para cargar automáticamente las variables en el entorno de ejecución. Aquí tienes cómo hacerlo:

1. **Instalar la librería:** Ya lo instalamos con:
    ```bash
    pip install python-dotenv
    ```

2. **Cargar el archivo `.env` en el archivo principal del proyecto (`app.py`):**
    ```python
    from flask import Flask
    from dotenv import load_dotenv
    import os

    # Cargar las variables del archivo .env
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    ```

3. **Acceder a las variables:** Usa `os.getenv()` para obtener las configuraciones en cualquier parte del código:
    ```python
    import os

    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_port = os.getenv('RABBITMQ_PORT')
    ```
