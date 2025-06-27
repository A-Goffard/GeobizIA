from src.controlador.gestores.crud.crud_factura_actividad import (
    crear_factura_actividad,
    leer_factura_actividad,
    actualizar_factura_actividad,
    eliminar_factura_actividad
)

def test_crud_factura_actividad():
    # Crear (asegúrate de que actividad_id y factura_id existan)
    fa = crear_factura_actividad(
        actividad_id=1,
        factura_id=1,
        monto=1500.00,
        fecha="2025-06-27"
    )
    print(f"FacturaActividad creada: {fa}")
    if fa is None:
        print("Error: No se pudo crear factura_actividad.")
        return

    # Leer
    leida = leer_factura_actividad(fa.id_factura_actividad)
    print(f"Leída: {leida}")

    # Actualizar
    actualizada = actualizar_factura_actividad(fa.id_factura_actividad, monto=2000.00)
    print(f"Actualizada: {actualizada}")

    # Eliminar
    eliminada = eliminar_factura_actividad(fa.id_factura_actividad)
    print(f"Eliminada: {eliminada}")

if __name__ == "__main__":
    test_crud_factura_actividad()
