#!/usr/bin/env python3
"""
Script para probar las redirecciones tras editar/eliminar eventos y proyectos
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_redirect_flow():
    """Prueba el flujo de redirección después de operaciones CRUD"""
    print("🔄 Probando flujo de redirección después de operaciones CRUD...")
    
    # Test 1: Crear evento para probar edición
    print("\n📝 Creando evento de prueba...")
    evento_data = {
        "nombre": "Evento Prueba Redirección",
        "tipo": "Workshop",
        "lugar": "Aula Virtual",
        "fecha_comienzo": "2024-12-15",
        "fecha_final": "2024-12-15",
        "poblacion": "Online",
        "tematica": "Pruebas de Sistema"
    }
    
    response = requests.post(f"{BASE_URL}/api/eventos", json=evento_data)
    if response.status_code == 200:
        print("✅ Evento creado exitosamente")
        
        # Obtener ID del evento creado
        response = requests.get(f"{BASE_URL}/api/eventos")
        eventos = response.json()
        evento_creado = next((e for e in eventos if e['nombre'] == "Evento Prueba Redirección"), None)
        
        if evento_creado:
            evento_id = evento_creado['id_evento']
            print(f"✅ ID del evento: {evento_id}")
            
            # Test 2: Actualizar evento
            print("\n✏️ Actualizando evento...")
            evento_actualizado = evento_creado.copy()
            evento_actualizado['nombre'] = "Evento Prueba Redirección - Actualizado"
            
            response = requests.put(f"{BASE_URL}/api/eventos/{evento_id}", json=evento_actualizado)
            if response.status_code == 200:
                print("✅ Evento actualizado - El frontend debería redirigir a /eventos/ver")
            else:
                print(f"❌ Error al actualizar: {response.status_code}")
            
            # Test 3: Eliminar evento
            print("\n🗑️ Eliminando evento...")
            response = requests.delete(f"{BASE_URL}/api/eventos/{evento_id}")
            if response.status_code == 200:
                print("✅ Evento eliminado - El frontend debería redirigir a /eventos/ver")
            else:
                print(f"❌ Error al eliminar: {response.status_code}")
    else:
        print(f"❌ Error al crear evento: {response.status_code}")
    
    # Test 4: Mismo flujo para proyectos
    print("\n📝 Creando proyecto de prueba...")
    proyecto_data = {
        "nombre": "Proyecto Prueba Redirección",
        "descripcion": "Proyecto para probar redirecciones",
        "fecha_inicio": "2024-12-01",
        "fecha_fin": "2024-12-31",
        "poblacion": "Madrid",
        "responsable": "Sistema de Pruebas",
        "estado": "PLANIFICACION",
        "objetivos": "Verificar redirecciones",
        "presupuesto": 1000.00
    }
    
    response = requests.post(f"{BASE_URL}/api/proyectos", json=proyecto_data)
    if response.status_code == 200:
        result = response.json()
        proyecto_id = result.get('id_proyecto')
        print(f"✅ Proyecto creado exitosamente con ID: {proyecto_id}")
        
        # Test 5: Actualizar proyecto
        print("\n✏️ Actualizando proyecto...")
        proyecto_actualizado = proyecto_data.copy()
        proyecto_actualizado['nombre'] = "Proyecto Prueba Redirección - Actualizado"
        proyecto_actualizado['estado'] = "EN_PROGRESO"
        
        response = requests.put(f"{BASE_URL}/api/proyectos/{proyecto_id}", json=proyecto_actualizado)
        if response.status_code == 200:
            print("✅ Proyecto actualizado - El frontend debería redirigir a /proyectos/ver")
        else:
            print(f"❌ Error al actualizar: {response.status_code}")
        
        # Test 6: Eliminar proyecto
        print("\n🗑️ Eliminando proyecto...")
        response = requests.delete(f"{BASE_URL}/api/proyectos/{proyecto_id}")
        if response.status_code == 200:
            print("✅ Proyecto eliminado - El frontend debería redirigir a /proyectos/ver")
        else:
            print(f"❌ Error al eliminar: {response.status_code}")
    else:
        print(f"❌ Error al crear proyecto: {response.status_code}")

def main():
    print("🧪 Probando redirecciones después de operaciones CRUD")
    print("=" * 60)
    
    try:
        # Probar conexión
        response = requests.get(f"{BASE_URL}/api/eventos", timeout=5)
        if response.status_code == 200:
            print("✅ Conexión exitosa con el servidor")
            test_redirect_flow()
        else:
            print(f"❌ El servidor respondió con código: {response.status_code}")
    except requests.ConnectionError:
        print("❌ No se pudo conectar al servidor. Asegúrate de que esté ejecutándose.")
    except requests.Timeout:
        print("❌ Timeout al conectar con el servidor")
    
    print("\n" + "=" * 60)
    print("📋 RESUMEN:")
    print("🔄 Las redirecciones se han configurado en el frontend:")
    print("   • Después de actualizar: redirige tras 1.5 segundos")
    print("   • Después de eliminar: redirige inmediatamente")
    print("   • Rutas de destino: /eventos/ver y /proyectos/ver")
    print("\n🎯 Prueba manualmente en el navegador:")
    print("   1. Ve a un evento/proyecto")
    print("   2. Edítalo y guarda")
    print("   3. Verifica que redirija a la lista")
    print("   4. Ve a otro evento/proyecto")
    print("   5. Elimínalo y verifica la redirección")

if __name__ == "__main__":
    main()
