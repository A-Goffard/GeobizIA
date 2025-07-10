#!/usr/bin/env python3
"""
Script de diagnóstico para debugging del problema de creación de cliente
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.validaciones.validar_persona import validar_datos_persona

def test_crear_persona():
    """Test para diagnosticar el problema de creación de persona"""
    print("=== DIAGNÓSTICO DE CREACIÓN DE PERSONA ===")
    
    # Datos de prueba similares a los del formulario
    datos_prueba = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'email': 'juan@test.com',
        'telefono': '123456789',
        'dni': '12345678A',
        'direccion': 'Calle Test 123',
        'cp': '08001',
        'poblacion': 'Barcelona',
        'pais': 'España'
    }
    
    print(f"Datos de prueba: {datos_prueba}")
    
    # 1. Validar datos
    print("\n1. Validando datos...")
    es_valido, mensaje = validar_datos_persona(datos_prueba)
    print(f"   Validación: {es_valido}")
    if not es_valido:
        print(f"   Error de validación: {mensaje}")
        return False
    
    # 2. Crear objeto Persona
    print("\n2. Creando objeto Persona...")
    try:
        persona = Persona(
            id_persona=None,
            nombre=datos_prueba['nombre'],
            apellido=datos_prueba['apellido'],
            email=datos_prueba['email'],
            telefono=datos_prueba['telefono'],
            dni=datos_prueba['dni'],
            direccion=datos_prueba['direccion'],
            cp=datos_prueba['cp'],
            poblacion=datos_prueba['poblacion'],
            pais=datos_prueba['pais']
        )
        print(f"   Persona creada: {persona}")
    except Exception as e:
        print(f"   Error al crear objeto Persona: {e}")
        return False
    
    # 3. Probar agregar a la base de datos
    print("\n3. Intentando agregar a la base de datos...")
    try:
        gestor = Personas()
        resultado = gestor.agregar(persona)
        
        if resultado:
            print(f"   ✅ Persona agregada exitosamente con ID: {resultado.id_persona}")
            return True
        else:
            print(f"   ❌ Error: gestor.agregar() devolvió None")
            return False
            
    except Exception as e:
        print(f"   ❌ Excepción al agregar persona: {e}")
        return False

def test_conexion_db():
    """Test básico de conexión a la base de datos"""
    print("\n=== TEST DE CONEXIÓN A LA BASE DE DATOS ===")
    try:
        from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Test básico
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        close_connection(conn, cursor)
        
        print(f"✅ Conexión exitosa, resultado: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando diagnóstico...")
    
    # Test conexión
    if not test_conexion_db():
        print("❌ Error en conexión básica, abortando...")
        sys.exit(1)
    
    # Test creación de persona
    if test_crear_persona():
        print("\n✅ Todos los tests pasaron correctamente")
    else:
        print("\n❌ Hay problemas en la creación de persona")
        sys.exit(1)
