# filepath: c:\Users\Geobizi\Desktop\Programacion\GeobizIA\GoffardSevillanoAintzane\src\api\main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.api_actividades import router as actividades_router
# from src.api.usuarios import router as usuarios_router
# ...otros routers...

app = FastAPI()

# Habilita CORS para el frontend (ajusta el puerto si es necesario)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:5173"],  # agrega aquí los orígenes de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(actividades_router)
# app.include_router(usuarios_router)
# ...otros routers...