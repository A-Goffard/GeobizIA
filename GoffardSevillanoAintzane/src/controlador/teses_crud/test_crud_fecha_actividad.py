from src.controlador.gestores.crud.crud_fecha_actividad import crear_fecha_actividad, leer_fecha_actividad, actualizar_fecha_actividad, eliminar_fecha_actividad

def test_crud_fecha_actividad():
    # Crear una fecha_actividad
    fecha = crear_fecha_actividad(fecha="2025-12-31")
    print(f"Fecha creada: {fecha}")
    
    if fecha is None:
        print("Error: No se pudo crear la fecha_actividad. Finalizando la prueba.")
        return

    # Leer la fecha_actividad
    fecha_leida = leer_fecha_actividad(fecha.id_fecha)
    print(f"Fecha leída: {fecha_leida}")

    # Actualizar la fecha_actividad
    actualizado = actualizar_fecha_actividad(fecha.id_fecha, fecha="2026-01-01")
    print(f"Fecha actualizada: {actualizado}")
    fecha_leida = leer_fecha_actividad(fecha.id_fecha)
    print(f"Fecha después de actualizar: {fecha_leida}")

    # Eliminar la fecha_actividad
    eliminado = eliminar_fecha_actividad(fecha.id_fecha)
    print(f"Fecha eliminada: {eliminado}")
    fecha_leida = leer_fecha_actividad(fecha.id_fecha)
    print(f"Fecha después de eliminar: {fecha_leida}")

if __name__ == "__main__":
    test_crud_fecha_actividad()