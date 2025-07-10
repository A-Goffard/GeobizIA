#!/usr/bin/env python3
"""
Script para probar la funcionalidad CRUD completa de eventos y proyectos.
Verifica que se pueden crear, leer, actualizar y eliminar eventos y proyectos.
"""

import requests
import json
from datetime import datetime, date
import sys

# Configuración del servidor API
BASE_URL = "http://localhost:8000"

def test_eventos_crud():
    """Prueba las operaciones CRUD para eventos"""
    print("🧪 Probando CRUD de Eventos...")
    
    # 1. Crear evento
    evento_data = {
        "nombre": "Evento de Prueba CRUD",
        "tipo": "Conferencia",
        "lugar": "Centro de Convenciones",
        "fecha_comienzo": "2024-12-01",
        "fecha_final": "2024-12-02",
        "poblacion": "Madrid",
        "tematica": "Tecnología Ambiental"
    }
    
    print("📝 Creando evento...")
    response = requests.post(f"{BASE_URL}/api/eventos", json=evento_data)
    if response.status_code == 200:
        print("✅ Evento creado exitosamente")
    else:
        print(f"❌ Error al crear evento: {response.status_code} - {response.text}")
        return False
    
    # 2. Listar eventos para obtener el ID
    print("📋 Obteniendo lista de eventos...")
    response = requests.get(f"{BASE_URL}/api/eventos")
    if response.status_code == 200:
        eventos = response.json()
        evento_creado = next((e for e in eventos if e['nombre'] == "Evento de Prueba CRUD"), None)
        if evento_creado:
            evento_id = evento_creado['id_evento']
            print(f"✅ Evento encontrado con ID: {evento_id}")
        else:
            print("❌ No se encontró el evento creado")
            return False
    else:
        print(f"❌ Error al obtener eventos: {response.status_code}")
        return False
    
    # 3. Obtener evento específico
    print(f"🔍 Obteniendo evento con ID {evento_id}...")
    response = requests.get(f"{BASE_URL}/api/eventos/{evento_id}")
    if response.status_code == 200:
        evento_detalle = response.json()
        print(f"✅ Evento obtenido: {evento_detalle['nombre']}")
    else:
        print(f"❌ Error al obtener evento: {response.status_code}")
        return False
    
    # 4. Actualizar evento
    print("✏️ Actualizando evento...")
    evento_actualizado = evento_detalle.copy()
    evento_actualizado['nombre'] = "Evento de Prueba CRUD - Actualizado"
    evento_actualizado['lugar'] = "Nuevo Centro de Convenciones"
    
    response = requests.put(f"{BASE_URL}/api/eventos/{evento_id}", json=evento_actualizado)
    if response.status_code == 200:
        print("✅ Evento actualizado exitosamente")
    else:
        print(f"❌ Error al actualizar evento: {response.status_code} - {response.text}")
        return False
    
    # 5. Verificar actualización
    print("🔍 Verificando actualización...")
    response = requests.get(f"{BASE_URL}/api/eventos/{evento_id}")
    if response.status_code == 200:
        evento_verificado = response.json()
        if evento_verificado['nombre'] == "Evento de Prueba CRUD - Actualizado":
            print("✅ Actualización verificada correctamente")
        else:
            print("❌ La actualización no se aplicó correctamente")
            return False
    else:
        print(f"❌ Error al verificar actualización: {response.status_code}")
        return False
    
    # 6. Eliminar evento
    print("🗑️ Eliminando evento...")
    response = requests.delete(f"{BASE_URL}/api/eventos/{evento_id}")
    if response.status_code == 200:
        print("✅ Evento eliminado exitosamente")
    else:
        print(f"❌ Error al eliminar evento: {response.status_code} - {response.text}")
        return False
    
    # 7. Verificar eliminación
    print("🔍 Verificando eliminación...")
    response = requests.get(f"{BASE_URL}/api/eventos/{evento_id}")
    if response.status_code == 404:
        print("✅ Eliminación verificada correctamente")
    else:
        print(f"❌ El evento no fue eliminado correctamente: {response.status_code}")
        return False
    
    print("🎉 Prueba CRUD de Eventos completada exitosamente!\n")
    return True

