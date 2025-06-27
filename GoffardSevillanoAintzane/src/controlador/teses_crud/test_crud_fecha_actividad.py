from src.controlador.gestores.crud.crud_fecha_actividad import crear_fecha_actividad, leer_fecha_actividad, actualizar_fecha_actividad, eliminar_fecha_actividad

def test_crud_fecha_actividad():
    # Crear una fecha_actividad
    fecha_actividad = crear_fecha_actividad(
        fecha="2025-07-01"
    )
    print(f"Fecha_Actividad creada: {fecha_actividad}")
    if fecha_actividad is None:
        print("Error: No se pudo crear la fecha_actividad. Finalizando la prueba.")
        return

    # Leer la fecha_actividad
    fecha_actividad_leida = leer_fecha_actividad(fecha_actividad.id_fecha)
    print(f"Fecha_Actividad leída: {fecha_actividad_leida}")

    # Actualizar la fecha_actividad
    actualizado = actualizar_fecha_actividad(
        fecha_actividad.id_fecha,
        fecha="2025-07-02"
    )
    print(f"Fecha_Actividad actualizada: {actualizado}")
    fecha_actividad_leida = leer_fecha_actividad(fecha_actividad.id_fecha)
    print(f"Fecha_Actividad después de actualizar: {fecha_actividad_leida}")

    # Eliminar la fecha_actividad
    eliminado = eliminar_fecha_actividad(fecha_actividad.id_fecha)
    print(f"Fecha_Actividad eliminada: {eliminado}")
    fecha_actividad_leida = leer_fecha_actividad(fecha_actividad.id_fecha)
    print(f"Fecha_Actividad después de eliminar: {fecha_actividad_leida}")

if __name__ == "__main__":
    test_crud_fecha_actividad()
    
    
    
    # cd "C:/Aintzane/Data Analisis/GeobizIA/GoffardSevillanoAintzane"
    # & C:/Users/Alumno/.virtualenvs/pipenv-0E7nQMdt/Scripts/python.exe -m src.controlador.teses_crud.test_crud_fecha_actividad