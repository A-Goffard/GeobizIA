from src.controlador.gestores.actividades_fecha import ActividadesFecha
from src.controlador.crud.crud_actividad import crear_actividad
from src.controlador.crud.crud_fecha_actividad import crear_fecha_actividad

def test_actividad_fecha():
    # Crear una actividad
    actividad = crear_actividad(tipo="Conferencia", nombre="Evento Anual", descripcion="Evento de tecnología", responsable="Juan Pérez", duracion="2 horas", coste_economico=1000.0, coste_horas=20.0, facturacion=1500.0, resultados="Éxito", valoracion="Positiva", observaciones="Ninguna")
    print(f"Actividad creada: {actividad}")
    if actividad is None:
        print("Error: No se pudo crear la actividad. Finalizando la prueba.")
        return

    # Crear una fecha_actividad
    fecha = crear_fecha_actividad(fecha="2025-12-31")
    print(f"Fecha creada: {fecha}")
    if fecha is None:
        print("Error: No se pudo crear la fecha_actividad. Finalizando la prueba.")
        return

    # Crear una relación actividad_fecha
    gestor = ActividadesFecha()
    actividad_fecha = gestor.agregar(id_actividad=actividad.id_actividad, id_fecha=fecha.id_fecha)
    print(f"Relación actividad_fecha creada: {actividad_fecha}")

    # Buscar la relación
    actividad_fecha_leida = gestor.buscar(actividad.id_actividad, fecha.id_fecha)
    print(f"Relación actividad_fecha leída: {actividad_fecha_leida}")

    # Eliminar la relación
    eliminado = gestor.eliminar(actividad.id_actividad, fecha.id_fecha)
    print(f"Relación actividad_fecha eliminada: {eliminado}")
    actividad_fecha_leida = gestor.buscar(actividad.id_actividad, fecha.id_fecha)
    print(f"Relación actividad_fecha después de eliminar: {actividad_fecha_leida}")

    # Limpiar datos creados
    from src.controlador.crud.crud_actividad import eliminar_actividad
    from src.controlador.crud.crud_fecha_actividad import eliminar_fecha_actividad
    eliminar_actividad(actividad.id_actividad)
    eliminar_fecha_actividad(fecha.id_fecha)

if __name__ == "__main__":
    test_actividad_fecha()