from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from GeobizIA.controlador.dominios.factura import Factura
from GeobizIA.controlador.gestores.facturas import Facturas
from GeobizIA.validaciones.validar_factura import validar_datos_factura

router = APIRouter()
gestor = Facturas()

class FacturaIn(BaseModel):
    id_cliente: int
    fecha_facturacion: str
    fecha_vencimiento: str
    concepto: str
    responsable: str
    iva: float
    coste_total: float
    base_imponible: float
    numero_factura: str
    tipo_pago: str
    irpf: float

@router.get("/api/facturas")
def listar_facturas():
    try:
        facturas = gestor.mostrar_todos_los_elem()
        return [f.to_dict() for f in facturas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener facturas: {e}")

@router.get("/api/facturas/{id_factura}")
def obtener_factura(id_factura: int):
    try:
        obj = gestor.buscar(id_factura)
        if obj is None:
            raise HTTPException(status_code=404, detail="Factura no encontrada")
        return obj.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener factura: {e}")

@router.post("/api/facturas")
def crear_factura(factura: FacturaIn):
    try:
        datos = factura.model_dump()
        valido, msg = validar_datos_factura(datos)
        if not valido:
            raise HTTPException(status_code=400, detail=msg)
        
        factura_a_guardar = Factura(
            id_factura=None,  # Se auto-genera en la base de datos
            id_cliente=datos['id_cliente'],
            tipo=None,  # Campo opcional
            nombre=None,  # Campo opcional
            direccion=None,  # Campo opcional
            nif=None,  # Campo opcional
            fecha_facturacion=datos['fecha_facturacion'],
            fecha_vencimiento=datos['fecha_vencimiento'],
            concepto=datos['concepto'],
            responsable=datos['responsable'],
            iva=datos['iva'],
            coste_total=datos['coste_total'],
            base_imponible=datos['base_imponible'],
            numero_factura=datos['numero_factura'],
            tipo_pago=datos['tipo_pago'],
            irpf=datos['irpf']
        )

        obj = gestor.agregar(factura_a_guardar)
        
        if obj is None:
            raise HTTPException(status_code=500, detail="El gestor no pudo guardar la factura, devolvió None.")
        return {"mensaje": "Factura guardada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor al crear la factura: {e}")

@router.put("/api/facturas/{id_factura}")
def actualizar_factura(id_factura: int, factura: FacturaIn):
    try:
        # Primero verificar que la factura existe
        factura_existente = gestor.buscar(id_factura)
        if factura_existente is None:
            raise HTTPException(status_code=404, detail="Factura no encontrada")
        
        datos = factura.model_dump()
        valido, msg = validar_datos_factura(datos)
        if not valido:
            raise HTTPException(status_code=400, detail=msg)
        
        factura_obj = Factura(
            id_factura=id_factura,
            id_cliente=datos['id_cliente'],
            tipo=factura_existente.tipo,  # Mantener valores existentes
            nombre=factura_existente.nombre,
            direccion=factura_existente.direccion,
            nif=factura_existente.nif,
            fecha_facturacion=datos['fecha_facturacion'],
            fecha_vencimiento=datos['fecha_vencimiento'],
            concepto=datos['concepto'],
            responsable=datos['responsable'],
            iva=datos['iva'],
            coste_total=datos['coste_total'],
            base_imponible=datos['base_imponible'],
            numero_factura=datos['numero_factura'],
            tipo_pago=datos['tipo_pago'],
            irpf=datos['irpf']
        )
        
        if not gestor.actualizar(factura_obj):
            raise HTTPException(status_code=404, detail="Factura no encontrada o no se pudo actualizar")
        return {"mensaje": "Factura actualizada correctamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@router.delete("/api/facturas/{id_factura}")
def eliminar_factura(id_factura: int):
    try:
        if not gestor.eliminar(id_factura):
            raise HTTPException(status_code=404, detail="Factura no encontrada o no se pudo eliminar")
        return {"mensaje": "Factura eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")
