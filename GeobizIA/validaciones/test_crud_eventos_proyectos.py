#!/usr/bin/env python3
"""
Script para probar la funcionalidad de edición y eliminación de eventos y proyectos
"""

import requests
import json
import sys

# Configuración de la API
API_BASE_URL = "http://localhost:8000"

def test_servidor_funcionando():
    """Verifica que el servidor esté funcionando"""
    print("🔍 Verificando servidor...")
    try:
        response = requests.get(f"{API_BASE_URL}/docs", timeout=5)
        if response.status_code == 200:
            print("✅ Servidor funcionando correctamente")
            return True
        else:
            print(f"❌ Servidor responde con error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Servidor no está funcionando: {e}")
        return False

def test_crud_eventos():
    """Prueba CRUD completo para eventos"""
    print("\n🔍 Probando CRUD de eventos...")
    
    # 1. Crear evento de prueba
    evento_test = {
        "nombre": "Evento de Prueba CRUD",
        "tipo": "Prueba",
        "lugar": "Madrid",
        "fecha_comienzo": "2024-07-01",
        "fecha_final": "2024-07-02",
        "poblacion": "Madrid",
        "tematica": "Pruebas automatizadas"
    }
    
    try:
        # Crear
        print("  📝 Creando evento...")
        response = requests.post(f"{API_BASE_URL}/api/eventos", json=evento_test)
        if response.status_code != 200:
            print(f"❌ Error al crear evento: {response.status_code}")
            return False
        print("  ✅ Evento creado")
        
        # Obtener lista para encontrar el ID
        response = requests.get(f"{API_BASE_URL}/api/eventos")
        eventos = response.json()
        evento_id = None
        for evento in eventos:
            if evento.get('nombre') == evento_test['nombre']:
                evento_id = evento.get('id_evento')
                break
        
        if not evento_id:
            print("❌ No se pudo encontrar el evento creado")
            return False
        
        print(f"  ✅ Evento encontrado con ID: {evento_id}")
        
        # Actualizar
        print("  📝 Actualizando evento...")
        evento_actualizado = evento_test.copy()
        evento_actualizado['nombre'] = "Evento de Prueba CRUD - ACTUALIZADO"
        evento_actualizado['tipo'] = "Prueba Actualizada"
        
        response = requests.put(f"{API_BASE_URL}/api/eventos/{evento_id}", json=evento_actualizado)
        if response.status_code != 200:
            print(f"❌ Error al actualizar evento: {response.status_code} - {response.text}")
            return False
        print("  ✅ Evento actualizado")
        
        # Verificar actualización
        response = requests.get(f"{API_BASE_URL}/api/eventos/{evento_id}")
        if response.status_code == 200:
            evento_verificado = response.json()
            if evento_verificado.get('nombre') == evento_actualizado['nombre']:
                print("  ✅ Actualización verificada")
            else:
                print("❌ La actualización no se aplicó correctamente")
                return False
        
        # Eliminar
        print("  🗑️ Eliminando evento...")
        response = requests.delete(f"{API_BASE_URL}/api/eventos/{evento_id}")
        if response.status_code != 200:
            print(f"❌ Error al eliminar evento: {response.status_code} - {response.text}")
            return False
        print("  ✅ Evento eliminado")
        
        # Verificar eliminación
        response = requests.get(f"{API_BASE_URL}/api/eventos/{evento_id}")
        if response.status_code == 404:
            print("  ✅ Eliminación verificada")
        else:
            print("❌ El evento no fue eliminado correctamente")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error en CRUD de eventos: {e}")
        return False

