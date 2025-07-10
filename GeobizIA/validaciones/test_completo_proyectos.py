#!/usr/bin/env python3
"""
Script de prueba completo para verificar la funcionalidad de proyectos
"""

import requests
import json
import time
import sys

# Configuración
API_BASE_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:8080"

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

def test_crear_proyecto():
    """Prueba crear un proyecto"""
    print("\n🔍 Probando creación de proyecto...")
    
    proyecto_test = {
        "nombre": "Proyecto de Prueba Automatizada",
        "descripcion": "Este es un proyecto creado automáticamente para probar la funcionalidad completa del sistema.",
        "estado": "PLANIFICACION",
        "fecha_inicio": "2024-01-15",
        "fecha_fin": "2024-06-15",
        "poblacion": "Madrid, España",
        "responsable": "Sistema de Pruebas",
        "objetivos": "Verificar que el sistema de proyectos funciona correctamente con todas las validaciones.",
        "presupuesto": 15000.00
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/api/proyectos", json=proyecto_test)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Proyecto creado exitosamente (ID: {result.get('id_proyecto', 'N/A')})")
            return True
        else:
            print(f"❌ Error al crear proyecto: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_listar_proyectos():
    """Prueba listar proyectos"""
    print("\n🔍 Probando listado de proyectos...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/api/proyectos")
        if response.status_code == 200:
            proyectos = response.json()
            print(f"✅ Se obtuvieron {len(proyectos)} proyectos")
            for i, proyecto in enumerate(proyectos[:3], 1):  # Mostrar solo los primeros 3
                print(f"  {i}. {proyecto.get('nombre', 'Sin nombre')} - {proyecto.get('estado', 'Sin estado')}")
            return True
        else:
            print(f"❌ Error al obtener proyectos: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_validacion_proyecto():
    """Prueba las validaciones"""
    print("\n🔍 Probando validaciones...")
    
    # Proyecto con datos inválidos
    proyecto_invalido = {
        "nombre": "AB",  # Muy corto
        "descripcion": "Descripción válida para el proyecto de prueba",
        "estado": "PLANIFICACION"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/api/proyectos", json=proyecto_invalido)
        if response.status_code == 400:
            print("✅ Validación funcionando correctamente (datos inválidos rechazados)")
            return True
        else:
            print(f"❌ Error: datos inválidos fueron aceptados")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_obtener_proyecto_individual():
    """Prueba obtener un proyecto específico"""
    print("\n🔍 Probando obtención de proyecto individual...")
    
    try:
        # Primero obtener lista de proyectos
        response = requests.get(f"{API_BASE_URL}/api/proyectos")
        if response.status_code == 200:
            proyectos = response.json()
            if proyectos:
                proyecto_id = proyectos[0].get('id_proyecto')
                if proyecto_id:
                    # Obtener proyecto específico
                    response_individual = requests.get(f"{API_BASE_URL}/api/proyectos/{proyecto_id}")
                    if response_individual.status_code == 200:
                        proyecto = response_individual.json()
                        print(f"✅ Proyecto obtenido: {proyecto.get('nombre', 'Sin nombre')}")
                        return True
                    else:
                        print(f"❌ Error al obtener proyecto: {response_individual.status_code}")
                        return False
                else:
                    print("❌ No se encontró ID válido")
                    return False
            else:
                print("ℹ️ No hay proyectos para probar")
                return True
        else:
            print(f"❌ Error al listar proyectos: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 PRUEBAS COMPLETAS DE FUNCIONALIDAD DE PROYECTOS")
    print("=" * 55)
    
    # Lista de pruebas
    pruebas = [
        ("Servidor funcionando", test_servidor_funcionando),
        ("Crear proyecto", test_crear_proyecto),
        ("Listar proyectos", test_listar_proyectos),
        ("Validación de datos", test_validacion_proyecto),
        ("Obtener proyecto individual", test_obtener_proyecto_individual)
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
    print(f"\n{'='*55}")
    print("RESUMEN DE PRUEBAS")
    print('='*55)
    
    exitosas = 0
    for nombre, resultado in resultados:
        estado = "✅ EXITOSA" if resultado else "❌ FALLIDA"
        print(f"{nombre}: {estado}")
        if resultado:
            exitosas += 1
    
    total = len(resultados)
    print(f"\n📊 RESULTADO FINAL: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("🎯 La funcionalidad de proyectos está completamente operativa")
        print("\n📋 Puedes usar:")
        print("   - API: http://localhost:8000/api/proyectos")
        print("   - Documentación: http://localhost:8000/docs")
        print("   - Frontend: http://localhost:8080")
    else:
        print("\n⚠️ Algunas pruebas fallaron")
        print("🔧 Revisa los errores anteriores y verifica:")
        print("   - Que el servidor esté funcionando")
        print("   - Que la base de datos esté accesible")
        print("   - Que no haya problemas de red")
    
    return exitosas == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
