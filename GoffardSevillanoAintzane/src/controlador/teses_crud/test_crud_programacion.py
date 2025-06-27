from src.controlador.gestores.crud.crud_programacion import crear_programacion, leer_programacion, actualizar_programacion, eliminar_programacion

def test_crud_programacion():
    # Crear una programación
    programacion = crear_programacion(
        fecha="2025-07-10",
        hora_inicio="09:00",
        hora_fin="11:00",
        actividad="Limpieza de playa",
        responsable="María López",
        estado="Programado"
    )
    print(f"Programación creada: {programacion}")

    if programacion is None:
        print("Error: No se pudo crear la programación. Finalizando la prueba.")
        return

    # Leer programación
    programacion_leida = leer_programacion(programacion.id_programacion)
    print(f"Programación leída: {programacion_leida}")

    # Actualizar programación
    actualizar_programacion(
        programacion.id_programacion,
        hora_fin="11:30",
        estado="Reprogramado"
    )
    programacion_actualizada = leer_programacion(programacion.id_programacion)
    print(f"Programación actualizada: {programacion_actualizada}")

    # Eliminar programación
    eliminar_programacion(programacion.id_programacion)
    programacion_eliminada = leer_programacion(programacion.id_programacion)
    print(f"Programación después de eliminar: {programacion_eliminada}")

if __name__ == "__main__":
    test_crud_programacion()
