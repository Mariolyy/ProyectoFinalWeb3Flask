from random import sample
from conexionBD import *  # Importando conexión BD

# Creando una función para obtener la lista de estadostarea.
def listaProyecto():
    conexion_MySQLdb = connectionBD()  # Creando mi instancia a la conexión de BD
    cur = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = """
        select p.id,
                p.nombre as proyecto,
                p.ubicacion,
                t.nombre as tarea,
                t.fecha_inicio,
                t.fecha_fin,
                et.nombre as estado_tarea
        from tareas t
        join proyectos p on p.id = t.proyecto_id
        join estadostarea et on et.id = t.estado_id
    """
    cur.execute(querySQL)
    resultadoBusqueda = cur.fetchall()  # fetchall() Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda)  # Total de búsqueda

    cur.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

"""
def insertarProyecto(nombre=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    sql = ("INSERT INTO estadostarea(nombre) VALUES (%s)")
    valores = (nombre)
    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()

    resultado_insert = cursor.rowcount  # Retorna 1 o 0
    ultimo_id = cursor.lastrowid  # Retorna el id del último registro
    return resultado_insert
"""

def selectProyecto(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute('''select p.id,
                            p.nombre as proyecto,
                            p.ubicacion,
                            t.nombre as tarea,
                            t.fecha_inicio,
                            t.fecha_fin,
                            et.nombre as estado_tarea
                    from tareas t
                    join proyectos p on p.id = t.proyecto_id
                    join estadostarea et on et.id = t.estado_id
                    where p.id= ='%s'
                    ''' % (id,))
    resultadoQuery = cursor.fetchone()
    cursor.close()
    conexion_MySQLdb.close()

    return resultadoQuery

'''
def actualizarProyecto(nombre):
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)
    cur.execute("""
        UPDATE estadostarea
        SET 
            nombre = %s
        WHERE id=%s
        """, (nombre))
    conexion_MySQLdb.commit()

    cur.close()
    conexion_MySQLdb.close()
    resultado_update = cur.rowcount  # Retorna 1 o 0
    return resultado_update
'''

# Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud = 20
    secuencia = string_aleatorio.upper()
    resultado_aleatorio = sample(secuencia, longitud)
    string_aleatorio = "".join(resultado_aleatorio)
    return string_aleatorio
