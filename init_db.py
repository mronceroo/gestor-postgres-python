import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def crear_tabla():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        cursor = connection.cursor()

        crear_inventario_sql = """
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL DEFAULT 0,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(crear_inventario_sql)
        connection.commit()
        print("Se creó la tabla")

        cursor.close()
        connection.close()

    except Exception as error:

        print(f"ERROR: {error}")

if __name__ == "__main__":
    crear_tabla()