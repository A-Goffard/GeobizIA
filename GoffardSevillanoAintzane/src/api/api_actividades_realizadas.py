from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.controlador.gestores.actividades_realizadas import ActividadesRealizadas
from src.controlador.gestores.actividades import Actividades
from src.controlador.dominios.actividad_realizada import ActividadRealizada
from src.controlador.ML.ML_actividades_realizadas import preparar_estadisticas_actividades

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

@router.post("/api/actividades_realizadas")
def crear_actividad_realizada(actividad: ActividadRealizadaIn):
    obj = gestor.agregar(ActividadRealizada(**actividad.dict()))
    if obj is None:
        raise HTTPException(status_code=500, detail="No se pudo guardar la actividad realizada")
    return {"mensaje": "Actividad realizada guardada correctamente"}

@router.get("/api/actividades_realizadas")
def listar_actividades_realizadas():
    actividades = gestor.mostrar_todos_los_elem()
    return [a.to_dict() for a in actividades]

@router.get("/api/actividades_realizadas/estadisticas")
def estadisticas_actividades_realizadas():
    actividades_realizadas = gestor.mostrar_todos_los_elem()
    actividades_dicts = [a.to_dict() for a in actividades_realizadas]
    # Mapeo id_actividad -> nombre
    actividades = Actividades().mostrar_todos_los_elem()
    id_to_nombre = {a.id_actividad: a.nombre for a in actividades}
    return preparar_estadisticas_actividades(actividades_dicts, id_to_nombre)

@router.get("/api/actividades_realizadas/{id_actividad_realizada}")
def obtener_actividad_realizada(id_actividad_realizada: int):
    obj = gestor.buscar(id_actividad_realizada)
    if obj is None:
        raise HTTPException(status_code=404, detail="No encontrada")
    return obj.to_dict()