def test_proyectos_crud():
    """Prueba las operaciones CRUD para proyectos"""
    print("🧪 Probando CRUD de Proyectos...")
    
    # 1. Crear proyecto
    proyecto_data = {
        "nombre": "Proyecto de Prueba CRUD",
        "descripcion": "Proyecto creado para probar las operaciones CRUD",
        "fecha_inicio": "2024-11-01",
        "fecha_fin": "2024-12-31",
        "poblacion": "Barcelona",
        "responsable": "Juan Pérez",
        "estado": "PLANIFICACION",
        "objetivos": "Probar funcionalidad CRUD",
        "presupuesto": 5000.00
    }
    
    print("📝 Creando proyecto...")
    response = requests.post(f"{BASE_URL}/api/proyectos", json=proyecto_data)
    if response.status_code == 200:
        result = response.json()
        proyecto_id = result.get('id_proyecto')
        print(f"✅ Proyecto creado exitosamente con ID: {proyecto_id}")
    else:
        print(f"❌ Error al crear proyecto: {response.status_code} - {response.text}")
        return False
    
    # 2. Obtener proyecto específico
    print(f"🔍 Obteniendo proyecto con ID {proyecto_id}...")
    response = requests.get(f"{BASE_URL}/api/proyectos/{proyecto_id}")
    if response.status_code == 200:
        proyecto_detalle = response.json()
        print(f"✅ Proyecto obtenido: {proyecto_detalle['nombre']}")
    else:
        print(f"❌ Error al obtener proyecto: {response.status_code}")
        return False
    
    # 3. Actualizar proyecto
    print("✏️ Actualizando proyecto...")
    proyecto_actualizado = proyecto_detalle.copy()
    proyecto_actualizado['nombre'] = "Proyecto de Prueba CRUD - Actualizado"
    proyecto_actualizado['estado'] = "EN_PROGRESO"
    proyecto_actualizado['presupuesto'] = 7500.00
    
    response = requests.put(f"{BASE_URL}/api/proyectos/{proyecto_id}", json=proyecto_actualizado)
    if response.status_code == 200:
        print("✅ Proyecto actualizado exitosamente")
    else:
        print(f"❌ Error al actualizar proyecto: {response.status_code} - {response.text}")
        return False
    
    # 4. Verificar actualización
    print("🔍 Verificando actualización...")
    response = requests.get(f"{BASE_URL}/api/proyectos/{proyecto_id}")
    if response.status_code == 200:
        proyecto_verificado = response.json()
        if (proyecto_verificado['nombre'] == "Proyecto de Prueba CRUD - Actualizado" and 
            proyecto_verificado['estado'] == "EN_PROGRESO"):
            print("✅ Actualización verificada correctamente")
        else:
            print("❌ La actualización no se aplicó correctamente")
            return False
    else:
        print(f"❌ Error al verificar actualización: {response.status_code}")
        return False
    
    # 5. Eliminar proyecto
    print("🗑️ Eliminando proyecto...")
    response = requests.delete(f"{BASE_URL}/api/proyectos/{proyecto_id}")
    if response.status_code == 200:
        print("✅ Proyecto eliminado exitosamente")
    else:
        print(f"❌ Error al eliminar proyecto: {response.status_code} - {response.text}")
        return False
    
    # 6. Verificar eliminación
    print("🔍 Verificando eliminación...")
    response = requests.get(f"{BASE_URL}/api/proyectos/{proyecto_id}")
    if response.status_code == 404:
        print("✅ Eliminación verificada correctamente")
    else:
        print(f"❌ El proyecto no fue eliminado correctamente: {response.status_code}")
        return False
    
    print("🎉 Prueba CRUD de Proyectos completada exitosamente!\n")
    return True

def test_server_connection():
    """Prueba la conexión con el servidor"""
    print("🔗 Probando conexión con el servidor...")
    try:
        response = requests.get(f"{BASE_URL}/api/eventos", timeout=5)
        if response.status_code == 200:
            print("✅ Conexión exitosa con el servidor")
            return True
        else:
            print(f"❌ El servidor respondió con código: {response.status_code}")
            return False
    except requests.ConnectionError:
        print("❌ No se pudo conectar al servidor. Asegúrate de que esté ejecutándose en http://localhost:8000")
        return False
    except requests.Timeout:
        print("❌ Timeout al conectar con el servidor")
        return False

def main():
    """Función principal"""
    print("🧪 Iniciando pruebas CRUD para Eventos y Proyectos")
    print("=" * 60)
    
    # Probar conexión
    if not test_server_connection():
        print("\n❌ No se pudo establecer conexión con el servidor. Finalizando pruebas.")
        sys.exit(1)
    
    print()
    
    # Probar CRUD de eventos
    eventos_ok = test_eventos_crud()
    
    # Probar CRUD de proyectos
    proyectos_ok = test_proyectos_crud()
    
    # Resumen final
    print("=" * 60)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"🎯 Eventos CRUD: {'✅ EXITOSO' if eventos_ok else '❌ FALLIDO'}")
    print(f"🎯 Proyectos CRUD: {'✅ EXITOSO' if proyectos_ok else '❌ FALLIDO'}")
    
    if eventos_ok and proyectos_ok:
        print("\n🎉 ¡Todas las pruebas CRUD pasaron exitosamente!")
        print("La funcionalidad de edición y eliminación está funcionando correctamente.")
    else:
        print("\n❌ Algunas pruebas fallaron. Revisa los endpoints y la configuración.")
        sys.exit(1)

if __name__ == "__main__":
    main()
