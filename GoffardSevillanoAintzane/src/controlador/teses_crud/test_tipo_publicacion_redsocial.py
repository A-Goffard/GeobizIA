import unittest
from src.controlador.gestores.gestor_tipo_publicacion_redsocial import GestorTipoPublicacionRedSocial

class TestGestorTipoPublicacionRedSocial(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTipoPublicacionRedSocial()
        # Aquí podrías limpiar la tabla antes de pruebas si tienes método para ello

    def test_agregar_y_buscar(self):
        id_tipo_publicacion = 1
        id_red_social = 2

        agregado = self.gestor.agregar(id_tipo_publicacion, id_red_social)
        self.assertTrue(agregado, "No se pudo agregar relación tipo_publicacion-redsocial")

        encontrado = self.gestor.buscar((id_tipo_publicacion, id_red_social))
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.id_tipo_publicacion, id_tipo_publicacion)
        self.assertEqual(encontrado.id_red_social, id_red_social)

    def test_listar(self):
        id_tipo_publicacion = 3
        id_red_social_1 = 4
        id_red_social_2 = 5

        self.gestor.agregar(id_tipo_publicacion, id_red_social_1)
        self.gestor.agregar(id_tipo_publicacion, id_red_social_2)

        lista = self.gestor.listar({"id_tipo_publicacion": id_tipo_publicacion})
        self.assertGreaterEqual(len(lista), 2)
        for item in lista:
            self.assertEqual(item.id_tipo_publicacion, id_tipo_publicacion)

    def test_eliminar(self):
        id_tipo_publicacion = 6
        id_red_social = 7

        self.gestor.agregar(id_tipo_publicacion, id_red_social)
        eliminado = self.gestor.eliminar(id_tipo_publicacion, id_red_social)
        self.assertTrue(eliminado)

        no_existe = self.gestor.buscar((id_tipo_publicacion, id_red_social))
        self.assertIsNone(no_existe)

if __name__ == "__main__":
    unittest.main()
