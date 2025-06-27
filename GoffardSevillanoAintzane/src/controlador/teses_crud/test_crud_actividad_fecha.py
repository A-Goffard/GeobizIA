from src.controlador.gestores.crud.crud_actividad_fecha import (
    crear_actividad_fecha,
    leer_actividad_fecha,
    actualizar_actividad_fecha,
    eliminar_actividad_fecha
)

def test_crud_actividad_fecha():
    # Crear
    actividad_fecha = crear_actividad_fecha(
        actividad_id=1,  # Asegúrate de que este ID exista en tu DB
        fecha="2025-07-01"
    )
    print(f"ActividadFecha creada: {actividad_fecha}")
    if actividad_fecha is None:
        print("Error: No se pudo crear la actividad_fecha.")
        return

    # Leer
    leida = leer_actividad_fecha(actividad_fecha.id_actividad_fecha)
    print(f"Leída: {leida}")

    # Actualizar
    actualizada = actualizar_actividad_fecha(actividad_fecha.id_actividad_fecha, fecha="2025-07-02")
    print(f"Actualizada: {actualizada}")

    # Eliminar
    eliminado = eliminar_actividad_fecha(actividad_fecha.id_actividad_fecha)
    print(f"Eliminada: {eliminado}")

if __name__ == "__main__":
    test_crud_actividad_fecha()
