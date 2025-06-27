from src.controlador.dominios.actividad_evento import ActividadEvento
from src.controlador.gestores.actividad_eventos import ActividadEventos

def crear_actividad_evento(actividad_id, evento_id):
    gestor = ActividadEventos()
    return gestor.agregar(actividad_id=actividad_id, evento_id=evento_id)

def leer_actividad_evento(id_actividad_evento):
    gestor = ActividadEventos()
    return gestor.buscar(id_actividad_evento)

def actualizar_actividad_evento(id_actividad_evento, **kwargs):
    gestor = ActividadEventos()
    return gestor.actualizar(id_actividad_evento, **kwargs)

def eliminar_actividad_evento(id_actividad_evento):
    gestor = ActividadEventos()
    return gestor.eliminar(id_actividad_evento)
