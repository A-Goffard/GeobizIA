from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from GeobizIA.controlador.dominios.evento import Evento
from GeobizIA.controlador.gestores.eventos import Eventos
from GeobizIA.validaciones.validar_evento import validar_datos_evento

router = APIRouter()
gestor = Eventos()

class EventoIn(BaseModel):
    nombre: str
    tipo: str
    lugar: str
    fecha_comienzo: str
    fecha_final: str
    poblacion: str
    tematica: str

@router.get("/api/eventos")
def listar_eventos():
    try:
        eventos = gestor.mostrar_todos_los_elem()
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

@router.post("/api/eventos")
def crear_evento(evento: EventoIn):
    try:
        datos = evento.model_dump()
        valido, msg = validar_datos_evento(datos)
        if not valido:
            raise HTTPException(status_code=400, detail=msg)
        
        evento_a_guardar = Evento(
            nombre=datos['nombre'],
            tipo=datos['tipo'],
            lugar=datos['lugar'],
            fecha_comienzo=datos['fecha_comienzo'],
            fecha_final=datos['fecha_final'],
            poblacion=datos['poblacion'],
            tematica=datos['tematica']
        )

        obj = gestor.agregar(evento_a_guardar)
        
        if obj is None:
            raise HTTPException(status_code=500, detail="El gestor no pudo guardar el evento, devolvió None.")
        return {"mensaje": "Evento guardado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor al crear el evento: {e}")
