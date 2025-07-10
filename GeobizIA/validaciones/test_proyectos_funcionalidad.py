#!/usr/bin/env python3
"""
Script de prueba para verificar que la creación de proyectos funciona correctamente
"""
import sys
import os
import requests
import json

# Agregar el directorio padre al path para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_crear_proyecto():
    """Prueba crear un proyecto a través de la API"""
    print("🧪 Probando creación de proyecto...")
    
    # Datos de prueba que coinciden con el formulario del frontend
    datos_proyecto = {
        "nombre": "Proyecto de Prueba Automatizada",
        "descripcion": "Este es un proyecto creado automáticamente para verificar la funcionalidad",
        "fecha_inicio": "2025-07-10",
        "fecha_fin": "2025-12-31",
        "poblacion": "Madrid",
        "responsable": "Juan Pérez",
        "estado": "PLANIFICACION",
        "objetivos": "Verificar que el sistema de proyectos funciona correctamente",
        "presupuesto": 50000.50
    }
    
    try:
        # Hacer petición POST a la API
        response = requests.post(
            'http://localhost:8000/api/proyectos',
            headers={'Content-Type': 'application/json'},
            json=datos_proyecto,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Proyecto creado exitosamente: {result}")
            return True
        else:
            print(f"❌ Error al crear proyecto: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a la API. ¿Está el servidor ejecutándose en http://localhost:8000?")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_listar_proyectos():
    """Prueba listar proyectos existentes"""
    print("\n🧪 Probando listado de proyectos...")
    
    try:
        response = requests.get('http://localhost:8000/api/proyectos', timeout=10)
        
        if response.status_code == 200:
            proyectos = response.json()
            print(f"✅ Se obtuvieron {len(proyectos)} proyectos")
            for i, proyecto in enumerate(proyectos[:3]):  # Mostrar solo los primeros 3
                print(f"   {i+1}. {proyecto.get('nombre', 'Sin nombre')} - {proyecto.get('estado', 'Sin estado')}")
            if len(proyectos) > 3:
                print(f"   ... y {len(proyectos) - 3} más")
            return True
        else:
            print(f"❌ Error al listar proyectos: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a la API")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_validaciones():
    """Prueba las validaciones del sistema"""
    print("\n🧪 Probando validaciones...")
    
    # Datos inválidos para probar validaciones
    datos_invalidos = {
        "nombre": "AB",  # Muy corto
        "descripcion": "Corto",  # Muy corto
        "estado": "ESTADO_INVALIDO",  # Estado no válido
        "presupuesto": -1000  # Presupuesto negativo
    }
    
    try:
        response = requests.post(
            'http://localhost:8000/api/proyectos',
            headers={'Content-Type': 'application/json'},
            json=datos_invalidos,
            timeout=10
        )
        
        if response.status_code == 400:
            print("✅ Las validaciones funcionan correctamente - se rechazaron datos inválidos")
            error_detail = response.json().get('detail', 'Error de validación')
            print(f"   Mensaje de error: {error_detail}")
            return True
        else:
            print(f"❌ Las validaciones no funcionan - se aceptaron datos inválidos: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error al probar validaciones: {e}")
        return False

def main():
    """Función principal de prueba"""
    print("🚀 Iniciando pruebas de funcionalidad de proyectos")
    print("=" * 60)
    
    pruebas_exitosas = 0
    total_pruebas = 3
    
    # Ejecutar pruebas
    if test_listar_proyectos():
        pruebas_exitosas += 1
    
    if test_crear_proyecto():
        pruebas_exitosas += 1
    
    if test_validaciones():
        pruebas_exitosas += 1
    
    # Resumen
    print("\n" + "=" * 60)
    print(f"📊 Resultados: {pruebas_exitosas}/{total_pruebas} pruebas exitosas")
    
    if pruebas_exitosas == total_pruebas:
        print("🎉 ¡Todas las pruebas pasaron! El sistema de proyectos está funcionando correctamente.")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisar los errores anteriores.")
    
    print("\n📋 Para usar el sistema:")
    print("   1. Asegúrate de que el servidor FastAPI esté ejecutándose")
    print("   2. Asegúrate de que el frontend Vue esté ejecutándose")
    print("   3. Ve a http://localhost:8080 (o el puerto del frontend)")
    print("   4. Navega al formulario de proyectos")
    print("   5. Crea y visualiza proyectos")

if __name__ == "__main__":
    main()
