from src.controlador.gestores.crud.crud_proyecto_actividad import agregar_proyecto_actividad, eliminar_proyecto_actividad, buscar_proyecto_actividad, listar_actividades_por_proyecto

def test_crud_proyecto_actividad():
    # Agregar relación
    relacion = agregar_proyecto_actividad(1, 101)
    print(f"Relación agregada: {relacion}")
    if relacion is None:
        print("No se pudo agregar la relación. Finalizando test.")
        return

    # Buscar relación
    encontrada = buscar_proyecto_actividad(1, 101)
    print(f"Relación encontrada: {encontrada}")

    # Listar actividades por proyecto
    lista = listar_actividades_por_proyecto(1)
    print(f"Lista actividades para proyecto 1: {[str(r) for r in lista]}")

    # Eliminar relación
    eliminado = eliminar_proyecto_actividad(1, 101)
    print(f"Relación eliminada: {eliminado}")

    # Buscar después de eliminar
    encontrada = buscar_proyecto_actividad(1, 101)
    print(f"Relación después de eliminar: {encontrada}")

if __name__ == "__main__":
    test_crud_proyecto_actividad()
