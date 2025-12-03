from random import sample
from conexionBD import *  # Importando conexión BD

# Creando una función para obtener la lista de estadostarea.
def listaEstadosTarea():
    conexion_MySQLdb = connectionBD()  # Creando mi instancia a la conexión de BD
    cur = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM estadostarea ORDER BY id DESC"
    cur.execute(querySQL)
    resultadoBusqueda = cur.fetchall()  # fetchall() Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda)  # Total de búsqueda

    cur.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def insertarEstadosTarea(nombre=''):
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


def selectEstadosTarea(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM estadostarea WHERE id ='%s'" % (id,))
    resultadoQuery = cursor.fetchone()
    cursor.close()
    conexion_MySQLdb.close()

    return resultadoQuery


def actualizarEstadosTarea(nombre):
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


# Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud = 20
    secuencia = string_aleatorio.upper()
    resultado_aleatorio = sample(secuencia, longitud)
    string_aleatorio = "".join(resultado_aleatorio)
    return string_aleatorio
