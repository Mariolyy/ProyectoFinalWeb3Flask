# controllerProyectos.py - Versión CORREGIDA para tu BD
from conexionBD import connectionBD

def listaProyecto():
    """
    Obtiene proyectos de TU base de datos
    """
    try:
        conexion = connectionBD()
        if not conexion:
            print("⚠️ No hay conexión a BD")
            return []
        
        cursor = conexion.cursor(dictionary=True)
        
        # CONSULTA para TU estructura de BD
        sql = """
        SELECT 
            p.id,
            p.nombre as proyecto,
            p.ubicacion,
            IFNULL(tp.nombre, 'Sin tipo') as tipo_proyecto,
            'En Progreso' as estado
        FROM proyectos p
        LEFT JOIN tiposproyecto tp ON p.id = tp.id
        ORDER BY p.id DESC;
        """
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        print(f"✅ {len(resultados)} proyectos cargados")
        return resultados
        
    except Exception as e:
        print(f"❌ Error en listaProyecto: {e}")
        return []
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass

def obtenerTiposProyecto():
    """
    Obtiene tipos de proyecto de TU tabla
    """
    try:
        conexion = connectionBD()
        if not conexion:
            return []
        
        cursor = conexion.cursor(dictionary=True)
        
        # Tu tabla se llama 'tiposproyecto'
        cursor.execute("SELECT id, nombre FROM tiposproyecto ORDER BY nombre")
        resultados = cursor.fetchall()
        
        if not resultados:
            resultados = [
                {"id": 1, "nombre": "GRANDE"},
                {"id": 2, "nombre": "MEDIANO"},
                {"id": 3, "nombre": "PEQUEÑO"}
            ]
        
        return resultados
        
    except Exception as e:
        print(f"❌ Error en obtenerTiposProyecto: {e}")
        return [
            {"id": 1, "nombre": "Residencial"},
            {"id": 2, "nombre": "Comercial"},
            {"id": 3, "nombre": "Industrial"},
            {"id": 4, "nombre": "Infraestructura"}
        ]
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass

def insertarProyecto(nombre, ubicacion, tipo_id=1, cliente_id=1):
    """
    Inserta proyecto en TU BD
    """
    try:
        conexion = connectionBD()
        if not conexion:
            print("❌ No hay conexión")
            return 0
        
        cursor = conexion.cursor()
        
        # INSERT para TU estructura
        sql = """
        INSERT INTO proyectos (nombre, ubicacion, tipo_proyecto_id, cliente_id)
        VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, ubicacion, tipo_id, cliente_id)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        nuevo_id = cursor.lastrowid
        print(f"✅ Proyecto insertado. ID: {nuevo_id}")
        
        return nuevo_id
        
    except Exception as e:
        print(f"❌ Error al insertar: {e}")
        return 0
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass

def obtenerProyectoPorId(id):
    """
    Obtiene un proyecto específico por su ID
    """
    try:
        conexion = connectionBD()
        if not conexion:
            print("⚠️ No hay conexión a BD")
            return None
        
        cursor = conexion.cursor(dictionary=True)
        
        sql = """
        SELECT 
            p.id,
            p.nombre,
            p.ubicacion,
            p.id,
            IFNULL(tp.nombre, 'Sin tipo') as tipo_proyecto,
            '' as descripcion,
            'En Progreso' as estado
        FROM proyectos p
        LEFT JOIN tiposproyecto tp ON p.id = tp.id
        WHERE p.id = %s
        """
        
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"✅ Proyecto ID {id} encontrado")
        else:
            print(f"⚠️ Proyecto ID {id} no encontrado")
            
        return resultado
        
    except Exception as e:
        print(f"❌ Error en obtenerProyectoPorId: {e}")
        return None
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass

def actualizarProyecto(id, nombre, ubicacion, tipo_id):
    """
    Actualiza un proyecto existente
    """
    try:
        conexion = connectionBD()
        if not conexion:
            print("❌ No hay conexión")
            return False
        
        cursor = conexion.cursor()
        
        sql = """
        UPDATE proyectos 
        SET nombre = %s, ubicacion = %s, id = %s
        WHERE id = %s
        """
        valores = (nombre, ubicacion, id, id)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        print(f"✅ Proyecto ID {id} actualizado")
        return True
        
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")
        return False
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass

def eliminarProyecto(id):
    """
    Elimina un proyecto por su ID
    """
    try:
        conexion = connectionBD()
        if not conexion:
            print("❌ No hay conexión")
            return False
        
        cursor = conexion.cursor()
        
        sql = "DELETE FROM proyectos WHERE id = %s"
        
        cursor.execute(sql, (id,))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ Proyecto ID {id} eliminado")
            return True
        else:
            print(f"⚠️ Proyecto ID {id} no encontrado")
            return False
        
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
        return False
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
        except:
            pass