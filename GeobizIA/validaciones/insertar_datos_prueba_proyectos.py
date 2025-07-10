#!/usr/bin/env python3
"""
Script para insertar datos de prueba en la base de datos de proyectos
y verificar que la funcionalidad completa funciona correctamente.
"""

import sys
import os
import sqlite3
from datetime import datetime

# Agregar la ruta del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from GeobizIA.controlador.gestores.proyectos import Proyectos
from GeobizIA.controlador.dominios.proyecto import Proyecto

def insertar_datos_prueba():
    """Inserta datos de prueba en la base de datos"""
    print("🔄 Insertando datos de prueba en la base de datos...")
    
    gestor = Proyectos()
    
    # Datos de prueba
    proyectos_prueba = [
        {
            "id_proyecto": 1,
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
            "id_proyecto": 2,
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
            "id_proyecto": 3,
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
            "id_proyecto": 4,
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
            "id_proyecto": 5,
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
    
    # Insertar cada proyecto
    proyectos_insertados = 0
    for datos in proyectos_prueba:
        try:
            # Verificar si el proyecto ya existe
            if not gestor.existe(datos["id_proyecto"]):
                proyecto = Proyecto(
                    id_proyecto=datos["id_proyecto"],
                    nombre=datos["nombre"],
                    descripcion=datos["descripcion"],
                    fecha_inicio=datos["fecha_inicio"],
                    fecha_fin=datos["fecha_fin"],
                    poblacion=datos["poblacion"],
                    responsable=datos["responsable"],
                    estado=datos["estado"],
                    objetivos=datos["objetivos"],
                    presupuesto=datos["presupuesto"]
                )
                
                resultado = gestor.agregar(proyecto)
                if resultado:
                    print(f"✅ Proyecto '{datos['nombre']}' insertado correctamente")
                    proyectos_insertados += 1
                else:
                    print(f"❌ Error al insertar proyecto '{datos['nombre']}'")
            else:
                print(f"ℹ️  Proyecto '{datos['nombre']}' ya existe, omitiendo...")
                
        except Exception as e:
            print(f"❌ Error al procesar proyecto '{datos['nombre']}': {e}")
    
    print(f"\n📊 Resultado: {proyectos_insertados} proyectos insertados correctamente")
    return proyectos_insertados > 0

def verificar_datos():
    """Verifica que los datos se insertaron correctamente"""
    print("\n🔍 Verificando datos insertados...")
    
    gestor = Proyectos()
    
    try:
        proyectos = gestor.mostrar_todos_los_elem()
        print(f"✅ Se encontraron {len(proyectos)} proyectos en la base de datos:")
        
        for proyecto in proyectos:
            print(f"  - {proyecto.nombre} ({proyecto.estado})")
            
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar datos: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Configurando datos de prueba para proyectos")
    print("=" * 50)
    
    # Insertar datos de prueba
    if insertar_datos_prueba():
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
    print("1. Iniciar el servidor: python -m uvicorn GeobizIA.api.main:app --reload")
    print("2. Acceder a la API: http://localhost:8000/api/proyectos")
    print("3. Ver la documentación: http://localhost:8000/docs")
    print("4. Usar el frontend para ver los proyectos creados")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
