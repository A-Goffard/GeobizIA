#!/usr/bin/env python3
"""
Script de prueba para verificar que el problema de creación de clientes se ha solucionado
"""

import sys
import os

# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.dominios.cliente import Cliente

def test_conexion_bd():
    """Prueba la conexión a la base de datos"""
    print("🔵 Probando conexión a la base de datos...")
    
    try:
        from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Hacer una consulta simple
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        close_connection(conn, cursor)
        
        if result:
            print("✅ Conexión a la base de datos exitosa")
            return True
        else:
            print("❌ Error: No se pudo ejecutar consulta de prueba")
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_crear_persona():
    """Prueba crear una persona"""
    print("🔵 Probando creación de persona...")
    
    try:
        gestor_personas = Personas()
        
        # Crear persona de prueba
        persona_nueva = Persona(
            id_persona=None,
            nombre="Juan Carlos",
            apellido="Pérez García",
            email="juan.perez@email.com",
            telefono="123456789",
            dni="12345678A",
            direccion="Calle Falsa 123",
            cp="28001",
            poblacion="Madrid",
            pais="España"
        )
        
        print(f"Datos de la persona a crear:")
        print(f"- Nombre: {persona_nueva.nombre}")
        print(f"- Apellido: {persona_nueva.apellido}")
        print(f"- Email: {persona_nueva.email}")
        print(f"- DNI: {persona_nueva.dni}")
        
        # Agregar persona
        persona_creada = gestor_personas.agregar(persona_nueva)
        
        if persona_creada is None:
            print("❌ Error: No se pudo crear la persona")
            return None
        
        print(f"✅ Persona creada exitosamente con ID: {persona_creada.id_persona}")
        return persona_creada
        
    except Exception as e:
        print(f"❌ Error durante la creación de persona: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_crear_cliente(persona_creada):
    """Prueba crear un cliente con la persona creada"""
    print("🔵 Probando creación de cliente...")
    
    try:
        gestor_clientes = Clientes()
        
        # Crear cliente de prueba
        cliente_nuevo = Cliente(
            id_cliente=None,
            id_persona=persona_creada.id_persona,
            tipo="PARTICULAR",
            razon_social="Juan Carlos Pérez García",
            nif="12345678A",
            fecha_registro="2024-01-15"
        )
        
        print(f"Datos del cliente a crear:")
        print(f"- ID Persona: {cliente_nuevo.id_persona}")
        print(f"- Tipo: {cliente_nuevo.tipo}")
        print(f"- Razón Social: {cliente_nuevo.razon_social}")
        print(f"- NIF: {cliente_nuevo.nif}")
        
        # Agregar cliente
        cliente_creado = gestor_clientes.agregar(cliente_nuevo)
        
        if cliente_creado is None:
            print("❌ Error: No se pudo crear el cliente")
            return None
        
        print(f"✅ Cliente creado exitosamente con ID: {cliente_creado.id_cliente}")
        print(f"Datos completos del cliente: {cliente_creado.to_dict()}")
        return cliente_creado
        
    except Exception as e:
        print(f"❌ Error durante la creación de cliente: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas de diagnóstico - Creación de Cliente SQL Server")
    print("=" * 70)
    
    # Paso 1: Probar conexión
    if not test_conexion_bd():
        print("❌ No se puede conectar a la base de datos. Abortando pruebas.")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    
    # Paso 2: Crear persona
    persona_creada = test_crear_persona()
    if persona_creada is None:
        print("❌ No se pudo crear la persona. Abortando pruebas.")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    
    # Paso 3: Crear cliente
    cliente_creado = test_crear_cliente(persona_creada)
    if cliente_creado is None:
        print("❌ No se pudo crear el cliente. Revisar logs de error arriba.")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("🎉 ¡Todas las pruebas completadas exitosamente!")
    print("✅ El problema de creación de clientes ha sido solucionado")
    print("\n💡 Ahora puedes probar crear un cliente desde el formulario web")

if __name__ == "__main__":
    main()
