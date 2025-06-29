import pytest
from src.controlador.gestores.documentos_tag import DocumentosTagGestor

@pytest.fixture
def gestor():
    return DocumentosTagGestor()

def test_agregar_y_buscar(gestor):
    # Crear relación
    id_documento = 1
    id_tag = 10

    agregado = gestor.agregar(id_documento, id_tag)
    assert agregado is not None, "No se pudo agregar relación documento-tag"

    # Buscar relación
    resultado = gestor.buscar(id_documento, id_tag)
    assert resultado is not None, "No se encontró relación documento-tag"
    assert resultado.id_documento == id_documento
    assert resultado.id_tag == id_tag

def test_eliminar(gestor):
    id_documento = 2
    id_tag = 20
    gestor.agregar(id_documento, id_tag)
    eliminado = gestor.eliminar(id_documento, id_tag)
    assert eliminado
    resultado = gestor.buscar(id_documento, id_tag)
    assert resultado is None
        id_tag2 = 21

        self.gestor.agregar(id_documento=id_documento, id_tag=id_tag1)
        self.gestor.agregar(id_documento=id_documento, id_tag=id_tag2)

        lista = self.gestor.listar(filtro={"id_documento": id_documento})
        self.assertGreaterEqual(len(lista), 2)
        for relacion in lista:
            self.assertEqual(relacion.id_documento, id_documento)

    def test_eliminar(self):
        id_documento = 3
        id_tag = 30

        self.gestor.agregar(id_documento=id_documento, id_tag=id_tag)
        eliminado = self.gestor.eliminar(id_documento, id_tag)
        self.assertTrue(eliminado, "No se pudo eliminar relación documento-tag")

        resultado = self.gestor.buscar((id_documento, id_tag))
        self.assertIsNone(resultado, "Relación documento-tag no fue eliminada")

if __name__ == "__main__":
    unittest.main()
