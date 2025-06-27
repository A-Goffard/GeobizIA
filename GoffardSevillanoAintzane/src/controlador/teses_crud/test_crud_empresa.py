from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_empresa import crear_empresa, leer_empresa, actualizar_empresa, eliminar_empresa

def test_crud_empresa():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Carlos",
        apellido="Martínez",
        email="carlos.martinez@example.com",
        telefono="912345678",
        dni="12345678C",
        direccion="Calle Real 789",
        cp="28003",
        poblacion="Valencia",
        pais="España"
    )
    print(f"Persona creada: {persona}")
    if persona is None:
        print("Error: No se pudo crear la persona. Finalizando la prueba.")
        return

    # Crear una empresa
    empresa = crear_empresa(
        id_empresa=1,
        id_persona=persona.id_persona,
        razon_social="Innovatech S.A.",
        nif="A12345678",
        sector="Tecnología",
        tamano="Mediana",
        fecha_registro="2025-06-27"
    )
    print(f"Empresa creada: {empresa}")
    if empresa is None:
        print("Error: No se pudo crear la empresa. Finalizando la prueba.")
        return

    # Leer la empresa
    empresa_leida = leer_empresa(empresa.id_empresa)
    print(f"Empresa leída: {empresa_leida}")

    # Actualizar la empresa
    actualizado = actualizar_empresa(
        empresa.id_empresa,
        razon_social="Innovatech Solutions S.A.",
        nif="B87654321",
        sector="Innovación",
        tamano="Grande",
        fecha_registro="2025-06-28"
    )
    print(f"Empresa actualizada: {actualizado}")
    empresa_leida = leer_empresa(empresa.id_empresa)
    print(f"Empresa después de actualizar: {empresa_leida}")

    # Eliminar la empresa
    eliminado = eliminar_empresa(empresa.id_empresa)
    print(f"Empresa eliminada: {eliminado}")
    empresa_leida = leer_empresa(empresa.id_empresa)
    print(f"Empresa después de eliminar: {empresa_leida}")

    # Limpiar la persona creada
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_empresa()