#!/usr/bin/env python3
"""
Script de diagnóstico para identificar problemas en la creación de clientes
"""

import sys
import os

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'GeobizIA'))

from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.dominios.cliente import Cliente
from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.validaciones.validar_persona import validar_datos_persona
from GeobizIA.validaciones.validar_cliente import validar_datos_cliente

def test_con_datos_formulario():
    """
    Test con los datos exactos del formulario que falló
    """
    print("=== DIAGNÓSTICO DE CREACIÓN DE CLIENTE ===")
    
    # Datos exactos del formulario que falló
    datos_formulario = {
        'nombre': 'xxxxxxxxxxx',
        'apellido': 'xxxxxxxxxxxxxxx',
        'email': 'e@s.o',
        'telefono': 'xxxxxxxxxxxxxxxxx',
        'dni': 'xxxxxxxxxxxxxxxxxxxx',
        'direccion': 'xxxxxxxxxxxxxxxxxxx',
        'cp': 'xxxxxxxxxxxxxxxxxxx',
        'poblacion': 'Barcelona',
        'pais': 'ccc',
        'tipo': 'ENTIDAD',
        'razon_social': 'xxxxxxxxxxxxxx',
        'nif': 'xxxxxxxxxxxxxxxxxxxxxxx',
        'fecha_registro': '2025-07-25'
    }
    
    print("1. Datos del formulario:")
    for key, value in datos_formulario.items():
        print(f"   {key}: '{value}'")
    
    print("\n2. Validando datos de persona...")
    # Separar datos de persona
    datos_persona = {
        'nombre': datos_formulario['nombre'],
        'apellido': datos_formulario['apellido'],
        'email': datos_formulario['email'],
        'telefono': datos_formulario['telefono'],
        'dni': datos_formulario['dni'],
        'direccion': datos_formulario['direccion'],
        'cp': datos_formulario['cp'],
        'poblacion': datos_formulario['poblacion'],
        'pais': datos_formulario['pais']
    }
    
    valido, mensaje = validar_datos_persona(datos_persona)
    print(f"   Validación persona: {'✓ VÁLIDO' if valido else '✗ INVÁLIDO'}")
    if not valido:
        print(f"   Error: {mensaje}")
        return False
    
    print("\n3. Validando datos de cliente...")
    # Separar datos de cliente
    datos_cliente = {
        'razon_social': datos_formulario['razon_social'],
        'nif': datos_formulario['nif'],
        'telefono': datos_formulario.get('telefono'),
        'email': datos_formulario.get('email'),
        'direccion': datos_formulario.get('direccion')
    }
    
    valido, mensaje = validar_datos_cliente(datos_cliente)
    print(f"   Validación cliente: {'✓ VÁLIDO' if valido else '✗ INVÁLIDO'}")
    if not valido:
        print(f"   Error: {mensaje}")
        return False
    
    print("\n4. Intentando crear objetos de dominio...")
    
    # Crear persona
    try:
        persona = Persona(
            id_persona=None,
            nombre=datos_formulario['nombre'],
            apellido=datos_formulario['apellido'],
            email=datos_formulario['email'],
            telefono=datos_formulario['telefono'],
            dni=datos_formulario['dni'],
            direccion=datos_formulario['direccion'],
            cp=datos_formulario['cp'],
            poblacion=datos_formulario['poblacion'],
            pais=datos_formulario['pais']
        )
        print("   ✓ Objeto Persona creado correctamente")
        print(f"   Persona: {persona}")
    except Exception as e:
        print(f"   ✗ Error al crear objeto Persona: {e}")
        return False
    
    # Crear cliente
    try:
        cliente = Cliente(
            id_cliente=None,
            id_persona=1,  # Simulado
            tipo=datos_formulario['tipo'],
            razon_social=datos_formulario['razon_social'],
            nif=datos_formulario['nif'],
            fecha_registro=datos_formulario['fecha_registro']
        )
        print("   ✓ Objeto Cliente creado correctamente")
        print(f"   Cliente: {cliente}")
    except Exception as e:
        print(f"   ✗ Error al crear objeto Cliente: {e}")
        return False
    
    print("\n5. Probando con gestores...")
    try:
        gestor_personas = Personas()
        persona_creada = gestor_personas.agregar(persona)
        if persona_creada:
            print("   ✓ Persona agregada correctamente al gestor")
            print(f"   ID persona creada: {persona_creada.id_persona}")
        else:
            print("   ✗ Error: El gestor retornó None al crear la persona")
            return False
    except Exception as e:
        print(f"   ✗ Error al usar gestor de personas: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n=== DIAGNÓSTICO COMPLETADO ===")
    return True

def test_con_datos_limpios():
    """
    Test con datos limpios para verificar que el sistema funciona
    """
    print("\n=== TEST CON DATOS LIMPIOS ===")
    
    datos_limpios = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'email': 'juan@example.com',
        'telefono': '600123456',
        'dni': '12345678A',
        'direccion': 'Calle Falsa 123',
        'cp': '08001',
        'poblacion': 'Barcelona',
        'pais': 'España',
        'tipo': 'PARTICULAR',
        'razon_social': 'Juan Pérez',
        'nif': 'A12345678',
        'fecha_registro': '2025-01-15'
    }
    
    try:
        # Crear persona
        persona = Persona(
            id_persona=None,
            nombre=datos_limpios['nombre'],
            apellido=datos_limpios['apellido'],
            email=datos_limpios['email'],
            telefono=datos_limpios['telefono'],
            dni=datos_limpios['dni'],
            direccion=datos_limpios['direccion'],
            cp=datos_limpios['cp'],
            poblacion=datos_limpios['poblacion'],
            pais=datos_limpios['pais']
        )
        
        gestor_personas = Personas()
        persona_creada = gestor_personas.agregar(persona)
        
        if persona_creada:
            print("   ✓ Datos limpios funcionan correctamente")
            return True
        else:
            print("   ✗ Error incluso con datos limpios")
            return False
    except Exception as e:
        print(f"   ✗ Error con datos limpios: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando diagnóstico de creación de clientes...")
    
    # Test con datos del formulario que falló
    test_con_datos_formulario()
    
    # Test con datos limpios
    test_con_datos_limpios()
