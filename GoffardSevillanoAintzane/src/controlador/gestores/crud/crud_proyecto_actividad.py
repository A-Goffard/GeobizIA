from src.controlador.dominios.proyecto_actividad import ProyectoActividad
from src.controlador.gestores.proyectos_actividad import ProyectosActividad

def crear_proyecto_actividad(proyecto_id, actividad_id):
    gestor = ProyectosActividad()
    return gestor.agregar(proyecto_id=proyecto_id, actividad_id=actividad_id)

def leer_proyecto_actividad(id_proyecto_actividad):
    gestor = ProyectosActividad()
    return gestor.buscar(id_proyecto_actividad)

def actualizar_proyecto_actividad(id_proyecto_actividad, **kwargs):
    gestor = ProyectosActividad()
    return gestor.actualizar(id_proyecto_actividad, **kwargs)

def eliminar_proyecto_actividad(id_proyecto_actividad):
    gestor = ProyectosActividad()
    return gestor.eliminar(id_proyecto_actividad)
