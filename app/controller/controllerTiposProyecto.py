# controller/controllerTiposProyecto.py
from conexionBD import *

def listaTiposProyecto():
    """Obtiene la lista de tipos de proyecto"""
    try:
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        
        querySQL = "SELECT id, nombre FROM tiposproyecto ORDER BY nombre"
        cur.execute(querySQL)
        resultado = cur.fetchall()
        
        cur.close()
        conexion_MySQLdb.close()
        return resultado
    except Exception as e:
        print(f"Error en listaTiposProyecto: {e}")
        # Datos de ejemplo si la tabla no existe
        return [
            {"id": 1, "nombre": "Residencial"},
            {"id": 2, "nombre": "Comercial"},
            {"id": 3, "nombre": "Industrial"},
            {"id": 4, "nombre": "Infraestructura"}
        ]