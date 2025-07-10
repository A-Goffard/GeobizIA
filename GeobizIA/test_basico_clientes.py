#!/usr/bin/env python3
"""
Script simplificado para probar las operaciones básicas de clientes
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_basico():
    print("🧪 Prueba básica de clientes")
    
    # 1. Listar clientes existentes
    print("📋 Listando clientes...")
    response = requests.get(f"{BASE_URL}/api/clientes")
    if response.status_code == 200:
        clientes = response.json()
        print(f"✅ Se encontraron {len(clientes)} clientes")
    else:
        print(f"❌ Error al listar: {response.status_code}")
        return
    
    # 2. Crear cliente
    cliente_data = {
        "id_persona": 1,
        "tipo": "EMPRESA",
        "razon_social": "Prueba Básica S.L.",
        "nif": "B98765432",
        "fecha_registro": "2024-12-01"
    }
    
    print("📝 Creando cliente...")
    response = requests.post(f"{BASE_URL}/api/clientes", json=cliente_data)
    if response.status_code == 200:
        result = response.json()
        cliente_id = result.get('id_cliente')
        print(f"✅ Cliente creado con ID: {cliente_id}")
        
        # 3. Obtener cliente
        print(f"🔍 Obteniendo cliente {cliente_id}...")
        response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}")
        if response.status_code == 200:
            cliente = response.json()
            print(f"✅ Cliente obtenido: {cliente.get('razon_social')}")
        else:
            print(f"❌ Error al obtener: {response.status_code}")
        
    else:
        print(f"❌ Error al crear: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_basico()
