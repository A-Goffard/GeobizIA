#!/usr/bin/env python3
"""
Script de depuración para verificar la conexión a la base de datos
y probar la inserción de personas
"""

import sys
import os

# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
from GeobizIA.controlador.dominios.persona import Persona

def test_conexion_bd():
    """Prueba la conexión a la base de datos"""
    print("🔵 Probando conexión a la base de datos...")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Ejecutar una consulta simple
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result and result[0] == 1:
            print("✅ Conexión a la base de datos exitosa")
            
            # Verificar que la tabla persona existe
            cursor.execute("SELECT COUNT(*) FROM persona")
            count = cursor.fetchone()[0]
            print(f"✅ Tabla persona existe con {count} registros")
            
            return True
        else:
            print("❌ Conexión falló")
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False
    finally:
        close_connection(conn, cursor)

def test_insercion_manual():
    """Prueba inserción manual paso a paso"""
    print("🔵 Probando inserción manual...")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Datos de prueba
        datos = (
            "Juan",
            "Pérez",
            "juan@test.com",
            "123456789",
            "12345678A",
            "Calle Test 123",
            "28001",
            "Madrid",
            "España"
        )
        
        print(f"Datos a insertar: {datos}")
        
        # Insertar
        query = """
            INSERT INTO persona (nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(query, datos)
        conn.commit()
        print("✅ Inserción ejecutada correctamente")
        
        # Obtener el ID generado
        cursor.execute("SELECT SCOPE_IDENTITY()")
        result = cursor.fetchone()
        
        if result and result[0]:
            nuevo_id = int(result[0])
            print(f"✅ ID generado: {nuevo_id}")
            
            # Verificar que se insertó correctamente
            cursor.execute("SELECT * FROM persona WHERE id_persona = ?", (nuevo_id,))
            row = cursor.fetchone()
            
            if row:
                print(f"✅ Persona insertada y verificada: {row}")
                return nuevo_id
            else:
                print("❌ No se pudo verificar la inserción")
                return None
        else:
            print("❌ No se pudo obtener el ID generado")
            return None
            
    except Exception as e:
        print(f"❌ Error durante la inserción: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        close_connection(conn, cursor)

def test_con_gestor():
    """Prueba usando el gestor de personas"""
    print("🔵 Probando con gestor de personas...")
    
    try:
        from GeobizIA.controlador.gestores.personas import Personas
        
        gestor = Personas()
        
        persona = Persona(
            id_persona=None,
            nombre="María",
            apellido="García",
            email="maria@test.com",
            telefono="987654321",
            dni="87654321B",
            direccion="Calle Gestor 456",
            cp="28002",
            poblacion="Madrid",
            pais="España"
        )
        
        print(f"Persona a crear: {persona}")
        
        resultado = gestor.agregar(persona)
        
        if resultado:
            print(f"✅ Persona creada exitosamente: {resultado}")
            print(f"ID asignado: {resultado.id_persona}")
            return resultado.id_persona
        else:
            print("❌ El gestor devolvió None")
            return None
            
    except Exception as e:
        print(f"❌ Error con el gestor: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Función principal"""
    print("🚀 Iniciando depuración de base de datos")
    print("=" * 60)
    
    # Paso 1: Probar conexión
    if not test_conexion_bd():
        print("❌ No se puede conectar a la base de datos. Abortando.")
        return
    
    print("\n" + "=" * 60)
    
    # Paso 2: Probar inserción manual
    id_manual = test_insercion_manual()
    
    print("\n" + "=" * 60)
    
    # Paso 3: Probar con gestor
    id_gestor = test_con_gestor()
    
    print("\n" + "=" * 60)
    print("🏁 Depuración completada")
    
    if id_manual and id_gestor:
        print("✅ Ambos métodos funcionaron correctamente")
    elif id_manual:
        print("⚠️ Solo la inserción manual funcionó")
    elif id_gestor:
        print("⚠️ Solo el gestor funcionó")
    else:
        print("❌ Ningún método funcionó")

if __name__ == "__main__":
    main()
