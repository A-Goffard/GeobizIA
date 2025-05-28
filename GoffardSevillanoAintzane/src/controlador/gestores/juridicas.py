from dominios.juridica import Juridica
from gestores.base_gestor import BaseGestor

class Juridicas(BaseGestor):
    def mostrar_elemento(self, elemento):
        return str(elemento)
