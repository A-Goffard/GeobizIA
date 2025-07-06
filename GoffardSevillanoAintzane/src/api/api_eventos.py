from fastapi import APIRouter, HTTPException
from src.controlador.gestores.eventos import Eventos

router = APIRouter()
gestor = Eventos()

@router.get("/api/eventos")
def listar_eventos():
    try:
        eventos = gestor.mostrar_todos_los_elem()
        # Verifica que cada evento tenga el método to_dict
        return [e.to_dict() for e in eventos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener eventos: {e}")

@router.get("/api/eventos/{id_evento}")
def obtener_evento(id_evento: int):
    try:
        obj = gestor.buscar(id_evento)
        if obj is None:
            raise HTTPException(status_code=404, detail="No encontrado")
        return obj.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener evento: {e}")
