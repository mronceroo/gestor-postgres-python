# Gestor de Inventario con Python y PostgreSQL 

Este proyecto es un sistema CRUD (Crear, Leer, Actualizar, Borrar) backend construido desde cero para aprender la integración profesional entre Python y bases de datos relacionales.

## Tecnologías

* **Python 3.12+**
* **PostgreSQL**: Base de datos relacional.
* **Psycopg2**: Adaptador de base de datos eficiente.
* **Python-Dotenv**: Gestión de seguridad y variables de entorno.
* **UV**: Gestor de paquetes moderno y rápido.

## Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/gestor-postgres-python.git](https://github.com/TU_USUARIO/gestor-postgres-python.git)
    cd gestor-postgres-python
    ```

2.  **Configurar entorno:**
    ```bash
    uv venv
    # Activar entorno (Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate)
    uv sync
    ```

3.  **Variables de Entorno:**
    Crea un archivo `.env` basado en tus credenciales de PostgreSQL:
    ```
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=tu_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

4.  **Ejecutar:**
    ```bash
    python init_db.py  # Para crear la tabla
    python crud.py     # Para probar las operaciones
    ```

## Aprendizajes Clave

* Uso de **Consultas Parametrizadas** para prevenir inyección SQL.
* Manejo de **Transacciones** (Commit/Rollback).
* Arquitectura modular (separación de conexión, configuración y lógica).
