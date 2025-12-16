# test_db.py
from conexionBD import connectionBD

print("🔍 TEST DE CONEXIÓN A BASE DE DATOS")
print("=" * 50)

try:
    # 1. Probar conexión
    conexion = connectionBD()
    if conexion:
        print("✅ Conexión establecida")
        
        # 2. Verificar base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"📁 Base de datos conectada: {db_name}")
        
        # 3. Ver tablas
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        print(f"\n📋 Tablas disponibles ({len(tablas)}):")
        for tabla in tablas:
            print(f"  - {tabla[0]}")
        
        # 4. Ver estructura de tabla 'proyectos'
        try:
            cursor.execute("DESCRIBE proyectos")
            columnas = cursor.fetchall()
            print(f"\n🗂️  Estructura de 'proyectos':")
            for col in columnas:
                print(f"  {col[0]:20} {col[1]}")
        except:
            print("\n❌ La tabla 'proyectos' no existe")
            
        # 5. Ver datos en 'proyectos'
        try:
            cursor.execute("SELECT COUNT(*) FROM proyectos")
            count = cursor.fetchone()[0]
            print(f"\n📊 Total de proyectos: {count}")
            
            if count > 0:
                cursor.execute("SELECT * FROM proyectos LIMIT 3")
                proyectos = cursor.fetchall()
                print("\n📝 Primeros proyectos:")
                for proy in proyectos:
                    print(f"  ID: {proy[0]}, Nombre: {proy[1]}")
        except Exception as e:
            print(f"\n⚠️ Error al leer proyectos: {e}")
        
        cursor.close()
        conexion.close()
        print("\n✅ Test completado")
    else:
        print("❌ No se pudo establecer conexión")
        
except Exception as e:
    print(f"❌ Error en test: {e}")