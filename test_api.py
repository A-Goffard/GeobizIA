#!/usr/bin/env python3
"""
Script de prueba para verificar que los endpoints funcionan correctamente
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoints():
    print("🧪 Probando endpoints...")
    
    # Probar endpoint de test
    try:
        response = requests.get(f"{BASE_URL}/api/actividades_realizadas/test")
        print(f"✅ Test endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Error en test endpoint: {e}")
    
    # Probar endpoint de actividades
    try:
        response = requests.get(f"{BASE_URL}/api/actividades")
        print(f"✅ Actividades: {response.status_code} - {len(response.json())} actividades encontradas")
    except Exception as e:
        print(f"❌ Error en actividades: {e}")
    
    # Probar endpoint de estadísticas de actividades
    try:
        response = requests.get(f"{BASE_URL}/api/actividades/estadisticas")
        print(f"✅ Estadísticas actividades: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   - Total: {data.get('total', 0)}")
            print(f"   - Tipos: {len(data.get('por_tipo', {}))}")
            print(f"   - Responsables: {len(data.get('por_responsable', {}))}")
        else:
            print(f"   - Error: {response.text}")
    except Exception as e:
        print(f"❌ Error en estadísticas de actividades: {e}")
    
    # Probar endpoint de actividades realizadas
    try:
        response = requests.get(f"{BASE_URL}/api/actividades_realizadas")
        print(f"✅ Actividades realizadas: {response.status_code} - {len(response.json())} registros encontrados")
    except Exception as e:
        print(f"❌ Error en actividades realizadas: {e}")
    
    # Probar endpoint de estadísticas de actividades realizadas
    try:
        response = requests.get(f"{BASE_URL}/api/actividades_realizadas/estadisticas")
        print(f"✅ Estadísticas actividades realizadas: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   - {len(data.get('por_actividad', []))} actividades en estadísticas")
        else:
            print(f"   - Error: {response.text}")
    except Exception as e:
        print(f"❌ Error en estadísticas: {e}")

if __name__ == "__main__":
    test_endpoints()
