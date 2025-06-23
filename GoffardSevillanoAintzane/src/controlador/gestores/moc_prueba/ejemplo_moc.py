from ...dominios.usuario import Usuario
from ...dominios.proyecto import Proyecto
from ...dominios.tema_ambiental import TemaAmbiental
from ...dominios.rol import Rol  # Make sure 'rol.py' exists in 'src/dominios' and contains the 'Rol' class

# Usuarios: primero los cargados (válidos), luego los no cargados (erróneos)
usuarios_cargados = [
    Usuario.crear_usuario(1, "Ana", "García", "ana@mail.com", "123456789", "1990-01-01", "Calle Falsa 123", "12345678A", "28080", "Madrid", "España", "admin", "ninguna", "pass123"),
    Usuario.crear_usuario(4, "Carlos", "López", "carlos.lopez@mail.com", "654321987", "1988-03-15", "Calle Sol 45", "23456789B", "29010", "Málaga", "España", "user", "cine", "pass321"),
    Usuario.crear_usuario(5, "María", "Ruiz", "maria.ruiz@mail.com", "789456123", "1992-07-20", "Avenida Paz 10", "34567890C", "33001", "Oviedo", "España", "user", "lectura", "pass654"),
]
usuarios_no_cargados = [
    Usuario.crear_usuario(2, "", "Pérez", "perez@mail.com", "987654321", "1985-05-05", "Avenida Real 45", "87654321B", "08080", "Barcelona", "España", "user", "deportes", "pass456"),  # nombre vacío
    Usuario.crear_usuario(3, "Luis", "Martín", "", "111222333", "1995-12-12", "Calle Luna 7", "11223344C", "41010", "Sevilla", "España", "user", "música", "pass789"),  # email vacío
]

proyectos_cargados = [
    Proyecto(1, "Proyecto Verde", "Reforestación urbana", "2023-01-01", "2023-12-31", "Madrid", "Ana", "activo", "plantar árboles", 10000),
    Proyecto(4, "Proyecto Solar", "Instalación de paneles solares", "2023-04-01", "2023-09-30", "Sevilla", "Carlos", "activo", "energía renovable", 20000),
    Proyecto(5, "Proyecto Agua", "Mejora de redes de agua", "2023-05-15", "2023-11-15", "Valencia", "María", "pendiente", "optimizar consumo", 15000),
]
proyectos_no_cargados = [
    Proyecto(2, "", "Sin nombre", "2023-02-01", "2023-11-30", "Valencia", "Luis", "pendiente", "limpieza playas", 5000),  # nombre vacío
    Proyecto(3, "Proyecto Azul", "", "2023-03-01", "2023-10-31", "Bilbao", "Marta", "finalizado", "", 0),  # descripción y objetivos vacíos
]

temas_ambientales_cargados = [
    TemaAmbiental.crear_tema_ambiental(1, "Cambio climático", "Impacto global", 10, ["actividad1"], ["pub1"]),
    TemaAmbiental.crear_tema_ambiental(4, "Biodiversidad", "Protección de especies", 8, ["actividad2"], ["pub2"]),
    TemaAmbiental.crear_tema_ambiental(5, "Reciclaje", "Gestión de residuos", 7, ["actividad3"], ["pub3"]),
]
temas_ambientales_no_cargados = [
    TemaAmbiental.crear_tema_ambiental(2, "", "Sin nombre", 5, [], []),  # nombre vacío
    TemaAmbiental.crear_tema_ambiental(3, "Contaminación", "", 0, [], []),  # descripción vacía
]

roles_cargados = [
    Rol.crear_rol("admin", ["crear", "editar", "eliminar"]),
    Rol.crear_rol("editor", ["crear", "editar"]),
    Rol.crear_rol("lector", ["ver"]),
]
roles_no_cargados = [
    Rol.crear_rol("", ["ver"]),  # nombre vacío
    Rol.crear_rol("usuario", []),  # tareas_permitidas vacío
]
roles_no_cargados = [
    Rol.crear_rol("", ["ver"]),  # nombre vacío
    Rol.crear_rol("usuario", []),  # tareas_permitidas vacío
]

