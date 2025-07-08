import sys
import os

# Añadir la ruta raíz del proyecto para poder importar los módulos
# Esto es necesario para que el script se pueda ejecutar directamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from GeobizIA.controlador.gestores.personas import Personas
from GeobizIA.controlador.gestores.usuarios import Usuarios
from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.controlador.dominios.usuario import Usuario

def crear_usuario_principal():
    """
    Crea una persona y un usuario principal para el login si no existen.
    """
    print("Iniciando la creación del usuario principal...")

    # --- Datos del usuario a crear ---
    EMAIL_USUARIO = "usuario@gmail.com"
    PASSWORD_USUARIO = "123"
    NOMBRE = "Usuario"
    APELLIDO = "Principal"
    ROL = "Administrador"

    # --- Instancias de los gestores ---
    gestor_personas = Personas()
    gestor_usuarios = Usuarios()

    # 1. Verificar si el usuario ya existe por su email
    usuario_existente = gestor_usuarios.buscar_por_email(EMAIL_USUARIO)
    if usuario_existente:
        print(f"El usuario con email '{EMAIL_USUARIO}' ya existe. No se realizarán cambios.")
        # Opcional: podrías añadir lógica para actualizar la contraseña si se desea
        return

    print(f"El usuario con email '{EMAIL_USUARIO}' no existe. Procediendo a crearlo.")

    # 2. Crear el objeto Persona (sin ID, ya que es autoincremental)
    # --- AJUSTE: Añadimos datos de relleno para todos los campos ---
    nueva_persona = Persona(
        id_persona=None, # El ID será asignado por la base de datos
        nombre=NOMBRE,
        apellido=APELLIDO,
        email=EMAIL_USUARIO,
        telefono="600000000",
        dni="00000000X",
        direccion="Calle Falsa 123",
        cp="00000",
        poblacion="Ciudad Ejemplo",
        pais="País Ejemplo"
    )

    # 3. Guardar la persona en la base de datos
    persona_guardada = gestor_personas.agregar(nueva_persona)
    if not persona_guardada or not persona_guardada.id_persona:
        print("Error: No se pudo crear la entrada en la tabla 'persona'. Abortando.")
        return

    print(f"Persona creada con éxito. ID de Persona: {persona_guardada.id_persona}")

    # 4. Crear el objeto Usuario
    # El ID de usuario también es autoincremental, por lo que se pasa como None.
    nuevo_usuario = Usuario(
        id_usuario=None,
        id_persona=persona_guardada.id_persona,
        rol=ROL,
        password=PASSWORD_USUARIO # Se pasa la contraseña en texto plano
    )

    # Se hashea la contraseña explícitamente antes de guardarla.
    nuevo_usuario.set_password(PASSWORD_USUARIO)

    # 5. Guardar el usuario en la base de datos
    usuario_guardado = gestor_usuarios.agregar(nuevo_usuario)
    if not usuario_guardado:
        print("Error: No se pudo crear la entrada en la tabla 'usuario'.")
        # Considera eliminar la persona creada si el usuario falla
        # gestor_personas.eliminar(persona_guardada.id_persona)
        return

    print("¡Usuario principal creado con éxito!")
    print(f"  Email: {EMAIL_USUARIO}")
    print(f"  Contraseña: {PASSWORD_USUARIO}")
    print("Ya puedes iniciar sesión con estas credenciales.")


if __name__ == "__main__":
    crear_usuario_principal()
