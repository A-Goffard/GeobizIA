from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from GeobizIA.controlador.gestores.usuarios import Usuarios

router = APIRouter()
gestor_usuarios = Usuarios()

class LoginCredentials(BaseModel):
    email: str
    password: str

@router.post("/api/login")
def login(credentials: LoginCredentials):
    try:
        # Buscar usuario por email
        usuario = gestor_usuarios.buscar_por_email(credentials.email)

        # Verificar si el usuario existe y la contraseña es correcta
        if not usuario or not usuario.check_password(credentials.password):
            raise HTTPException(
                status_code=401,
                detail="Email o contraseña incorrectos",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # En una aplicación real, aquí generarías y devolverías un token (JWT)
        return {"mensaje": "Login exitoso", "rol": usuario.rol}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")
