import sys
import os

# Añade la raíz del proyecto al sys.path para que los imports absolutos funcionen
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from GeobizIA.modelo.database.config.constantes_conexion import get_connection_string
import pyodbc

def eliminar_base_datos():
    """
    Elimina completamente la base de datos GeobizIAPruebas.
    ⚠️ ATENCIÓN: Esta operación es IRREVERSIBLE.
    """
    
    print("⚠️  ADVERTENCIA: Vas a eliminar COMPLETAMENTE la base de datos GeobizIAPruebas")
    print("📋 Esto incluye:")
    print("   - Todas las tablas")
    print("   - Todos los datos")
    print("   - Toda la estructura")
    print("   - No hay forma de recuperar los datos después")
    print()
    
    confirmacion = input("¿Estás seguro? Escribe 'ELIMINAR' para confirmar: ")
    
    if confirmacion != "ELIMINAR":
        print("❌ Operación cancelada. No se ha eliminado nada.")
        return False
    
    try:
        # Conexión a master para eliminar la base de datos
        print("\n🔄 Conectando a la base de datos master...")
        master_conn = pyodbc.connect(get_connection_string(database="master"))
        master_cursor = master_conn.cursor()
        
        # Habilita autocommit para ejecutar DROP DATABASE
        master_conn.autocommit = True
        
        print("🔄 Verificando si la base de datos existe...")
        
        # Verificar si la base de datos existe
        master_cursor.execute("SELECT COUNT(*) FROM sys.databases WHERE name = 'GeobizIAPruebas'")
        exists = master_cursor.fetchone()[0]
        
        if exists == 0:
            print("ℹ️  La base de datos 'GeobizIAPruebas' no existe.")
            return False
        
        print("🔄 Cerrando conexiones activas a la base de datos...")
        
        # Cerrar todas las conexiones activas a la base de datos
        kill_connections_sql = """
        ALTER DATABASE GeobizIAPruebas SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
        """
        
        try:
            master_cursor.execute(kill_connections_sql)
            print("✅ Conexiones cerradas correctamente.")
        except Exception as e:
            print(f"⚠️  Advertencia al cerrar conexiones: {e}")
        
        print("🔄 Eliminando la base de datos...")
        
        # Eliminar la base de datos
        drop_database_sql = "DROP DATABASE GeobizIAPruebas;"
        master_cursor.execute(drop_database_sql)
        
        print("✅ Base de datos 'GeobizIAPruebas' eliminada correctamente.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al eliminar la base de datos: {e}")
        return False
        
    finally:
        try:
            master_cursor.close()
            master_conn.close()
            print("🔄 Conexión cerrada.")
        except:
            pass

def eliminar_solo_datos():
    """
    Elimina solo los datos de todas las tablas, pero mantiene la estructura.
    """
    
    print("⚠️  ADVERTENCIA: Vas a eliminar TODOS LOS DATOS de GeobizIAPruebas")
    print("📋 La estructura de las tablas se mantendrá, pero todos los datos serán eliminados.")
    print()
    
    confirmacion = input("¿Estás seguro? Escribe 'LIMPIAR' para confirmar: ")
    
    if confirmacion != "LIMPIAR":
        print("❌ Operación cancelada. No se ha eliminado nada.")
        return False
    
    try:
        from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
        
        print("\n🔄 Conectando a la base de datos...")
        conn = get_connection()
        cursor = conn.cursor()
        
        # Obtener lista de tablas que realmente existen
        print("🔄 Obteniendo lista de tablas...")
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE' 
            AND TABLE_CATALOG = 'GeobizIAPruebas'
            ORDER BY TABLE_NAME
        """)
        
        tablas_existentes = [row[0] for row in cursor.fetchall()]
        
        if not tablas_existentes:
            print("ℹ️  No se encontraron tablas en la base de datos.")
            return False
        
        print(f"📋 Se encontraron {len(tablas_existentes)} tablas:")
        for tabla in tablas_existentes:
            print(f"   - {tabla}")
        
        print("\n🔄 Desactivando restricciones de clave foránea...")
        cursor.execute("EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL'")
        
        print("🔄 Eliminando datos de todas las tablas...")
        
        # Eliminar datos de cada tabla existente
        tablas_limpiadas = 0
        for tabla in tablas_existentes:
            try:
                cursor.execute(f"DELETE FROM [{tabla}]")
                filas_eliminadas = cursor.rowcount
                print(f"✅ {tabla}: {filas_eliminadas} filas eliminadas")
                tablas_limpiadas += 1
            except Exception as e:
                print(f"⚠️  Error en {tabla}: {str(e)[:100]}...")
        
        print(f"\n🔄 Reactivando restricciones de clave foránea...")
        cursor.execute("EXEC sp_MSforeachtable 'ALTER TABLE ? CHECK CONSTRAINT ALL'")
        
        conn.commit()
        close_connection(conn, cursor)
        
        print(f"✅ Datos eliminados correctamente de {tablas_limpiadas}/{len(tablas_existentes)} tablas.")
        print("📊 La estructura de las tablas se mantiene intacta.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al eliminar datos: {e}")
        return False

def crear_archivo_limpieza(sql_path):
    """
    Crea un archivo SQL para limpiar todos los datos de las tablas.
    """
    
    sql_content = """-- Limpieza de datos de GeobizIAPruebas
