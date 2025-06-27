from src.controlador.gestores.crud.crud_documento import crear_documento, leer_documento, actualizar_documento, eliminar_documento

def test_crud_documento():
    # Crear un documento
    documento = crear_documento(
        id_documento=1,
        titulo="Informe Anual",
        descripcion="Informe anual de actividades 2025",
        fecha_subida="2025-06-27",
        tipo="Informe",
        tematica="Gestión Empresarial"
    )
    print(f"Documento creado: {documento}")
    if documento is None:
        print("Error: No se pudo crear el documento. Finalizando la prueba.")
        return

    # Leer el documento
    documento_leido = leer_documento(documento.id_documento)
    print(f"Documento leído: {documento_leido}")

    # Actualizar el documento
    actualizado = actualizar_documento(
        documento.id_documento,
        titulo="Informe Anual Actualizado",
        descripcion="Informe anual de actividades 2025 actualizado",
        fecha_subida="2025-06-28",
        tipo="Informe Técnico",
        tematica="Gestión Empresarial Avanzada"
    )
    print(f"Documento actualizado: {actualizado}")
    documento_leido = leer_documento(documento.id_documento)
    print(f"Documento después de actualizar: {documento_leido}")

    # Eliminar el documento
    eliminado = eliminar_documento(documento.id_documento)
    print(f"Documento eliminado: {eliminado}")
    documento_leido = leer_documento(documento.id_documento)
    print(f"Documento después de eliminar: {documento_leido}")

if __name__ == "__main__":
    test_crud_documento()