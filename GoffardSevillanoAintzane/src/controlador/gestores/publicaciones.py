from dominios.publicacion import Publicacion
from gestores.base_gestor import BaseGestor

class Publicaciones(BaseGestor):
    def mostrar_elemento(self, elemento):
        return str(elemento)
