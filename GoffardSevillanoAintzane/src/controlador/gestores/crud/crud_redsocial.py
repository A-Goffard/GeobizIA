from src.controlador.dominios.redsocial import RedSocial
from src.controlador.gestores.redes_sociales import RedesSociales

def crear_redsocial(plataforma, nombre_cuenta, credenciales=None, preferencias_publicacion=None, estado_conexion=None, ultima_publicacion=None):
    gestor = RedesSociales()
    return gestor.agregar(
        plataforma=plataforma,
        nombre_cuenta=nombre_cuenta,
        credenciales=credenciales,
        preferencias_publicacion=preferencias_publicacion,
        estado_conexion=estado_conexion,
        ultima_publicacion=ultima_publicacion
    )

def leer_redsocial(id_red_social):
    gestor = RedesSociales()
    return gestor.buscar(id_red_social)

def actualizar_redsocial(id_red_social, plataforma=None, nombre_cuenta=None, credenciales=None, preferencias_publicacion=None, estado_conexion=None, ultima_publicacion=None):
    gestor = RedesSociales()
    return gestor.actualizar(
        id_red_social,
        plataforma=plataforma,
        nombre_cuenta=nombre_cuenta,
        credenciales=credenciales,
        preferencias_publicacion=preferencias_publicacion,
        estado_conexion=estado_conexion,
        ultima_publicacion=ultima_publicacion
    )

def eliminar_redsocial(id_red_social):
    gestor = RedesSociales()
    return gestor.eliminar(id_red_social)
