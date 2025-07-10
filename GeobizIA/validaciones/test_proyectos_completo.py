#!/usr/bin/env python3
"""
Script para probar la funcionalidad completa de proyectos en GeobizIA.
Verifica la creación, listado y validación de proyectos.
"""

import requests
import json
import sys
import os

# Configuración de la API
API_BASE_URL = "http://localhost:8000"
API_PROYECTOS_URL = f"{API_BASE_URL}/api/proyectos"

def test_crear_proyecto():
    """Prueba la creación de un proyecto"""
    print("🔸 Probando creación de proyecto...")
    
    # Datos de prueba válidos
    proyecto_datos = {
        "nombre": "Proyecto de Prueba GeobizIA",
        "descripcion": "Este es un proyecto de prueba para verificar la funcionalidad completa del sistema de proyectos en GeobizIA.",
        "fecha_inicio": "2024-01-15",
        "fecha_fin": "2024-06-15",
        "poblacion": "Madrid, España",
        "responsable": "Juan Pérez",
        "estado": "PLANIFICACION",
        "objetivos": "Verificar que el sistema de proyectos funciona correctamente con validación y sanitización.",
        "presupuesto": 25000.50
    }
    
    try:
        response = requests.post(API_PROYECTOS_URL, json=proyecto_datos)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Proyecto creado exitosamente: {result}")
            return True
        else:
            print(f"❌ Error al crear proyecto: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión al crear proyecto: {e}")
        return False

def test_listar_proyectos():
    """Prueba el listado de proyectos"""
    print("\n🔸 Probando listado de proyectos...")
    
    try:
        response = requests.get(API_PROYECTOS_URL)
        
        if response.status_code == 200:
            proyectos = response.json()
            print(f"✅ Proyectos obtenidos exitosamente: {len(proyectos)} proyectos encontrados")
            
            # Mostrar detalles de los proyectos
            for i, proyecto in enumerate(proyectos, 1):
                print(f"  {i}. {proyecto.get('nombre', 'Sin nombre')} - Estado: {proyecto.get('estado', 'Sin estado')}")
            
            return True
        else:
            print(f"❌ Error al obtener proyectos: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión al obtener proyectos: {e}")
        return False

def test_validacion_proyecto():
    """Prueba la validación de proyectos con datos inválidos"""
    print("\n🔸 Probando validación de proyectos...")
    
    # Datos inválidos para probar validación
    casos_invalidos = [
        {
            "datos": {
                "nombre": "AB",  # Muy corto
                "descripcion": "Descripción de prueba para validar la longitud mínima",
                "estado": "PLANIFICACION"
            },
            "descripcion": "Nombre muy corto"
        },
        {
            "datos": {
                "nombre": "Proyecto válido",
                "descripcion": "Corta",  # Muy corta
                "estado": "PLANIFICACION"
            },
            "descripcion": "Descripción muy corta"
        },
        {
            "datos": {
                "nombre": "Proyecto válido",
                "descripcion": "Descripción válida para el proyecto de prueba",
                "estado": "ESTADO_INVALIDO"  # Estado inválido
            },
            "descripcion": "Estado inválido"
        },
        {
            "datos": {
                "nombre": "",  # Nombre vacío
                "descripcion": "Descripción válida para el proyecto de prueba",
                "estado": "PLANIFICACION"
            },
            "descripcion": "Nombre vacío"
        }
    ]
    
    validaciones_correctas = 0
    total_casos = len(casos_invalidos)
    
    for caso in casos_invalidos:
        try:
            response = requests.post(API_PROYECTOS_URL, json=caso["datos"])
            
            if response.status_code == 400:
                print(f"✅ Validación correcta para {caso['descripcion']}: {response.json().get('detail', 'Error de validación')}")
                validaciones_correctas += 1
            else:
                print(f"❌ Error: {caso['descripcion']} debería haber sido rechazado pero fue aceptado")
                
        except Exception as e:
            print(f"❌ Error de conexión en validación {caso['descripcion']}: {e}")
    
    print(f"\n📊 Resultados de validación: {validaciones_correctas}/{total_casos} casos validados correctamente")
    return validaciones_correctas == total_casos

def test_obtener_proyecto_individual():
    """Prueba obtener un proyecto específico por ID"""
    print("\n🔸 Probando obtención de proyecto individual...")
    
    try:
        # Primero obtener la lista para tener un ID válido
        response = requests.get(API_PROYECTOS_URL)
        if response.status_code == 200:
            proyectos = response.json()
            if proyectos:
                proyecto_id = proyectos[0].get('id_proyecto')
                if proyecto_id:
                    # Obtener el proyecto específico
                    response_individual = requests.get(f"{API_PROYECTOS_URL}/{proyecto_id}")
                    if response_individual.status_code == 200:
                        proyecto = response_individual.json()
                        print(f"✅ Proyecto obtenido exitosamente: {proyecto.get('nombre', 'Sin nombre')}")
                        return True
                    else:
                        print(f"❌ Error al obtener proyecto individual: {response_individual.status_code}")
                        return False
                else:
                    print("❌ No se encontró un ID válido en los proyectos")
                    return False
            else:
                print("⚠️ No hay proyectos disponibles para probar obtención individual")
                return True  # No es un error si no hay proyectos
        else:
            print(f"❌ Error al obtener lista de proyectos: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error de conexión al obtener proyecto individual: {e}")
        return False

def verificar_servidor():
    """Verifica que el servidor esté funcionando"""
    print("🔸 Verificando conexión con el servidor...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/docs")
        if response.status_code == 200:
            print("✅ Servidor funcionando correctamente")
            return True
        else:
            print(f"❌ Servidor no responde correctamente: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ No se puede conectar al servidor: {e}")
        print("💡 Asegúrate de que el servidor esté funcionando en http://localhost:8000")
        return False

def main():
    """Función principal que ejecuta todas las pruebas"""
    print("🚀 Iniciando pruebas completas de la funcionalidad de proyectos\n")
    
    # Verificar conexión al servidor
    if not verificar_servidor():
        print("\n❌ No se puede continuar sin conexión al servidor")
        return False
    
    # Ejecutar todas las pruebas
    pruebas = [
        ("Crear proyecto", test_crear_proyecto),
        ("Listar proyectos", test_listar_proyectos),
        ("Validación de proyectos", test_validacion_proyecto),
        ("Obtener proyecto individual", test_obtener_proyecto_individual)
    ]
    
    resultados = []
    
    for nombre, test_func in pruebas:
        print(f"\n{'='*50}")
        print(f"Ejecutando: {nombre}")
        print('='*50)
        
        resultado = test_func()
        resultados.append((nombre, resultado))
    
    # Mostrar resumen final
    print(f"\n{'='*50}")
    print("RESUMEN DE PRUEBAS")
    print('='*50)
    
    exitosas = 0
    for nombre, resultado in resultados:
        estado = "✅ EXITOSA" if resultado else "❌ FALLIDA"
        print(f"{nombre}: {estado}")
        if resultado:
            exitosas += 1
    
    total = len(resultados)
    print(f"\n📊 Resultado final: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("🎉 ¡Todas las pruebas han pasado! La funcionalidad de proyectos está funcionando correctamente.")
        return True
    else:
        print("⚠️ Algunas pruebas fallaron. Revisa los errores anteriores.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
