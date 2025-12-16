# conexionBD.py
import mysql.connector

def connectionBD():
    """
    Conexión a TU base de datos
    """
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",           # Tu usuario
            passwd="",             # Tu contraseña (vacía en tu caso)
            database="sistemaweb", # Tu base de datos
            port=3306
        )
        
        if mydb.is_connected():
            print("✅ Conexión exitosa a BD")
            return mydb
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None