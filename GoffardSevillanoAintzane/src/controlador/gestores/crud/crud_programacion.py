from src.controlador.gestores.programaciones import Programaciones

def crear_programacion(fecha, hora_inicio, hora_fin, actividad, responsable, estado):
    gestor = Programaciones()
    return gestor.agregar(
        fecha=fecha,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        actividad=actividad,
        responsable=responsable,
        estado=estado
    )

def leer_programacion(id_programacion):
    gestor = Programaciones()
    return gestor.buscar(id_programacion)

def actualizar_programacion(id_programacion, fecha=None, hora_inicio=None, hora_fin=None, actividad=None, responsable=None, estado=None):
    gestor = Programaciones()
    return gestor.actualizar(
        id_programacion,
        fecha=fecha,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        actividad=actividad,
        responsable=responsable,
        estado=estado
    )

def eliminar_programacion(id_programacion):
    gestor = Programaciones()
    return gestor.eliminar(id_programacion)
