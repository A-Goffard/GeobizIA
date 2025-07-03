# filepath: c:\Users\Geobizi\Desktop\Programacion\GeobizIA\GoffardSevillanoAintzane\src\api\main.py
from fastapi import FastAPI
from src.api.api_actividades import router as actividades_router
# from src.api.usuarios import router as usuarios_router
# ...otros routers...

app = FastAPI()

app.include_router(actividades_router)
# app.include_router(usuarios_router)
# ...otros routers...