def test_crud_proyectos():
    """Prueba CRUD completo para proyectos"""
    print("\n🔍 Probando CRUD de proyectos...")
    
    # 1. Crear proyecto de prueba
    proyecto_test = {
        "nombre": "Proyecto de Prueba CRUD",
        "descripcion": "Proyecto para probar funcionalidad CRUD completa",
        "estado": "PLANIFICACION",
        "fecha_inicio": "2024-07-01",
        "fecha_fin": "2024-12-01",
        "poblacion": "Barcelona",
        "responsable": "Sistema de Pruebas",
        "objetivos": "Verificar funcionalidad CRUD",
        "presupuesto": 5000.00
    }
    
    try:
        # Crear
        print("  📝 Creando proyecto...")
        response = requests.post(f"{API_BASE_URL}/api/proyectos", json=proyecto_test)
        if response.status_code != 200:
            print(f"❌ Error al crear proyecto: {response.status_code}")
            return False
        result = response.json()
        proyecto_id = result.get('id_proyecto')
        print(f"  ✅ Proyecto creado con ID: {proyecto_id}")
        
        if not proyecto_id:
            print("❌ No se pudo obtener el ID del proyecto creado")
            return False
        
        # Actualizar
        print("  📝 Actualizando proyecto...")
        proyecto_actualizado = proyecto_test.copy()
        proyecto_actualizado['nombre'] = "Proyecto de Prueba CRUD - ACTUALIZADO"
        proyecto_actualizado['estado'] = "EN_PROGRESO"
        proyecto_actualizado['presupuesto'] = 7500.00
        
        response = requests.put(f"{API_BASE_URL}/api/proyectos/{proyecto_id}", json=proyecto_actualizado)
        if response.status_code != 200:
            print(f"❌ Error al actualizar proyecto: {response.status_code} - {response.text}")
            return False
        print("  ✅ Proyecto actualizado")
        
        # Verificar actualización
        response = requests.get(f"{API_BASE_URL}/api/proyectos/{proyecto_id}")
        if response.status_code == 200:
            proyecto_verificado = response.json()
            if (proyecto_verificado.get('nombre') == proyecto_actualizado['nombre'] and 
                proyecto_verificado.get('estado') == proyecto_actualizado['estado']):
                print("  ✅ Actualización verificada")
            else:
                print("❌ La actualización no se aplicó correctamente")
                return False
        
        # Eliminar
        print("  🗑️ Eliminando proyecto...")
        response = requests.delete(f"{API_BASE_URL}/api/proyectos/{proyecto_id}")
        if response.status_code != 200:
            print(f"❌ Error al eliminar proyecto: {response.status_code} - {response.text}")
            return False
        print("  ✅ Proyecto eliminado")
        
        # Verificar eliminación
        response = requests.get(f"{API_BASE_URL}/api/proyectos/{proyecto_id}")
        if response.status_code == 404:
            print("  ✅ Eliminación verificada")
        else:
            print("❌ El proyecto no fue eliminado correctamente")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error en CRUD de proyectos: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 PRUEBAS DE FUNCIONALIDAD CRUD - EVENTOS Y PROYECTOS")
    print("=" * 60)
    
    # Lista de pruebas
    pruebas = [
        ("Servidor funcionando", test_servidor_funcionando),
        ("CRUD Eventos", test_crud_eventos),
        ("CRUD Proyectos", test_crud_proyectos)
    ]
    
    resultados = []
    
    for nombre, test_func in pruebas:
        print(f"\n{'='*30}")
        print(f"PRUEBA: {nombre}")
        print('='*30)
        
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ Error inesperado en {nombre}: {e}")
            resultados.append((nombre, False))
    
    # Resumen final
    print(f"\n{'='*60}")
    print("RESUMEN DE PRUEBAS CRUD")
    print('='*60)
    
    exitosas = 0
    for nombre, resultado in resultados:
        estado = "✅ EXITOSA" if resultado else "❌ FALLIDA"
        print(f"{nombre}: {estado}")
        if resultado:
            exitosas += 1
    
    total = len(resultados)
    print(f"\n📊 RESULTADO FINAL: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("\n🎉 ¡TODAS LAS PRUEBAS CRUD PASARON!")
        print("🎯 La funcionalidad de edición y eliminación está operativa")
        print("\n📋 Ahora puedes:")
        print("   - Hacer clic en eventos/proyectos para editarlos")
        print("   - Actualizar datos desde el formulario de detalle")
        print("   - Eliminar elementos con confirmación")
    else:
        print("\n⚠️ Algunas pruebas fallaron")
        print("🔧 Revisa los errores anteriores y verifica:")
        print("   - Que el servidor esté funcionando")
        print("   - Que la base de datos esté accesible")
        print("   - Que las APIs estén configuradas correctamente")
    
    return exitosas == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
