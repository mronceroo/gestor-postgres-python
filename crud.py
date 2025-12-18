from database import get_connection

def crear_producto(nombre, precio, stock):
    conn = get_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        
        datos = (nombre, precio, stock)
        
        cursor.execute(sql, datos)
        conn.commit()
        print(f"Producto '{nombre}' guardado ")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
        
def leer_productos():
    conn = get_connection()
    if  conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        sql = "SELECT id, nombre, precio, stock FROM productos"
        cursor.execute(sql)
        
        resultados = cursor.fetchall()
        
        print("Inventario actual")
        for producto in resultados:
            print(f"ID: {producto[0]}, Producto: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]}")
            
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error al leer: {e}")
        
def actualizar_precio(id_producto, nuevo_precio):
    conn = get_connection()
    if  conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        sql = "UPDATE productos SET precio = %s WHERE id = %s"
        
        cursor.execute(sql, (nuevo_precio, id_producto))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Precio actualizado, ID producto: {id_producto}")
        else:
            print(f"No se encontro ningún producto con ID: {id_producto}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error al actualizar: {e}")
        
def eliminar_producto(id_producto):
    conn = get_connection()
    if  conn is None: return
    
    try:
        cursor = conn.cursor()
        
        sql = "DELETE FROM productos WHERE id = %s"

        cursor.execute(sql, (id_producto, ))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Producto con Id: {id_producto}, eliminado correctamente")
        else:
            print(f"No se encontró producto con Id {id_producto}, para eliminar")

        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"Error al eliminar: {e}")
        
if __name__ == "__main__":
    
    print("Estado inicial")
    leer_productos()
    
    id_a_modificar = 13
    nuevo_precio = 52
    
    print(f"Actualizar precio del id: {id_a_modificar}" )
    actualizar_precio(id_a_modificar, nuevo_precio)
    
    id_a_borrar = 14
    
    print(f"Eliminando Id: {id_a_borrar}")
    eliminar_producto(id_a_borrar)
    
    print("Estado final")
    leer_productos()