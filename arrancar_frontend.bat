@echo off
echo.
echo ================================================
echo 🎨 FRONTEND VUE.JS - GEOBIZIA
echo ================================================
echo.

cd vista/frontend

echo 🔍 Verificando dependencias...
if not exist node_modules (
    echo 📦 Instalando dependencias de Node.js...
    npm install
)

echo.
echo 🚀 Arrancando servidor de desarrollo Vue.js...
echo.
echo 🌐 El frontend estará disponible en:
echo    http://localhost:8080/ia/generador-publicaciones
echo.
echo ⏹️  Para detener el servidor: Ctrl+C
echo.

npm run serve
