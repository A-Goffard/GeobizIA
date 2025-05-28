from dominios.fisica import Fisica
from gestores.base_gestor import BaseGestor

class Fisicas(BaseGestor):
    def mostrar_elemento(self, elemento):
        return str(elemento)
