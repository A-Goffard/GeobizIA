
from dominios.persona import Persona
from dominios.usuario import Usuario
from gestores.personas import PersonaFactory


class UsuarioFactory(PersonaFactory):
    def crear_persona(self, datos) -> Persona:
        return Usuario(
            id=datos["id"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            email=datos["email"],
            telefono=datos["telefono"],
            dni=datos["dni"],
            direccion=datos["direccion"],
            cp=datos["cp"],
            poblacion=datos["poblacion"],
            pais=datos["pais"],
            fecha_nacimiento=datos["fecha_nacimiento"],
            preferencias=datos["preferencias"],
            rol=datos["rol"],
            password=datos["password"]
        )