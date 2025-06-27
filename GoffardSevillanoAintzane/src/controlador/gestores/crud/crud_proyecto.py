from src.controlador.gestores.proyectos_actividad import ProyectosActividad

def agregar_proyecto_actividad(proyecto_id, actividad_id):
    gestor = ProyectosActividad()
    return gestor.agregar(proyecto_id, actividad_id)

def eliminar_proyecto_actividad(proyecto_id, actividad_id):
    gestor = ProyectosActividad()
    return gestor.eliminar(proyecto_id, actividad_id)

def buscar_proyecto_actividad(proyecto_id, actividad_id):
    gestor = ProyectosActividad()
    return gestor.buscar(proyecto_id, actividad_id)

def listar_actividades_por_proyecto(proyecto_id):
    gestor = ProyectosActividad()
    return gestor.listar_por_proyecto(proyecto_id)
