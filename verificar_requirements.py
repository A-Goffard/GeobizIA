#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias del requirements.txt
están correctamente instaladas y funcionando.

Uso: python verificar_requirements.py
"""

import sys
import subprocess
import importlib
from pathlib import Path

def verificar_paquete(nombre_paquete, nombre_import=None):
    """Verifica si un paquete está instalado y se puede importar"""
    if nombre_import is None:
        nombre_import = nombre_paquete
    
    try:
        importlib.import_module(nombre_import)
        return True, "✅ OK"
    except ImportError as e:
        return False, f"❌ Error: {str(e)}"

def obtener_version_paquete(nombre_paquete):
    """Obtiene la versión instalada de un paquete"""
    try:
        result = subprocess.run([sys.executable, "-c", f"import {nombre_paquete}; print({nombre_paquete}.__version__)"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Intentar con metadata si no tiene __version__
            result = subprocess.run([sys.executable, "-c", f"import pkg_resources; print(pkg_resources.get_distribution('{nombre_paquete}').version)"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
    except:
        pass
    return "Desconocida"

def main():
    print("🔍 VERIFICANDO DEPENDENCIAS DE GEOBIZIA")
    print("=" * 50)
    
    # Paquetes principales a verificar
    paquetes_criticos = [
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn"), 
        ("pydantic", "pydantic"),
        ("sqlalchemy", "sqlalchemy"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("scikit-learn", "sklearn"),
        ("matplotlib", "matplotlib"),
        ("requests", "requests"),
        ("bcrypt", "bcrypt")
    ]
    
    print("\n📦 DEPENDENCIAS PRINCIPALES:")
    print("-" * 30)
    
    errores = []
    
    for paquete, modulo in paquetes_criticos:
        exito, mensaje = verificar_paquete(modulo)
        version = obtener_version_paquete(modulo) if exito else "N/A"
        
        print(f"{paquete:<15} {version:<12} {mensaje}")
        
        if not exito:
            errores.append(paquete)
    
    # Verificar paquetes opcionales
    print("\n🔧 DEPENDENCIAS OPCIONALES:")
    print("-" * 30)
    
    paquetes_opcionales = [
        ("openai", "openai"),
        ("plotly", "plotly"),
        ("seaborn", "seaborn"),
        ("openpyxl", "openpyxl")
    ]
    
    for paquete, modulo in paquetes_opcionales:
        exito, mensaje = verificar_paquete(modulo)
        version = obtener_version_paquete(modulo) if exito else "N/A"
        status = "✅ Disponible" if exito else "⚠️  No instalado (opcional)"
        
        print(f"{paquete:<15} {version:<12} {status}")
    
    # Verificar API específica del proyecto
    print("\n🚀 VERIFICANDO APIS DEL PROYECTO:")
    print("-" * 30)
    
    try:
        # Verificar que la estructura del proyecto existe
        project_paths = [
            "GeobizIA/api/main.py",
            "GeobizIA/api/api_ia_publicaciones.py",
            "GeobizIA/controlador/gestores/actividades.py"
        ]
        
        for path in project_paths:
            if Path(path).exists():
                print(f"✅ {path}")
            else:
                print(f"❌ {path} - No encontrado")
                errores.append(f"Archivo {path}")
        
    except Exception as e:
        print(f"❌ Error verificando estructura del proyecto: {e}")
        errores.append("Estructura del proyecto")
    
    # Resumen final
    print("\n" + "=" * 50)
    if errores:
        print("❌ ERRORES ENCONTRADOS:")
        for error in errores:
            print(f"   • {error}")
        print("\n💡 Para instalar dependencias faltantes:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("🎉 ¡TODAS LAS DEPENDENCIAS ESTÁN CORRECTAMENTE INSTALADAS!")
        print("✅ El proyecto está listo para ejecutarse")
        print("\n🚀 Para iniciar el servidor:")
        print("   python -m uvicorn GeobizIA.api.main:app --reload")
        sys.exit(0)

if __name__ == "__main__":
    main()
