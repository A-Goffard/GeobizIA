import unittest
from src.controlador.gestores.gestor_plantilla_tipo_publicacion import GestorPlantillaTipoPublicacion

class TestGestorPlantillaTipoPublicacion(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorPlantillaTipoPublicacion()
        # Considera limpiar la tabla para evitar conflictos si es posible
        # No implementado aquí porque depende de tu BaseGestor/BaseCRUD

    def test_agregar_y_buscar(self):
        id_plantilla = 1
        id_tipo_publicacion = 2

        agregado = self.gestor.agregar(id_plantilla, id_tipo_publicacion)
        self.assertTrue(agregado, "No se pudo agregar relación plantilla-tipo_publicacion")

        encontrado = self.gestor.buscar((id_plantilla, id_tipo_publicacion))
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.id_plantilla, id_plantilla)
        self.assertEqual(encontrado.id_tipo_publicacion, id_tipo_publicacion)

    def test_listar(self):
        id_plantilla = 3
        id_tipo_publicacion_1 = 4
        id_tipo_publicacion_2 = 5

        self.gestor.agregar(id_plantilla, id_tipo_publicacion_1)
        self.gestor.agregar(id_plantilla, id_tipo_publicacion_2)

        lista = self.gestor.listar({"id_plantilla": id_plantilla})
        self.assertGreaterEqual(len(lista), 2)
        for item in lista:
            self.assertEqual(item.id_plantilla, id_plantilla)

    def test_eliminar(self):
        id_plantilla = 6
        id_tipo_publicacion = 7

        self.gestor.agregar(id_plantilla, id_tipo_publicacion)
        eliminado = self.gestor.eliminar(id_plantilla, id_tipo_publicacion)
        self.assertTrue(eliminado)

        no_existe = self.gestor.buscar((id_plantilla, id_tipo_publicacion))
        self.assertIsNone(no_existe)

if __name__ == "__main__":
    unittest.main()
