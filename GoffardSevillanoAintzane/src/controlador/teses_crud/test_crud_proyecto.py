from src.controlador.gestores.crud.crud_proyecto import crear_proyecto, leer_proyecto, actualizar_proyecto, eliminar_proyecto

def test_crud_proyecto():
    # Crear un proyecto
    proyecto = crear_proyecto(
        id_proyecto=1,
        nombre="Proyecto de Consultoría",
        descripcion="Consultoría para optimización de procesos",
        fecha_inicio="2025-07-01",
        fecha_fin="2025-12-31",
        poblacion="Madrid",
        responsable="Juan Pérez",
        estado="Activo",
        objetivos="Mejorar eficiencia operativa",
        presupuesto=50000.0
    )
    print(f"Proyecto creado: {proyecto}")
    if proyecto is None:
        print("Error: No se pudo crear el proyecto. Finalizando la prueba.")
        return

    # Leer el proyecto
    proyecto_leido = leer_proyecto(proyecto.id_proyecto)
    print(f"Proyecto leído: {proyecto_leido}")

    # Actualizar el proyecto
    actualizado = actualizar_proyecto(
        proyecto.id_proyecto,
        nombre="Proyecto de Consultoría Actualizado",
        descripcion="Consultoría para optimización avanzada",
        fecha_inicio="2025-07-01",
        fecha_fin="2026-01-15",
        poblacion="Barcelona",
        responsable="María López",
        estado="En Progreso",
        objetivos="Mejorar eficiencia operativa y reducir costos",
        presupuesto=60000.0
    )
    print(f"Proyecto actualizado: {actualizado}")
    proyecto_leido = leer_proyecto(proyecto.id_proyecto)
    print(f"Proyecto después de actualizar: {proyecto_leido}")

    # Eliminar el proyecto
    eliminado = eliminar_proyecto(proyecto.id_proyecto)
    print(f"Proyecto eliminado: {eliminado}")
    proyecto_leido = leer_proyecto(proyecto.id_proyecto)
    print(f"Proyecto después de eliminar: {proyecto_leido}")

if __name__ == "__main__":
    test_crud_proyecto()