-- Este archivo elimina todos los datos pero mantiene la estructura

-- Desactivar restricciones de clave foránea temporalmente
EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL';

-- Eliminar datos en orden inverso a las dependencias
DELETE FROM actividad_realizadas;
DELETE FROM actividad_evento;
DELETE FROM actividad_fecha;
DELETE FROM factura_actividad;
DELETE FROM proyecto_actividad;
DELETE FROM publicacion_tag;
DELETE FROM documento_tag;
DELETE FROM tema_ambiental_tag;
DELETE FROM tipo_publicacion_redsocial;
DELETE FROM plantilla_tipo_publicacion;
DELETE FROM auditoria_publicacion;
DELETE FROM log_sistema;
DELETE FROM participantes;
DELETE FROM programaciones;
DELETE FROM actividades;
DELETE FROM eventos;
DELETE FROM proyectos;
DELETE FROM publicaciones;
DELETE FROM documentos;
DELETE FROM plantillas;
DELETE FROM recurso_multimedia;
DELETE FROM tags;
DELETE FROM tema_ambiental;
DELETE FROM tipo_publicacion;
DELETE FROM redsocial;
DELETE FROM facturas;
DELETE FROM generadoria;
DELETE FROM fecha_actividad;
DELETE FROM clientes;
DELETE FROM empresas;
DELETE FROM personas;
DELETE FROM usuarios;
DELETE FROM roles;

-- Reactivar restricciones de clave foránea
EXEC sp_MSforeachtable 'ALTER TABLE ? CHECK CONSTRAINT ALL';

-- Reiniciar contadores de identidad (opcional)
-- DBCC CHECKIDENT('tabla', RESEED, 0);
"""
    
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write(sql_content)
    
    print(f"✅ Archivo de limpieza creado: {sql_path}")

def mostrar_menu():
    """
    Muestra el menú de opciones para el usuario.
    """
    print("\n" + "="*60)
    print("🗑️  GESTIÓN DE ELIMINACIÓN - GeobizIA")
    print("="*60)
    print("1. 💥 Eliminar base de datos completa (IRREVERSIBLE)")
    print("2. 🧹 Limpiar solo datos (mantiene estructura)")
    print("3. ❌ Cancelar y salir")
    print("="*60)
    
    opcion = input("\nSelecciona una opción (1-3): ")
    
    if opcion == "1":
        return eliminar_base_datos()
    elif opcion == "2":
        return eliminar_solo_datos()
    elif opcion == "3":
        print("❌ Operación cancelada.")
        return False
    else:
        print("❌ Opción no válida.")
        return mostrar_menu()

if __name__ == "__main__":
    print("🔒 SCRIPT DE ELIMINACIÓN DE BASE DE DATOS")
    print("⚠️  IMPORTANTE: Lee cuidadosamente antes de proceder")
    print()
    
    try:
        resultado = mostrar_menu()
        
        if resultado:
            print("\n✅ Operación completada exitosamente.")
            print("💡 Recordatorio: Puedes recrear la base de datos ejecutando:")
            print("   - create_db_tables.py (para crear estructura)")
            print("   - insertar_datos_prueba.py (para datos de ejemplo)")
        else:
            print("\n🔄 No se realizaron cambios.")
            
    except KeyboardInterrupt:
        print("\n❌ Operación interrumpida por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    
    input("\nPresiona Enter para salir...")
