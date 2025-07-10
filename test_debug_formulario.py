#!/usr/bin/env python3
"""
Script para probar con los datos exactos del formulario que falló
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.validaciones.validar_persona import validar_datos_persona

def test_datos_formulario():
    """Test con los datos exactos del formulario que falló"""
    print("=== TEST CON DATOS EXACTOS DEL FORMULARIO ===")
    
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
        'pais': 'ccc'
    }
    
    print(f"Datos del formulario: {datos_formulario}")
    
    # 1. Validar datos
    print("\n1. Validando datos...")
    es_valido, mensaje = validar_datos_persona(datos_formulario)
    print(f"   Validación: {es_valido}")
    if not es_valido:
        print(f"   ❌ Error de validación: {mensaje}")
        return False
    
    # 2. Crear objeto Persona
    print("\n2. Creando objeto Persona...")
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
        print(f"   Persona creada: {persona}")
    except Exception as e:
        print(f"   ❌ Error al crear objeto Persona: {e}")
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

def test_validaciones_individuales():
    """Test de validaciones individuales"""
    print("\n=== TEST DE VALIDACIONES INDIVIDUALES ===")
    
    # Test nombre con x's
    print("\n1. Validando nombre 'xxxxxxxxxxx'...")
    import re
    nombre = 'xxxxxxxxxxx'
    if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'-]+$', nombre):
        print(f"   ✅ Nombre válido: {nombre}")
    else:
        print(f"   ❌ Nombre inválido: {nombre}")
    
    # Test email corto
    print("\n2. Validando email 'e@s.o'...")
    from GeobizIA.validaciones.sanitizacion import sanitizar_email
    email = 'e@s.o'
    email_sanitizado = sanitizar_email(email)
    if email_sanitizado:
        print(f"   ✅ Email válido: {email_sanitizado}")
    else:
        print(f"   ❌ Email inválido: {email}")
    
    # Test DNI largo
    print("\n3. Validando DNI 'xxxxxxxxxxxxxxxxxxxx'...")
    dni = 'xxxxxxxxxxxxxxxxxxxx'
    print(f"   Longitud DNI: {len(dni)} caracteres")
    if len(dni) > 20:  # Assuming max length is 20
        print(f"   ❌ DNI demasiado largo: {dni}")
    else:
        print(f"   ✅ DNI longitud aceptable: {dni}")

if __name__ == "__main__":
    print("Iniciando test con datos del formulario...")
    
    # Test validaciones individuales
    test_validaciones_individuales()
    
    # Test con datos exactos
    if test_datos_formulario():
        print("\n✅ Test completado exitosamente")
    else:
        print("\n❌ Test falló")
