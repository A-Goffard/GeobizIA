from src.controlador.gestores.crud.crud_recurso_multimedia import (
    crear_recurso_multimedia,
    leer_recurso_multimedia,
    actualizar_recurso_multimedia,
    eliminar_recurso_multimedia
)

def test_crud_recurso_multimedia():
    # Crear
    recurso = crear_recurso_multimedia(
        tipo="Imagen",
        titulo="Foto del proyecto",
        fecha_subida="2025-06-27",
        autor="Equipo A"
    )
    print(f"Recurso creado: {recurso}")
    if recurso is None:
        print("Error: No se pudo crear el recurso.")
        return

    # Leer
    recurso_leido = leer_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso leído: {recurso_leido}")

    # Actualizar
    actualizado = actualizar_recurso_multimedia(recurso.id_recurso_multimedia, titulo="Foto oficial del proyecto")
    print(f"Recurso actualizado: {actualizado}")
    recurso_leido = leer_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso después de actualizar: {recurso_leido}")

    # Eliminar
    eliminado = eliminar_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso eliminado: {eliminado}")
    recurso_leido = leer_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso después de eliminar: {recurso_leido}")

if __name__ == "__main__":
    test_crud_recurso_multimedia()
