from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from GeobizIA.api.api_actividades import router as actividades_router
from GeobizIA.api.api_actividades_realizadas import router as actividades_realizadas_router
from GeobizIA.api.api_eventos import router as eventos_router
from GeobizIA.api.api_proyectos import router as proyectos_router
from GeobizIA.api.api_clientes import router as clientes_router
from GeobizIA.api.api_empresas import router as empresas_router
from GeobizIA.api.api_facturas import router as facturas_router
from GeobizIA.api.api_auth import router as auth_router
from GeobizIA.api.api_ia_publicaciones import router as ia_publicaciones_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(actividades_router)
app.include_router(actividades_realizadas_router)
app.include_router(eventos_router)
app.include_router(proyectos_router)
app.include_router(clientes_router)
app.include_router(empresas_router)
app.include_router(facturas_router)
app.include_router(auth_router)
app.include_router(ia_publicaciones_router, prefix="/api/ia")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)