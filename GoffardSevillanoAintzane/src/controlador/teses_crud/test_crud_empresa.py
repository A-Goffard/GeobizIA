import pytest
from src.controlador.gestores.empresas import Empresas

@pytest.fixture
def gestor():
    return Empresas()

def test_crud_empresa(gestor):
    empresa = gestor.agregar(
        id_empresa=1,
        nombre="Innovatech S.A.",
        sector="Tecnología",
        logo="logo.png",
        ubicacion="Valencia"
    )
    assert empresa is not None

    empresa_leida = gestor.buscar(1)
    assert empresa_leida.nombre == "Innovatech S.A."

    actualizado = gestor.actualizar(1, nombre="Innovatech Solutions S.A.", sector="Innovación")
    assert actualizado
    assert gestor.buscar(1).nombre == "Innovatech Solutions S.A."
    assert gestor.buscar(1).sector == "Innovación"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None