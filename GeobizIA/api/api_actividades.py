from fastapi import APIRouter, HTTPException
router = APIRouter()
from typing import Optional
from pydantic import BaseModel
from GeobizIA.controlador.gestores.actividades import Actividades
from GeobizIA.validaciones.validar_actividad import validar_datos_actividad
from GeobizIA.controlador.ML.ML_actividades import preparar_estadisticas_actividades

router = APIRouter()
gestor = Actividades()

class ActividadIn(BaseModel):
    tipo: str
    nombre: str
    descripcion: str
    responsable: str
    duracion: str
    coste_economico: float
    coste_horas: float
    facturacion: float
    resultados: Optional[str] = ""
    valoracion: Optional[str] = ""
    observaciones: Optional[str] = ""

@router.post("/api/actividades")
def crear_actividad(actividad: ActividadIn):
    datos = actividad.dict()
    valido, msg = validar_datos_actividad(datos)
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    from GeobizIA.controlador.dominios.actividad import Actividad
    # Aquí se crea el objeto Actividad a partir de los datos validados del usuario
    obj = gestor.agregar(Actividad(**datos))
    if obj is None:
        raise HTTPException(status_code=500, detail="No se pudo guardar la actividad")
    return {"mensaje": "Actividad guardada correctamente"}

@router.get("/api/actividades/estadisticas")
def estadisticas_actividades():
    actividades = gestor.mostrar_todos_los_elem()
    # Convierte a dict explícitamente antes de pasar a la función ML
    actividades_dict = [a.to_dict() for a in actividades]
    return preparar_estadisticas_actividades(actividades_dict)

@router.get("/api/actividades")
def listar_actividades():
    actividades = gestor.mostrar_todos_los_elem()
    return [a.to_dict() for a in actividades]

@router.get("/api/actividades/{id_actividad}")
def obtener_actividad(id_actividad: int):
    obj = gestor.buscar(id_actividad)
    if obj is None:
        raise HTTPException(status_code=404, detail="No encontrada")
    return obj


