#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias funcionan correctamente
después de la actualización del requirements.txt
"""

def verificar_dependencias():
    """Verifica que todas las dependencias principales funcionen"""
    print("🔍 VERIFICANDO DEPENDENCIAS ACTUALIZADAS")
    print("=" * 50)
    
    dependencias = [
        ("FastAPI", "fastapi"),
        ("Uvicorn", "uvicorn"),
        ("Pydantic", "pydantic"),
        ("SQLAlchemy", "sqlalchemy"),
        ("Pandas", "pandas"),
        ("NumPy", "numpy"),
        ("Matplotlib", "matplotlib"),
        ("Scikit-learn", "sklearn"),
        ("Requests", "requests"),
        ("PyODBC", "pyodbc"),
    ]
    
    resultados = []
    
    for nombre, modulo in dependencias:
        try:
            __import__(modulo)
            print(f"✅ {nombre}: OK")
            resultados.append((nombre, True))
        except ImportError as e:
            print(f"❌ {nombre}: ERROR - {e}")
            resultados.append((nombre, False))
    
    print("\n" + "=" * 50)
    exitosas = sum(1 for _, ok in resultados if ok)
    total = len(resultados)
    
    print(f"📊 RESULTADO: {exitosas}/{total} dependencias funcionando")
    
    if exitosas == total:
        print("🎉 ¡Todas las dependencias están funcionando correctamente!")
        return True
    else:
        print("⚠️ Algunas dependencias tienen problemas")
        return False

def verificar_apis():
    """Verifica que las APIs del proyecto funcionen"""
    print("\n🔍 VERIFICANDO APIs DEL PROYECTO")
    print("=" * 50)
    
    try:
        # Verificar imports del proyecto
        from GeobizIA.api.api_ia_publicaciones import router
        print("✅ API IA Publicaciones: OK")
        
        from GeobizIA.controlador.gestores.actividades import Actividades
        print("✅ Gestor Actividades: OK")
        
        from GeobizIA.controlador.gestores.actividades_realizadas import ActividadesRealizadas
        print("✅ Gestor Actividades Realizadas: OK")
        
        return True
    except Exception as e:
        print(f"❌ Error en APIs: {e}")
        return False

def verificar_funcionalidad_ia():
    """Verifica que el generador IA funcione"""
    print("\n🤖 VERIFICANDO GENERADOR IA")
    print("=" * 50)
    
    try:
        from GeobizIA.api.api_ia_publicaciones import GenerarPublicacionRequest, generar_hashtags
        
        # Crear objeto de prueba
        class ActividadPrueba:
            def __init__(self):
                self.nombre = "Taller de Reciclaje"
                self.tipo = "taller"
                self.descripcion = "Actividad sobre reciclaje"
        
        actividad_test = ActividadPrueba()
        
        request_test = GenerarPublicacionRequest(
            id_actividad_realizada=1,
            tipo_publicacion="completado",
            tono="profesional",
            plataforma="instagram",
            incluir_hashtags=True
        )
        
        hashtags = generar_hashtags(actividad_test, request_test)
        print(f"✅ Generación de hashtags: OK")
        print(f"   Ejemplo: {hashtags[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Error en generador IA: {e}")
        return False

def main():
    """Función principal de verificación"""
    print("🧪 VERIFICACIÓN POST-ACTUALIZACIÓN")
    print("📅 Fecha: 10 de julio de 2025")
    print("🎯 Objetivo: Verificar requirements.txt actualizado")
    print("=" * 50)
    
    # Ejecutar verificaciones
    deps_ok = verificar_dependencias()
    apis_ok = verificar_apis()
    ia_ok = verificar_funcionalidad_ia()
    
    print("\n" + "=" * 50)
    print("📋 RESUMEN FINAL")
    print("=" * 50)
    
    estado_general = deps_ok and apis_ok and ia_ok
    
    if estado_general:
        print("🎉 ¡TODO FUNCIONA PERFECTAMENTE!")
        print("✅ Dependencias actualizadas correctamente")
        print("✅ APIs del proyecto funcionando")
        print("✅ Generador IA operativo")
        print("\n🚀 El proyecto está listo para continuar el desarrollo")
    else:
        print("⚠️ Se encontraron algunos problemas:")
        if not deps_ok:
            print("  - Revisar instalación de dependencias")
        if not apis_ok:
            print("  - Verificar estructura del proyecto")
        if not ia_ok:
            print("  - Revisar código del generador IA")
    
    return estado_general

if __name__ == "__main__":
    main()
