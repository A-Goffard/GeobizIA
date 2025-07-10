from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from GeobizIA.controlador.gestores.empresas import Empresas
from GeobizIA.controlador.dominios.empresa import Empresa
from GeobizIA.validaciones.validar_empresa import validar_datos_empresa

router = APIRouter()

class EmpresaCreate(BaseModel):
    nombre: str
    sector: str
    logo: Optional[str] = None
    ubicacion: str

class EmpresaUpdate(BaseModel):
    nombre: Optional[str] = None
    sector: Optional[str] = None
    logo: Optional[str] = None
    ubicacion: Optional[str] = None

class EmpresaResponse(BaseModel):
    id_empresa: int
    nombre: str
    sector: str
    logo: Optional[str]
    ubicacion: str

    class Config:
        from_attributes = True

# Inicializar el gestor
gestor_empresas = Empresas()

@router.post("/api/empresas", response_model=dict, status_code=status.HTTP_201_CREATED)
async def crear_empresa(empresa_data: EmpresaCreate):
    """
    Crear una nueva empresa
    """
    try:
        # Convertir datos a diccionario para validación
        datos_empresa = empresa_data.model_dump()
        
        # Validar datos usando la capa de validaciones
        es_valido, mensaje = validar_datos_empresa(datos_empresa)
        if not es_valido:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error de validación: {mensaje}"
            )
        
        # Crear objeto Empresa
        empresa = Empresa(
            id_empresa=None,
            nombre=datos_empresa['nombre'],
            sector=datos_empresa['sector'],
            logo=datos_empresa.get('logo'),
            ubicacion=datos_empresa['ubicacion']
        )
        
        # Agregar empresa a la base de datos
        resultado = gestor_empresas.agregar(empresa)
        
        if resultado:
            return {
                "mensaje": "Empresa creada exitosamente",
                "id_empresa": resultado.id_empresa,
                "empresa": {
                    "id_empresa": resultado.id_empresa,
                    "nombre": resultado.nombre,
                    "sector": resultado.sector,
                    "logo": resultado.logo,
                    "ubicacion": resultado.ubicacion
                }
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No se pudo crear la empresa"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )

@router.get("/api/empresas", response_model=List[dict])
async def listar_empresas():
    """
    Obtener todas las empresas
    """
    try:
        empresas = gestor_empresas.mostrar_todos_los_elem()
        return [
            {
                "id_empresa": empresa.id_empresa,
                "nombre": empresa.nombre,
                "sector": empresa.sector,
                "logo": empresa.logo,
                "ubicacion": empresa.ubicacion
            }
            for empresa in empresas
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener las empresas: {str(e)}"
        )

@router.get("/api/empresas/{id_empresa}", response_model=dict)
async def obtener_empresa(id_empresa: int):
    """
    Obtener una empresa específica por ID
    """
    try:
        empresa = gestor_empresas.buscar(id_empresa)
        if empresa:
            return {
                "id_empresa": empresa.id_empresa,
                "nombre": empresa.nombre,
                "sector": empresa.sector,
                "logo": empresa.logo,
                "ubicacion": empresa.ubicacion
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empresa no encontrada"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener la empresa: {str(e)}"
        )

@router.put("/api/empresas/{id_empresa}", response_model=dict)
async def actualizar_empresa(id_empresa: int, empresa_data: EmpresaUpdate):
    """
    Actualizar una empresa existente
    """
    try:
        # Verificar si la empresa existe
        empresa_existente = gestor_empresas.buscar(id_empresa)
        if not empresa_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empresa no encontrada"
            )
        
        # Preparar datos para actualización (solo campos proporcionados)
        datos_actualizacion = {}
        if empresa_data.nombre is not None:
            datos_actualizacion['nombre'] = empresa_data.nombre
        if empresa_data.sector is not None:
            datos_actualizacion['sector'] = empresa_data.sector
        if empresa_data.logo is not None:
            datos_actualizacion['logo'] = empresa_data.logo
        if empresa_data.ubicacion is not None:
            datos_actualizacion['ubicacion'] = empresa_data.ubicacion
        
        # Validar datos (combinar existentes con nuevos)
        datos_para_validar = {
            'nombre': datos_actualizacion.get('nombre', empresa_existente.nombre),
            'sector': datos_actualizacion.get('sector', empresa_existente.sector),
            'logo': datos_actualizacion.get('logo', empresa_existente.logo),
            'ubicacion': datos_actualizacion.get('ubicacion', empresa_existente.ubicacion)
        }
        
        es_valido, mensaje = validar_datos_empresa(datos_para_validar)
        if not es_valido:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error de validación: {mensaje}"
            )
        
        # Crear empresa actualizada
        empresa_actualizada = Empresa(
            id_empresa=id_empresa,
            nombre=datos_para_validar['nombre'],
            sector=datos_para_validar['sector'],
            logo=datos_para_validar['logo'],
            ubicacion=datos_para_validar['ubicacion']
        )
        
        # Actualizar en la base de datos
        resultado = gestor_empresas.actualizar(empresa_actualizada)
        
        if resultado:
            return {
                "mensaje": "Empresa actualizada exitosamente",
                "empresa": {
                    "id_empresa": empresa_actualizada.id_empresa,
                    "nombre": empresa_actualizada.nombre,
                    "sector": empresa_actualizada.sector,
                    "logo": empresa_actualizada.logo,
                    "ubicacion": empresa_actualizada.ubicacion
                }
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No se pudo actualizar la empresa"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )

@router.delete("/api/empresas/{id_empresa}", response_model=dict)
async def eliminar_empresa(id_empresa: int):
    """
    Eliminar una empresa
    """
    try:
        # Verificar si la empresa existe
        empresa_existente = gestor_empresas.buscar(id_empresa)
        if not empresa_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empresa no encontrada"
            )
        
        # Eliminar empresa
        resultado = gestor_empresas.eliminar(id_empresa)
        
        if resultado:
            return {
                "mensaje": "Empresa eliminada exitosamente",
                "id_empresa": id_empresa
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No se pudo eliminar la empresa"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )

@router.get("/api/empresas/count", response_model=dict)
async def contar_empresas():
    """
    Obtener el número total de empresas
    """
    try:
        count = gestor_empresas.cantidad_elementos()
        return {"total_empresas": count}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al contar empresas: {str(e)}"
        )
