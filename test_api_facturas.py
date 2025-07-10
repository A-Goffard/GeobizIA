import requests
import json

# Datos de la factura para probar
factura_data = {
    "id_cliente": 1,
    "fecha_facturacion": "2025-07-11",
    "fecha_vencimiento": "2025-07-24",
    "concepto": "Servicios de consultoría ambiental",
    "responsable": "Juan Pérez",
    "iva": 21.0,
    "coste_total": 363.0,
    "base_imponible": 300.0,
    "numero_factura": "FAC-API-001",
    "tipo_pago": "transferencia",
    "irpf": 15.0
}

# Probar creación de factura
print("🧪 Probando creación de factura vía API...")
try:
    response = requests.post('http://localhost:8000/api/facturas', json=factura_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ Factura creada exitosamente")
        
        # Probar listado de facturas
        print("\n🧪 Probando listado de facturas...")
        response = requests.get('http://localhost:8000/api/facturas')
        if response.status_code == 200:
            facturas = response.json()
            print(f"✅ Se encontraron {len(facturas)} facturas")
            if facturas:
                print(f"Última factura: {facturas[-1]}")
        else:
            print(f"❌ Error al listar facturas: {response.status_code}")
    else:
        print("❌ Error al crear factura")
        print(f"Error: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ No se pudo conectar al servidor. ¿Está ejecutándose en localhost:8000?")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
