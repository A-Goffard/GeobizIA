#!/usr/bin/env python3
"""
Script simple para probar las validaciones de proyectos
"""

import sys
import os

# Agregar la ruta del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from GeobizIA.validaciones.validar_proyecto import validar_datos_proyecto

def test_validacion_local():
    """Prueba las validaciones localmente sin servidor"""
    print("🚀 Probando validaciones de proyectos localmente...")
    
    # Datos válidos
    datos_validos = {
        "nombre": "Proyecto de Prueba",
        "descripcion": "Esta es una descripción válida para el proyecto de prueba",
        "estado": "PLANIFICACION",
        "fecha_inicio": "2024-01-15",
        "fecha_fin": "2024-06-15",
        "poblacion": "Madrid",
        "responsable": "Juan Pérez",
        "objetivos": "Objetivos del proyecto de prueba",
        "presupuesto": 25000.50
    }
    
    # Probar datos válidos
    print("\n1. Probando datos válidos...")
    valido, mensaje = validar_datos_proyecto(datos_validos)
    if valido:
        print(f"✅ Datos válidos: {mensaje}")
    else:
        print(f"❌ Error inesperado: {mensaje}")
        return False
    
    # Probar datos inválidos
    print("\n2. Probando datos inválidos...")
    casos_invalidos = [
        {
            "datos": {"nombre": "AB", "descripcion": "Descripción válida", "estado": "PLANIFICACION"},
            "descripcion": "Nombre muy corto"
        },
        {
            "datos": {"nombre": "Proyecto válido", "descripcion": "Corta", "estado": "PLANIFICACION"},
            "descripcion": "Descripción muy corta"
        },
        {
            "datos": {"nombre": "Proyecto válido", "descripcion": "Descripción válida", "estado": "ESTADO_INVALIDO"},
            "descripcion": "Estado inválido"
        }
    ]
    
    for caso in casos_invalidos:
        valido, mensaje = validar_datos_proyecto(caso["datos"])
        if not valido:
            print(f"✅ Validación correcta para {caso['descripcion']}: {mensaje}")
        else:
            print(f"❌ Error: {caso['descripcion']} debería haber sido rechazado")
            return False
    
    print("\n🎉 Todas las validaciones funcionan correctamente!")
    return True

if __name__ == "__main__":
    success = test_validacion_local()
    sys.exit(0 if success else 1)
