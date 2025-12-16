# controllerTareas.py - CREA ESTE ARCHIVO
from conexionBD import *

def listaTareas():
    """Obtiene todas las tareas con información relacionada"""
    try:
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        
        querySQL = """
            SELECT 
                t.id,
                t.nombre,
                t.descripcion,
                t.fecha_inicio,
                t.fecha_fin,
                t.estado_id,
                t.proyecto_id,
                p.nombre as proyecto_nombre,
                e.nombre as estado_nombre
            FROM tareas t
            LEFT JOIN proyectos p ON t.proyecto_id = p.id
            LEFT JOIN estadostarea e ON t.estado_id = e.id
            ORDER BY t.fecha_inicio DESC
        """
        cur.execute(querySQL)
        resultado = cur.fetchall()
        cur.close()
        conexion_MySQLdb.close()
        return resultado
    except Exception as e:
        print(f"Error en listaTareas: {e}")
        return []

def insertarTarea(proyecto_id, nombre, descripcion, fecha_inicio, fecha_fin, estado_id):
    """Inserta una nueva tarea"""
    try:
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor()
        
        sql = """
            INSERT INTO tareas (proyecto_id, nombre, descripcion, fecha_inicio, fecha_fin, estado_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (proyecto_id, nombre, descripcion, fecha_inicio, fecha_fin, estado_id)
        
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        ultimo_id = cursor.lastrowid
        cursor.close()
        conexion_MySQLdb.close()
        return ultimo_id
    except Exception as e:
        print(f"Error en insertarTarea: {e}")
        return 0