#!/usr/bin/env python3
"""
Script para probar la funcionalidad CRUD completa de clientes.
Verifica que se pueden crear, leer, actualizar y eliminar clientes.
"""

import requests
import json
from datetime import datetime
import sys

# Configuración del servidor API
BASE_URL = "http://localhost:8000"

def test_clientes_crud():
    """Prueba las operaciones CRUD para clientes"""
    print("🧪 Probando CRUD de Clientes...")
    
    # 1. Crear cliente
    cliente_data = {
        "id_persona": 1,
        "tipo": "EMPRESA",
        "razon_social": "Cliente de Prueba CRUD S.L.",
        "nif": "B12345678",
        "fecha_registro": "2024-12-01"
    }
    
    print("📝 Creando cliente...")
    response = requests.post(f"{BASE_URL}/api/clientes", json=cliente_data)
    if response.status_code == 200:
        result = response.json()
        cliente_id = result.get('id_cliente')
        print(f"✅ Cliente creado exitosamente con ID: {cliente_id}")
    else:
        print(f"❌ Error al crear cliente: {response.status_code} - {response.text}")
        return False
    
    # 2. Listar clientes para verificar
    print("📋 Obteniendo lista de clientes...")
    response = requests.get(f"{BASE_URL}/api/clientes")
    if response.status_code == 200:
        clientes = response.json()
        cliente_creado = next((c for c in clientes if c.get('id_cliente') == cliente_id), None)
        if cliente_creado:
            print(f"✅ Cliente encontrado en la lista: {cliente_creado['razon_social']}")
        else:
            print("❌ No se encontró el cliente creado en la lista")
            return False
    else:
        print(f"❌ Error al obtener clientes: {response.status_code}")
        return False
    
    # 3. Obtener cliente específico
    print(f"🔍 Obteniendo cliente con ID {cliente_id}...")
    response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}")
    if response.status_code == 200:
        cliente_detalle = response.json()
        print(f"✅ Cliente obtenido: {cliente_detalle.get('razon_social', 'N/A')}")
    else:
        print(f"❌ Error al obtener cliente: {response.status_code}")
        return False
    
    # 4. Actualizar cliente
    print("✏️ Actualizando cliente...")
    cliente_actualizado = cliente_detalle.copy()
    cliente_actualizado['razon_social'] = "Cliente de Prueba CRUD S.L. - Actualizado"
    cliente_actualizado['tipo'] = "AUTONOMO"
    
    response = requests.put(f"{BASE_URL}/api/clientes/{cliente_id}", json=cliente_actualizado)
    if response.status_code == 200:
        print("✅ Cliente actualizado exitosamente")
    else:
        print(f"❌ Error al actualizar cliente: {response.status_code} - {response.text}")
        return False
    
    # 5. Verificar actualización
    print("🔍 Verificando actualización...")
    response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}")
    if response.status_code == 200:
        cliente_verificado = response.json()
        if (cliente_verificado.get('razon_social') == "Cliente de Prueba CRUD S.L. - Actualizado" and 
            cliente_verificado.get('tipo') == "AUTONOMO"):
            print("✅ Actualización verificada correctamente")
        else:
            print("❌ La actualización no se aplicó correctamente")
            return False
    else:
        print(f"❌ Error al verificar actualización: {response.status_code}")
        return False
    
    # 6. Eliminar cliente
    print("🗑️ Eliminando cliente...")
    response = requests.delete(f"{BASE_URL}/api/clientes/{cliente_id}")
    if response.status_code == 200:
        print("✅ Cliente eliminado exitosamente")
    else:
        print(f"❌ Error al eliminar cliente: {response.status_code} - {response.text}")
        return False
    
    # 7. Verificar eliminación
    print("🔍 Verificando eliminación...")
    response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}")
    if response.status_code == 404:
        print("✅ Eliminación verificada correctamente")
    else:
        print(f"❌ El cliente no fue eliminado correctamente: {response.status_code}")
        return False
    
    print("🎉 Prueba CRUD de Clientes completada exitosamente!\n")
    return True

def test_server_connection():
    """Prueba la conexión con el servidor"""
    print("🔗 Probando conexión con el servidor...")
    try:
        response = requests.get(f"{BASE_URL}/api/clientes", timeout=5)
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
    print("🧪 Iniciando pruebas CRUD para Clientes")
    print("=" * 60)
    
    # Probar conexión
    if not test_server_connection():
        print("\n❌ No se pudo establecer conexión con el servidor. Finalizando pruebas.")
        sys.exit(1)
    
    print()
    
    # Probar CRUD de clientes
    clientes_ok = test_clientes_crud()
    
    # Resumen final
    print("=" * 60)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"🎯 Clientes CRUD: {'✅ EXITOSO' if clientes_ok else '❌ FALLIDO'}")
    
    if clientes_ok:
        print("\n🎉 ¡Todas las pruebas CRUD pasaron exitosamente!")
        print("La funcionalidad de clientes está funcionando correctamente.")
        print("\n🎯 Para probar en el navegador:")
        print("   1. Ve a 'Ver Clientes'")
        print("   2. Haz clic en cualquier cliente para editarlo")
        print("   3. Modifica los datos y guarda")
        print("   4. Verifica que redirija a la lista")
        print("   5. Prueba la eliminación desde la zona de peligro")
    else:
        print("\n❌ Las pruebas fallaron. Revisa los endpoints y la configuración.")
        sys.exit(1)

if __name__ == "__main__":
    main()
