from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from GeobizIA.controlador.dominios.actividad_realizada import ActividadRealizada
from GeobizIA.controlador.gestores.actividades_realizadas import ActividadesRealizadas
from GeobizIA.controlador.gestores.actividades import Actividades
from GeobizIA.controlador.ML.ML_actividades_realizadas_prediccion import realizar_prediccion_actividad
from GeobizIA.controlador.ML.ML_actividades import preparar_estadisticas_actividades
from GeobizIA.validaciones.validar_actividad_realizada import validar_datos_actividad_realizada

router = APIRouter()
gestor = ActividadesRealizadas()

class ActividadRealizadaIn(BaseModel):
    id_actividad: int
    fecha: str
    asistentes: Optional[int] = None
    coste_economico: Optional[float] = None
    facturacion: Optional[float] = None
    observaciones: Optional[str] = ""
    id_evento: Optional[int] = None
    id_proyecto: Optional[int] = None

class PrediccionIn(BaseModel):
    id_actividad: int
    fecha: str
    coste_economico: float

@router.post("/api/actividades_realizadas")
def crear_actividad_realizada(actividad: ActividadRealizadaIn):
    datos = actividad.dict()
    valido, msg = validar_datos_actividad_realizada(datos)
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    
    # ✅ SEGURO: Solo campos esperados (evita inyección de campos)
    obj = gestor.agregar(ActividadRealizada(
        id_actividad=datos['id_actividad'],
        fecha=datos['fecha'],
        asistentes=datos.get('asistentes'),
        coste_economico=datos.get('coste_economico'),
        facturacion=datos.get('facturacion'),
        observaciones=datos.get('observaciones', ''),
        id_evento=datos.get('id_evento'),
        id_proyecto=datos.get('id_proyecto')
    ))
    
    if obj is None:
        raise HTTPException(status_code=500, detail="No se pudo guardar la actividad realizada")
    return {"mensaje": "Actividad realizada guardada correctamente"}

@router.get("/api/actividades_realizadas")
def listar_actividades_realizadas():
    actividades = gestor.mostrar_todos_los_elem()
    return [a.to_dict() for a in actividades]

@router.get("/api/actividades_realizadas/estadisticas")
def estadisticas_actividades_realizadas():
    try:
        actividades_realizadas = gestor.mostrar_todos_los_elem()
        actividades_dicts = [a.to_dict() for a in actividades_realizadas]
        
        # Mapeo id_actividad -> nombre
        actividades = Actividades().mostrar_todos_los_elem()
        id_to_nombre = {a.id_actividad: a.nombre for a in actividades}
        
        resultado = preparar_estadisticas_actividades(actividades_dicts, id_to_nombre)
        return resultado
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar estadísticas: {str(e)}")

@router.get("/api/actividades_realizadas/test")
def test_endpoint():
    """Endpoint de prueba para verificar que el servidor funciona"""
    return {"status": "ok", "mensaje": "Servidor funcionando correctamente"}

@router.get("/api/actividades_realizadas/{id_actividad_realizada}")
def obtener_actividad_realizada(id_actividad_realizada: int):
    obj = gestor.buscar(id_actividad_realizada)
    if obj is None:
        raise HTTPException(status_code=404, detail="No encontrada")
    return obj.to_dict()

@router.post("/api/actividades_realizadas/prediccion")
def prediccion_actividad_realizada(datos_prediccion: PrediccionIn):
    """Predice asistentes y facturación basado en id_actividad, fecha y coste_economico"""
    try:
        actividades_realizadas = gestor.mostrar_todos_los_elem()
        actividades_dicts = [a.to_dict() for a in actividades_realizadas]
        
        # Mapeo id_actividad -> nombre
        actividades = Actividades().mostrar_todos_los_elem()
        id_to_nombre = {a.id_actividad: a.nombre for a in actividades}
        
        # Validar que la actividad existe
        if datos_prediccion.id_actividad not in id_to_nombre:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")
        
        # Realizar predicción
        resultado = realizar_prediccion_actividad(
            actividades_dicts,
            datos_prediccion.id_actividad,
            datos_prediccion.fecha,
            datos_prediccion.coste_economico,
            id_to_nombre
        )
        
        if resultado['error']:
            raise HTTPException(status_code=400, detail=resultado['mensaje'])
        
        return resultado
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno en predicción: {str(e)}")
