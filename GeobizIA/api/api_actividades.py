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
    datos = actividad.model_dump()
    valido, msg = validar_datos_actividad(datos)
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    from GeobizIA.controlador.dominios.actividad import Actividad
    
    obj = gestor.agregar(Actividad(
        tipo=datos['tipo'],
        nombre=datos['nombre'],
        descripcion=datos['descripcion'],
        responsable=datos['responsable'],
        duracion=datos['duracion'],
        coste_economico=datos['coste_economico'],
        coste_horas=datos['coste_horas'],
        facturacion=datos['facturacion'],
        resultados=datos.get('resultados', ''),
        valoracion=datos.get('valoracion', ''),
        observaciones=datos.get('observaciones', '')
    ))
    
    if obj is None:
        raise HTTPException(status_code=500, detail="No se pudo guardar la actividad")
    return {"mensaje": "Actividad guardada correctamente"}

@router.put("/api/actividades/{id_actividad}")
def actualizar_actividad(id_actividad: int, actividad: ActividadIn):
    datos = actividad.model_dump()
    valido, msg = validar_datos_actividad(datos)
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    
    from GeobizIA.controlador.dominios.actividad import Actividad
    actividad_obj = Actividad(
        id_actividad=id_actividad,
        **datos
    )
    
    if not gestor.actualizar(actividad_obj):
        raise HTTPException(status_code=404, detail="Actividad no encontrada o no se pudo actualizar")
    return {"mensaje": "Actividad actualizada correctamente"}

@router.delete("/api/actividades/{id_actividad}")
def eliminar_actividad(id_actividad: int):
    try:
        if not gestor.eliminar(id_actividad):
            raise HTTPException(status_code=404, detail="Actividad no encontrada o no se pudo eliminar")
        return {"mensaje": "Actividad eliminada correctamente"}
    except Exception as e:
        # Captura cualquier otro error inesperado del gestor
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@router.get("/api/actividades")
def listar_actividades():
    try:
        actividades = gestor.mostrar_todos_los_elem()
        return [a.to_dict() for a in actividades]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener actividades: {e}")

@router.get("/api/actividades/estadisticas")
def estadisticas_actividades():
    try:
        actividades = gestor.mostrar_todos_los_elem()
        actividades_dict = [a.to_dict() for a in actividades]
        return preparar_estadisticas_actividades(actividades_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar estadísticas: {str(e)}")

@router.get("/api/actividades/{id_actividad}")
def obtener_actividad(id_actividad: int):
    try:
        obj = gestor.buscar(id_actividad)
        if obj is None:
            raise HTTPException(status_code=404, detail="No encontrada")
        return obj.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener actividad: {e}")


