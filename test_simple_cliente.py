#!/usr/bin/env python3
"""
Prueba simple para verificar la funcionalidad de creación de clientes
"""

import sys
import os

# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.dominios.cliente import Cliente

def test_crear_cliente():
    """Prueba crear un cliente con su persona asociada"""
    print("🔵 Probando creación de cliente y persona...")
    
    try:
        # Crear gestores
        gestor_personas = Personas()
        gestor_clientes = Clientes()
        
        # Crear persona
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
        
        print(f"Datos de la persona a crear: {persona_nueva}")
        
        # Agregar persona
        persona_creada = gestor_personas.agregar(persona_nueva)
        
        if persona_creada is None:
            print("❌ Error: No se pudo crear la persona")
            return False
        
        print(f"✅ Persona creada con ID: {persona_creada.id_persona}")
        
        # Crear cliente
        cliente_nuevo = Cliente(
            id_cliente=None,
            id_persona=persona_creada.id_persona,
            tipo="individual",
            razon_social="Juan Carlos Pérez García",
            nif="12345678A",
            fecha_registro="2024-01-15"
        )
        
        print(f"Datos del cliente a crear: {cliente_nuevo}")
        
        # Agregar cliente
        cliente_creado = gestor_clientes.agregar(cliente_nuevo)
        
        if cliente_creado is None:
            print("❌ Error: No se pudo crear el cliente")
            return False
        
        print(f"✅ Cliente creado con ID: {cliente_creado.id_cliente}")
        print(f"Datos completos del cliente: {cliente_creado.to_dict()}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando prueba de creación de clientes")
    print("=" * 50)
    
    if test_crear_cliente():
        print("✅ Prueba completada exitosamente")
    else:
        print("❌ Prueba falló")

if __name__ == "__main__":
    main()
