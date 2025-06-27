from src.controlador.gestores.crud.crud_evento import crear_evento, leer_evento, actualizar_evento, eliminar_evento

def test_crud_evento():
    # Crear un evento
    evento = crear_evento(
        id_evento=1,
        nombre="Conferencia de Tecnología",
        tipo="Conferencia",
        lugar="Centro de Convenciones",
        fecha_comienzo="2025-07-01",
        fecha_final="2025-07-03",
        poblacion="Madrid",
        tematica="Innovación Tecnológica"
    )
    print(f"Evento creado: {evento}")
    if evento is None:
        print("Error: No se pudo crear el evento. Finalizando la prueba.")
        return

    # Leer el evento
    evento_leido = leer_evento(evento.id_evento)
    print(f"Evento leído: {evento_leido}")

    # Actualizar el evento
    actualizado = actualizar_evento(
        evento.id_evento,
        nombre="Conferencia de Tecnología Actualizada",
        tipo="Conferencia Internacional",
        lugar="Palacio de Congresos",
        fecha_comienzo="2025-07-02",
        fecha_final="2025-07-04",
        poblacion="Barcelona",
        tematica="Innovación Tecnológica Avanzada"
    )
    print(f"Evento actualizado: {actualizado}")
    evento_leido = leer_evento(evento.id_evento)
    print(f"Evento después de actualizar: {evento_leido}")

    # Eliminar el evento
    eliminado = eliminar_evento(evento.id_evento)
    print(f"Evento eliminado: {eliminado}")
    evento_leido = leer_evento(evento.id_evento)
    print(f"Evento después de eliminar: {evento_leido}")

if __name__ == "__main__":
    test_crud_evento()