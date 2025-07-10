@echo off
echo.
echo ================================================
echo 🤖 GENERADOR DE PUBLICACIONES IA - GEOBIZIA
echo ================================================
echo.

echo 🔍 Verificando configuración...
python prueba_rapida_ia.py

echo.
echo 🚀 Arrancando servidor FastAPI en puerto 8000...
echo.
echo 💡 Después de que arranque, abre otra terminal y ejecuta:
echo    cd vista/frontend
echo    npm run serve
echo.
echo 🌐 Luego visita: http://localhost:8080/ia/generador-publicaciones
echo.
echo ⏹️  Para detener el servidor: Ctrl+C
echo.

python -m uvicorn GeobizIA.api.main:app --reload --port 8000
