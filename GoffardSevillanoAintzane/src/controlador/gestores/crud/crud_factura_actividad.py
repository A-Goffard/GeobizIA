from src.controlador.dominios.factura_actividad import FacturaActividad
from src.controlador.gestores.factura_actividades import FacturaActividades

def crear_factura_actividad(actividad_id, factura_id, monto, fecha):
    gestor = FacturaActividades()
    return gestor.agregar(actividad_id=actividad_id, factura_id=factura_id, monto=monto, fecha=fecha)

def leer_factura_actividad(id_factura_actividad):
    gestor = FacturaActividades()
    return gestor.buscar(id_factura_actividad)

def actualizar_factura_actividad(id_factura_actividad, **kwargs):
    gestor = FacturaActividades()
    return gestor.actualizar(id_factura_actividad, **kwargs)

def eliminar_factura_actividad(id_factura_actividad):
    gestor = FacturaActividades()
    return gestor.eliminar(id_factura_actividad)
