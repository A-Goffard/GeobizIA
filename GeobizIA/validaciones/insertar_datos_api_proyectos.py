#!/usr/bin/env python3
"""
Script para insertar datos de prueba en la base de datos de proyectos
usando la API (para aprovechar la generación automática de IDs).
"""

import requests
import json
import sys

# Configuración de la API
API_BASE_URL = "http://localhost:8000"
API_PROYECTOS_URL = f"{API_BASE_URL}/api/proyectos"

def insertar_datos_via_api():
    """Inserta datos de prueba usando la API"""
    print("🔄 Insertando datos de prueba usando la API...")
    
    # Datos de prueba
    proyectos_prueba = [
        {
            "nombre": "Proyecto Sostenibilidad Urbana",
            "descripcion": "Proyecto para implementar soluciones sostenibles en entornos urbanos, incluyendo gestión de residuos y energías renovables.",
            "fecha_inicio": "2024-01-15",
            "fecha_fin": "2024-12-15",
            "poblacion": "Madrid, España",
            "responsable": "María García López",
            "estado": "EN_PROGRESO",
            "objetivos": "Reducir la huella de carbono en un 30% y mejorar la calidad del aire en zonas urbanas.",
            "presupuesto": 150000.00
        },
        {
            "nombre": "Educación Ambiental Comunitaria",
            "descripcion": "Programa de educación ambiental dirigido a comunidades locales para promover prácticas sostenibles.",
            "fecha_inicio": "2024-03-01",
            "fecha_fin": "2024-08-31",
            "poblacion": "Barcelona, España",
            "responsable": "Juan Carlos Ruiz",
            "estado": "PLANIFICACION",
            "objetivos": "Capacitar a 500 personas en prácticas ambientales sostenibles y crear 10 grupos de acción comunitaria.",
            "presupuesto": 75000.50
        },
        {
            "nombre": "Restauración Forestal",
            "descripcion": "Proyecto de reforestación y restauración de ecosistemas forestales degradados en zonas rurales.",
            "fecha_inicio": "2024-02-01",
            "fecha_fin": "2025-01-31",
            "poblacion": "Asturias, España",
            "responsable": "Ana Martínez Torres",
            "estado": "EN_PROGRESO",
            "objetivos": "Restaurar 200 hectáreas de bosque y plantar 50,000 árboles nativos.",
            "presupuesto": 300000.75
        },
        {
            "nombre": "Gestión Integral de Residuos",
            "descripcion": "Implementación de un sistema integral de gestión de residuos con enfoque en economía circular.",
            "fecha_inicio": "2024-01-01",
            "fecha_fin": "2024-06-30",
            "poblacion": "Valencia, España",
            "responsable": "Pedro Sánchez Gómez",
            "estado": "COMPLETADO",
            "objetivos": "Reducir los residuos urbanos en un 40% y aumentar el reciclaje al 85%.",
            "presupuesto": 120000.25
        },
        {
            "nombre": "Energía Solar Comunitaria",
            "descripcion": "Instalación de paneles solares comunitarios para promover el uso de energías renovables.",
            "fecha_inicio": "2024-05-01",
            "fecha_fin": "2024-11-30",
            "poblacion": "Sevilla, España",
            "responsable": "Laura Fernández Díaz",
            "estado": "PLANIFICACION",
            "objetivos": "Instalar 100 kW de capacidad solar y reducir el consumo eléctrico convencional en un 50%.",
            "presupuesto": 200000.00
        }
    ]
    
    # Verificar si el servidor está funcionando
    try:
        response = requests.get(f"{API_BASE_URL}/docs")
        if response.status_code != 200:
            print("❌ El servidor no está funcionando. Inicia el servidor primero.")
            return False
    except Exception as e:
        print(f"❌ No se puede conectar al servidor: {e}")
        print("💡 Asegúrate de que el servidor esté funcionando en http://localhost:8000")
        return False
    
    # Insertar cada proyecto
    proyectos_insertados = 0
    for datos in proyectos_prueba:
        try:
            response = requests.post(API_PROYECTOS_URL, json=datos)
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Proyecto '{datos['nombre']}' insertado correctamente (ID: {result.get('id_proyecto', 'N/A')})")
                proyectos_insertados += 1
            else:
                print(f"❌ Error al insertar proyecto '{datos['nombre']}': {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"❌ Error al procesar proyecto '{datos['nombre']}': {e}")
    
    print(f"\n📊 Resultado: {proyectos_insertados} proyectos insertados correctamente")
    return proyectos_insertados > 0

def verificar_datos():
    """Verifica que los datos se insertaron correctamente"""
    print("\n🔍 Verificando datos insertados...")
    
    try:
        response = requests.get(API_PROYECTOS_URL)
        if response.status_code == 200:
            proyectos = response.json()
            print(f"✅ Se encontraron {len(proyectos)} proyectos en la base de datos:")
            
            for proyecto in proyectos:
                print(f"  - {proyecto.get('nombre', 'Sin nombre')} ({proyecto.get('estado', 'Sin estado')})")
                
            return True
        else:
            print(f"❌ Error al obtener proyectos: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error al verificar datos: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Configurando datos de prueba para proyectos")
    print("=" * 50)
    
    # Insertar datos de prueba
    if insertar_datos_via_api():
        print("\n✅ Datos de prueba insertados exitosamente")
    else:
        print("\n❌ Hubo errores al insertar datos de prueba")
        return False
    
    # Verificar datos
    if verificar_datos():
        print("\n✅ Verificación completada exitosamente")
    else:
        print("\n❌ Error en la verificación")
        return False
    
    print("\n🎉 Configuración completada!")
    print("\nAhora puedes:")
    print("1. Acceder a la API: http://localhost:8000/api/proyectos")
    print("2. Ver la documentación: http://localhost:8000/docs")
    print("3. Usar el frontend para ver los proyectos creados")
    print("4. Crear más proyectos desde el formulario web")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
