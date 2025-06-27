from src.controlador.dominios.actividad_fecha import ActividadFecha
from src.controlador.gestores.actividades_fecha import ActividadesFecha

def crear_actividad_fecha(actividad_id, fecha):
    gestor = ActividadesFecha()
    return gestor.agregar(actividad_id=actividad_id, fecha=fecha)

def leer_actividad_fecha(id_actividad_fecha):
    gestor = ActividadesFecha()
    return gestor.buscar(id_actividad_fecha)

def actualizar_actividad_fecha(id_actividad_fecha, **kwargs):
    gestor = ActividadesFecha()
    return gestor.actualizar(id_actividad_fecha, **kwargs)

def eliminar_actividad_fecha(id_actividad_fecha):
    gestor = ActividadesFecha()
    return gestor.eliminar(id_actividad_fecha)
