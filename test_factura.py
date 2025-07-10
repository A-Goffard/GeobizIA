from GeobizIA.controlador.dominios.factura import Factura
from GeobizIA.controlador.gestores.facturas import Facturas

# Crear una factura de prueba
factura_test = Factura(
    id_factura=None,  # Se auto-generará
    id_cliente=1,  # Usar ID de cliente existente
    tipo=None,
    nombre=None,
    direccion=None,
    nif=None,
    fecha_facturacion="2025-07-11",
    fecha_vencimiento="2025-07-24",
    concepto="Factura de prueba desde gestor",
    responsable="Usuario de prueba",
    iva=21,
    coste_total=500,
    base_imponible=300,
    numero_factura="FAC-TEST-002",
    tipo_pago="transferencia",
    irpf=15
)

# Probar el gestor
gestor = Facturas()
resultado = gestor.agregar(factura_test)

if resultado:
    print(f"✅ Factura creada exitosamente: {resultado.to_dict()}")
else:
    print("❌ Error al crear la factura")
