# Password Generator API

Este proyecto es una API sencilla creada con FastAPI que genera contraseñas seguras basadas en parámetros especificados por el usuario. La API valida los parámetros de entrada y asegura que las contraseñas generadas cumplan con los requisitos de longitud, cantidad de letras minúsculas, letras mayúsculas y dígitos.

## Requisitos

- Python 3.7+
- FastAPI
- Pydantic
- Starlette

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Cómo ejecutar la API

1. Inicia el servidor con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. La API estará disponible en `http://127.0.0.1:8000`.

