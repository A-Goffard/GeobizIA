@echo off
echo ================================================================
echo SCRIPT DE INSTALACION Y VERIFICACION - GeobizIA
echo ================================================================
echo.

echo 🔍 Verificando entorno virtual...
if exist "GeobiziaEnv\Scripts\activate.bat" (
    echo ✅ Entorno virtual encontrado
    call GeobiziaEnv\Scripts\activate.bat
    echo ✅ Entorno virtual activado
) else (
    echo ❌ Entorno virtual no encontrado
    echo 💡 Creando entorno virtual...
    python -m venv GeobiziaEnv
    call GeobiziaEnv\Scripts\activate.bat
    echo ✅ Entorno virtual creado y activado
)

echo.
echo 📦 Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

echo.
echo 🔍 Verificando instalación...
python verificar_requirements.py

echo.
echo ================================================================
echo 🎉 ¡INSTALACION COMPLETADA!
echo ================================================================
echo.
echo Para iniciar el servidor:
echo   python -m uvicorn GeobizIA.api.main:app --reload
echo.
pause
