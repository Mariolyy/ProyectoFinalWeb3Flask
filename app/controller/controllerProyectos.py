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
        LEFT JOIN tipos_proyecto tp ON p.tipo_id = tp.id
        ORDER BY p.id DESC
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
        
        # Tu tabla se llama 'tipos_proyecto'
        cursor.execute("SELECT id, nombre FROM tipos_proyecto ORDER BY nombre")
        resultados = cursor.fetchall()
        
        if not resultados:
            resultados = [
                {"id": 1, "nombre": "Residencial"},
                {"id": 2, "nombre": "Comercial"},
                {"id": 3, "nombre": "Industrial"},
                {"id": 4, "nombre": "Infraestructura"}
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
        INSERT INTO proyectos (nombre, ubicacion, tipo_id, cliente_id) 
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