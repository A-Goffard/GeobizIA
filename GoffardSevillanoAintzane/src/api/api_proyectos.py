from fastapi import APIRouter, HTTPException
from src.controlador.gestores.proyectos import Proyectos

router = APIRouter()
gestor = Proyectos()

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

