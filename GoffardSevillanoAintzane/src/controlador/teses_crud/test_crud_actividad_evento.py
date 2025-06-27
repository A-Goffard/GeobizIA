from src.controlador.gestores.crud.crud_actividad_evento import (
    crear_actividad_evento,
    leer_actividad_evento,
    actualizar_actividad_evento,
    eliminar_actividad_evento
)

def test_crud_actividad_evento():
    # Crear
    ae = crear_actividad_evento(
        actividad_id=1,  # Asegúrate de que exista
        evento_id=1      # Asegúrate de que exista
    )
    print(f"ActividadEvento creada: {ae}")
    if ae is None:
        print("Error: No se pudo crear actividad_evento.")
        return

    # Leer
    leida = leer_actividad_evento(ae.id_actividad_evento)
    print(f"Leída: {leida}")

    # Actualizar
    actualizada = actualizar_actividad_evento(ae.id_actividad_evento, evento_id=2)
    print(f"Actualizada: {actualizada}")

    # Eliminar
    eliminada = eliminar_actividad_evento(ae.id_actividad_evento)
    print(f"Eliminada: {eliminada}")

if __name__ == "__main__":
    test_crud_actividad_evento()
