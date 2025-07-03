# filepath: c:\Users\Geobizi\Desktop\Programacion\GeobizIA\GoffardSevillanoAintzane\src\api\actividades.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.controlador.gestores.actividades import Actividades
from src.controlador.validaciones.validar_actividad import validar_datos_actividad

router = APIRouter()
gestor = Actividades()

class ActividadIn(BaseModel):
    id_actividad: int
    tipo: str
    nombre: str
    descripcion: str
    responsable: str
    duracion: str
    coste_economico: float
    coste_horas: float
    facturacion: float
    resultados: str = ""
    valoracion: str = ""
    observaciones: str = ""

@router.post("/api/actividades")
def crear_actividad(actividad: ActividadIn):
    valido, msg = validar_datos_actividad(actividad.dict())
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    obj = gestor.agregar(actividad)
    if obj is None:
        raise HTTPException(status_code=500, detail="No se pudo guardar la actividad")
    return {"mensaje": "Actividad guardada correctamente"}

@router.get("/api/actividades/{id_actividad}")
def obtener_actividad(id_actividad: int):
    obj = gestor.buscar(id_actividad)
    if obj is None:
        raise HTTPException(status_code=404, detail="No encontrada")
    return obj