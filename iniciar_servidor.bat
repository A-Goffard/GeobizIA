@echo off
echo ================================
echo GeobizIA - Sistema de Proyectos
echo ================================
echo.
echo Este script inicia el servidor de desarrollo y prueba la funcionalidad de proyectos
echo.

echo 1. Activando entorno virtual...
call "c:\Users\Geobizi\Desktop\Programacion\Proyecto_final\GeobiziaEnv\Scripts\activate.bat"

echo.
echo 2. Instalando dependencias si es necesario...
pip install -r requirements.txt

echo.
echo 3. Iniciando servidor de desarrollo...
echo Servidor disponible en: http://localhost:8000
echo Frontend disponible en: http://localhost:8080 (si está ejecutándose)
echo.
echo Para probar la funcionalidad de proyectos:
echo - Abrir otra terminal y ejecutar: python GeobizIA/validaciones/test_proyectos_completo.py
echo - O usar el frontend en: http://localhost:8080
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

cd /d "c:\Users\Geobizi\Desktop\Programacion\Proyecto_final\GeobizIA"
python -m uvicorn GeobizIA.api.main:app --reload --host 0.0.0.0 --port 8000

pause
