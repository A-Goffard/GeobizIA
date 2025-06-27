import unittest
from src.controlador.dominios.documento_tag import DocumentoTag
from src.controlador.gestores.documentos_tag import DocumentosTag

class TestDocumentosTag(unittest.TestCase):

    def setUp(self):
        self.gestor = DocumentosTag()
        # Limpiar datos previos (si existe método para ello)
        # Esto depende de tu implementación de BaseGestor, si no hay, considera hacerlo manualmente
        # por ejemplo: self.gestor.eliminar_todos()

    def test_agregar_y_buscar(self):
        # Crear relación
        id_documento = 1
        id_tag = 10

        agregado = self.gestor.agregar(id_documento=id_documento, id_tag=id_tag)
        self.assertTrue(agregado, "No se pudo agregar relación documento-tag")

        # Buscar relación
        resultado = self.gestor.buscar((id_documento, id_tag))
        self.assertIsNotNone(resultado, "No se encontró relación documento-tag")
        self.assertEqual(resultado.id_documento, id_documento)
        self.assertEqual(resultado.id_tag, id_tag)

    def test_listar_por_documento(self):
        id_documento = 2
        id_tag1 = 20
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
