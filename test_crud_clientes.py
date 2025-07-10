#!/usr/bin/env python3
"""
Script de prueba para verificar el funcionamiento correcto del CRUD de clientes
después de las correcciones realizadas.
"""

import requests
import json
import sys
import time

# Configuración del servidor
BASE_URL = "http://localhost:8000"
CLIENTES_URL = f"{BASE_URL}/api/clientes"

def test_crear_cliente():
    """Prueba la creación de un cliente"""
    print("🔵 Probando creación de cliente...")
    
    cliente_data = {
        "nombre": "Juan Carlos",
        "apellido": "Pérez García",
        "email": "juan.perez@email.com",
        "telefono": "123456789",
        "dni": "12345678A",
        "direccion": "Calle Falsa 123",
        "cp": "28001",
        "poblacion": "Madrid",
        "pais": "España",
        "tipo": "individual",
        "razon_social": "Juan Carlos Pérez García",
        "nif": "12345678A",
        "fecha_registro": "2024-01-15"
    }
    
    try:
        response = requests.post(CLIENTES_URL, json=cliente_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Cliente creado exitosamente")
            return result.get('id_cliente'), result.get('id_persona')
        else:
            print("❌ Error al crear cliente")
            return None, None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None, None

def test_obtener_cliente(id_cliente):
    """Prueba obtener un cliente por ID"""
    print(f"🔵 Probando obtención de cliente ID: {id_cliente}")
    
    try:
        response = requests.get(f"{CLIENTES_URL}/{id_cliente}")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            cliente = response.json()
            print("✅ Cliente obtenido exitosamente")
            print(f"Datos: {json.dumps(cliente, indent=2, ensure_ascii=False)}")
            return cliente
        elif response.status_code == 404:
            print("❌ Cliente no encontrado")
            return None
        else:
            print(f"❌ Error al obtener cliente: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def test_listar_clientes():
    """Prueba listar todos los clientes"""
    print("🔵 Probando listado de clientes...")
    
    try:
        response = requests.get(CLIENTES_URL)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            clientes = response.json()
            print(f"✅ Listado obtenido exitosamente. Total: {len(clientes)}")
            return clientes
        else:
            print(f"❌ Error al listar clientes: {response.text}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return []

def test_actualizar_cliente(id_cliente):
    """Prueba actualizar un cliente"""
    print(f"🔵 Probando actualización de cliente ID: {id_cliente}")
    
    cliente_actualizado = {
        "nombre": "Juan Carlos",
        "apellido": "Pérez García",
        "email": "juan.perez.actualizado@email.com",
        "telefono": "987654321",
        "dni": "12345678A",
        "direccion": "Calle Actualizada 456",
        "cp": "28002",
        "poblacion": "Madrid",
        "pais": "España",
        "tipo": "empresa",
        "razon_social": "Empresa Juan Carlos S.L.",
        "nif": "B12345678",
        "fecha_registro": "2024-01-15"
    }
    
    try:
        response = requests.put(f"{CLIENTES_URL}/{id_cliente}", json=cliente_actualizado)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Cliente actualizado exitosamente")
            return True
        else:
            print("❌ Error al actualizar cliente")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_eliminar_cliente(id_cliente):
    """Prueba eliminar un cliente"""
    print(f"🔵 Probando eliminación de cliente ID: {id_cliente}")
    
    try:
        response = requests.delete(f"{CLIENTES_URL}/{id_cliente}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Cliente eliminado exitosamente")
            return True
        else:
            print("❌ Error al eliminar cliente")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_servidor_disponible():
    """Verifica si el servidor está disponible"""
    print("🔵 Verificando disponibilidad del servidor...")
    
    try:
        response = requests.get(BASE_URL, timeout=5)
        print("✅ Servidor disponible")
        return True
    except requests.exceptions.RequestException:
        print("❌ Servidor no disponible")
        return False

def main():
    """Función principal que ejecuta todas las pruebas"""
    print("🚀 Iniciando pruebas CRUD de clientes (versión corregida)")
    print("=" * 60)
    
    # Verificar servidor
    if not test_servidor_disponible():
        print("❌ No se puede conectar al servidor. Asegúrate de que esté ejecutándose.")
        sys.exit(1)
    
    # Paso 1: Crear cliente
    print("\n" + "=" * 60)
    id_cliente, id_persona = test_crear_cliente()
    if not id_cliente:
        print("❌ No se pudo crear el cliente. Abortando pruebas.")
        sys.exit(1)
    
    print(f"🔑 Cliente creado con ID: {id_cliente}, Persona ID: {id_persona}")
    time.sleep(1)
    
    # Paso 2: Obtener cliente
    print("\n" + "=" * 60)
    cliente = test_obtener_cliente(id_cliente)
    if not cliente:
        print("❌ No se pudo obtener el cliente creado.")
        sys.exit(1)
    
    time.sleep(1)
    
    # Paso 3: Listar clientes
    print("\n" + "=" * 60)
    clientes = test_listar_clientes()
    time.sleep(1)
    
    # Paso 4: Actualizar cliente
    print("\n" + "=" * 60)
    if test_actualizar_cliente(id_cliente):
        time.sleep(1)
        # Verificar que la actualización se aplicó
        print("\n🔍 Verificando actualización...")
        cliente_actualizado = test_obtener_cliente(id_cliente)
        if cliente_actualizado and cliente_actualizado.get('email') == 'juan.perez.actualizado@email.com':
            print("✅ Actualización verificada correctamente")
        else:
            print("❌ La actualización no se aplicó correctamente")
    else:
        print("❌ No se pudo actualizar el cliente.")
    
    time.sleep(1)
    
    # Paso 5: Eliminar cliente
    print("\n" + "=" * 60)
    if test_eliminar_cliente(id_cliente):
        time.sleep(1)
        # Verificar que la eliminación se aplicó
        print("\n🔍 Verificando eliminación...")
        cliente_eliminado = test_obtener_cliente(id_cliente)
        if cliente_eliminado is None:
            print("✅ Eliminación verificada correctamente - Cliente no encontrado (404)")
        else:
            print("❌ La eliminación no se aplicó correctamente - Cliente aún existe")
    else:
        print("❌ No se pudo eliminar el cliente.")
    
    print("\n" + "=" * 60)
    print("🏁 Pruebas completadas")

if __name__ == "__main__":
    main()
