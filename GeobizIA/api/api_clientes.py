from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from GeobizIA.controlador.dominios.cliente import Cliente
from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.validaciones.validar_cliente import validar_datos_cliente

router = APIRouter()
gestor_clientes = Clientes()
gestor_personas = Personas()

class ClienteIn(BaseModel):
    # Datos de la persona
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    dni: Optional[str] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    pais: Optional[str] = None
    
    # Datos específicos del cliente
    tipo: Optional[str] = None
    razon_social: Optional[str] = None  
    nif: Optional[str] = None
    fecha_registro: Optional[str] = None

@router.get("/api/clientes")
def listar_clientes():
    try:
        clientes = gestor_clientes.mostrar_todos_los_elem()
        return [c.to_dict() for c in clientes]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener clientes: {e}")

@router.get("/api/clientes/{id_cliente}")
def obtener_cliente(id_cliente: int):
    try:
        obj = gestor_clientes.buscar(id_cliente)
        if obj is None:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        return obj.to_dict()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener cliente: {e}")

@router.post("/api/clientes")
def crear_cliente(cliente: ClienteIn):
    try:
        datos = cliente.model_dump()
        
        # Primero crear la persona
        persona_nueva = Persona(
            id_persona=None,  # Se generará automáticamente
            nombre=datos.get('nombre'),
            apellido=datos.get('apellido'),
            email=datos.get('email'),
            telefono=datos.get('telefono'),
            dni=datos.get('dni'),
            direccion=datos.get('direccion'),
            cp=datos.get('cp'),
            poblacion=datos.get('poblacion'),
            pais=datos.get('pais')
        )
        
        persona_creada = gestor_personas.agregar(persona_nueva)
        if persona_creada is None:
            raise HTTPException(status_code=500, detail="No se pudo crear la persona asociada al cliente")
        
        # Luego crear el cliente con el ID de la persona creada
        cliente_nuevo = Cliente(
            id_cliente=None,  # Se generará automáticamente
            id_persona=persona_creada.id_persona,
            tipo=datos.get('tipo'),
            razon_social=datos.get('razon_social'),
            nif=datos.get('nif'),
            fecha_registro=datos.get('fecha_registro')
        )

        cliente_creado = gestor_clientes.agregar(cliente_nuevo)
        if cliente_creado is None:
            raise HTTPException(status_code=500, detail="No se pudo crear el cliente")
            
        return {"mensaje": "Cliente creado correctamente", "id_cliente": cliente_creado.id_cliente, "id_persona": persona_creada.id_persona}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor al crear el cliente: {e}")

@router.put("/api/clientes/{id_cliente}")
def actualizar_cliente(id_cliente: int, cliente: ClienteIn):
    try:
        datos = cliente.model_dump()
        
        # Primero obtener el cliente actual para obtener su id_persona
        cliente_actual = gestor_clientes.buscar(id_cliente)
        if cliente_actual is None:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        
        # Actualizar los datos de la persona asociada
        if cliente_actual.id_persona:
            persona_actualizada = Persona(
                id_persona=cliente_actual.id_persona,
                nombre=datos.get('nombre'),
                apellido=datos.get('apellido'),
                email=datos.get('email'),
                telefono=datos.get('telefono'),
                dni=datos.get('dni'),
                direccion=datos.get('direccion'),
                cp=datos.get('cp'),
                poblacion=datos.get('poblacion'),
                pais=datos.get('pais')
            )
            
            if not gestor_personas.actualizar(persona_actualizada):
                raise HTTPException(status_code=500, detail="No se pudo actualizar la persona asociada")
        
        # Actualizar los datos del cliente
        cliente_actualizado = Cliente(
            id_cliente=id_cliente,
            id_persona=cliente_actual.id_persona,
            tipo=datos.get('tipo'),
            razon_social=datos.get('razon_social'),
            nif=datos.get('nif'),
            fecha_registro=datos.get('fecha_registro')
        )
        
        if not gestor_clientes.actualizar(cliente_actualizado):
            raise HTTPException(status_code=500, detail="No se pudo actualizar el cliente")
        
        return {"mensaje": "Cliente actualizado correctamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@router.delete("/api/clientes/{id_cliente}")
def eliminar_cliente(id_cliente: int):
    try:
        # Primero obtener el cliente para obtener su id_persona
        cliente_actual = gestor_clientes.buscar(id_cliente)
        if cliente_actual is None:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        
        # Eliminar el cliente
        if not gestor_clientes.eliminar(id_cliente):
            raise HTTPException(status_code=500, detail="No se pudo eliminar el cliente")
        
        # Eliminar la persona asociada si existe
        if cliente_actual.id_persona:
            gestor_personas.eliminar(cliente_actual.id_persona)
        
        return {"mensaje": "Cliente eliminado correctamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")
