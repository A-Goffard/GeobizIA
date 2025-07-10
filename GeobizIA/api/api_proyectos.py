from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from GeobizIA.controlador.dominios.proyecto import Proyecto
from GeobizIA.controlador.gestores.proyectos import Proyectos
from GeobizIA.validaciones.validar_proyecto import validar_datos_proyecto

router = APIRouter()
gestor = Proyectos()

class ProyectoIn(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None
    poblacion: Optional[str] = None
    responsable: Optional[str] = None
    estado: str
    objetivos: Optional[str] = None
    presupuesto: Optional[float] = None

@router.get("/api/proyectos")
def listar_proyectos():
    try:
        proyectos = gestor.mostrar_todos_los_elem()
        return [p.to_dict() for p in proyectos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener proyectos: {e}")

@router.get("/api/proyectos/{id_proyecto}")
def obtener_proyecto(id_proyecto: int):
    try:
        obj = gestor.buscar(id_proyecto)
        if obj is None:
            raise HTTPException(status_code=404, detail="No encontrado")
        return obj.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener proyecto: {e}")

@router.post("/api/proyectos")
def crear_proyecto(proyecto: ProyectoIn):
    try:
        datos = proyecto.model_dump()
        valido, msg = validar_datos_proyecto(datos)
        if not valido:
            raise HTTPException(status_code=400, detail=msg)
        
        # Crear el proyecto sin ID (será generado automáticamente por la BD)
        proyecto_a_guardar = Proyecto(
            id_proyecto=None,  # Será generado automáticamente
            nombre=datos['nombre'],
            descripcion=datos['descripcion'],
            fecha_inicio=datos.get('fecha_inicio'),
            fecha_fin=datos.get('fecha_fin'),
            poblacion=datos.get('poblacion'),
            responsable=datos.get('responsable'),
            estado=datos['estado'],
            objetivos=datos.get('objetivos'),
            presupuesto=datos.get('presupuesto')
        )

        obj = gestor.agregar(proyecto_a_guardar)
        
        if obj is None:
            raise HTTPException(status_code=500, detail="El gestor no pudo guardar el proyecto, devolvió None.")
        return {"mensaje": "Proyecto guardado correctamente", "id_proyecto": obj.id_proyecto}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor al crear el proyecto: {e}")

@router.put("/api/proyectos/{id_proyecto}")
def actualizar_proyecto(id_proyecto: int, proyecto: ProyectoIn):
    try:
        datos = proyecto.model_dump()
        valido, msg = validar_datos_proyecto(datos)
        if not valido:
            raise HTTPException(status_code=400, detail=msg)
        
        proyecto_obj = Proyecto(
            id_proyecto=id_proyecto,
            nombre=datos['nombre'],
            descripcion=datos['descripcion'],
            fecha_inicio=datos.get('fecha_inicio'),
            fecha_fin=datos.get('fecha_fin'),
            poblacion=datos.get('poblacion'),
            responsable=datos.get('responsable'),
            estado=datos['estado'],
            objetivos=datos.get('objetivos'),
            presupuesto=datos.get('presupuesto')
        )
        
        if not gestor.actualizar(proyecto_obj):
            raise HTTPException(status_code=404, detail="Proyecto no encontrado o no se pudo actualizar")
        return {"mensaje": "Proyecto actualizado correctamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@router.delete("/api/proyectos/{id_proyecto}")
def eliminar_proyecto(id_proyecto: int):
    try:
        if not gestor.eliminar(id_proyecto):
            raise HTTPException(status_code=404, detail="Proyecto no encontrado o no se pudo eliminar")
        return {"mensaje": "Proyecto eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

