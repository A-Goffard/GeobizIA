import pytest
from src.controlador.gestores.documentos import Documentos

@pytest.fixture
def gestor():
    return Documentos()

def test_crud_documento(gestor):
    # Crear un documento
    documento = gestor.agregar(
        id_documento=1,
        titulo="Informe Anual",
        descripcion="Informe anual de actividades 2025",
        fecha_subida="2025-06-27",
        tipo="Informe",
        tematica="Gestión Empresarial"
    )
    assert documento is not None

    # Leer el documento
    documento_leido = gestor.buscar(1)
    assert documento_leido.titulo == "Informe Anual"

    # Actualizar el documento
    actualizado = gestor.actualizar(1, titulo="Informe Anual Actualizado", tipo="Informe Técnico")
    assert actualizado
    assert gestor.buscar(1).titulo == "Informe Anual Actualizado"

    # Eliminar el documento
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None