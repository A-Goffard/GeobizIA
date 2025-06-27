from src.controlador.gestores.crud.crud_actividad import crear_actividad, leer_actividad, actualizar_actividad, eliminar_actividad

def test_crud_actividad():
    # Crear una actividad
    actividad = crear_actividad(
        id_actividad=1,
        tipo="Conferencia",
        nombre="Evento Anual",
        descripcion="Evento de tecnología",
        responsable="Juan Pérez",
        duracion="2 horas",
        coste_economico=1000.0,
        coste_horas=20.0,
        facturacion=1500.0,
        resultados="Éxito",
        valoracion="Positiva",
        observaciones="Ninguna"
    )
    print(f"Actividad creada: {actividad}")
    if actividad is None:
        print("Error: No se pudo crear la actividad. Finalizando la prueba.")
        return

    # Leer la actividad
    actividad_leida = leer_actividad(actividad.id_actividad)
    print(f"Actividad leída: {actividad_leida}")

    # Actualizar la actividad
    actualizado = actualizar_actividad(
        actividad.id_actividad,
        tipo="Taller",
        nombre="Taller de Innovación",
        descripcion="Taller práctico",
        responsable="María López",
        duracion="3 horas",
        coste_economico=1200.0,
        coste_horas=25.0,
        facturacion=1800.0,
        resultados="Muy exitoso",
        valoracion="Excelente",
        observaciones="Buena participación"
    )
    print(f"Actividad actualizada: {actualizado}")
    actividad_leida = leer_actividad(actividad.id_actividad)
    print(f"Actividad después de actualizar: {actividad_leida}")

    # Eliminar la actividad
    eliminado = eliminar_actividad(actividad.id_actividad)
    print(f"Actividad eliminada: {eliminado}")
    actividad_leida = leer_actividad(actividad.id_actividad)
    print(f"Actividad después de eliminar: {actividad_leida}")

if __name__ == "__main__":
    test_crud_actividad()