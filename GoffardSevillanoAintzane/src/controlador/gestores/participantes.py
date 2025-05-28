from dominios.participante import Participante
from dominios.persona import Persona
from gestores.personas import PersonaFactory


class ParticipanteFactory(PersonaFactory):
    def crear_persona(self, datos) -> Persona:
        return Participante(
            id=datos["id"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            email=datos["email"],
            telefono=datos["telefono"],
            numero_personas_juntas=datos["numero_personas_juntas"],
            como_conocer=datos["como_conocer"],
            actividad_id=datos["actividad_id"],
            fecha_registro=datos["fecha_registro"]
        )