#!/usr/bin/env python3
"""
Script de prueba para el endpoint de IA de publicaciones
"""
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Probar las importaciones del módulo de IA"""
    try:
        from GeobizIA.api.api_ia_publicaciones import router, GenerarPublicacionRequest, PublicacionGenerada
        print("✅ Importaciones exitosas")
        return True
    except ImportError as e:
        print(f"❌ Error en las importaciones: {e}")
        return False

def test_gestor_actividades():
    """Probar el gestor de actividades realizadas"""
    try:
        from GeobizIA.controlador.gestores.actividades_realizadas import ActividadesRealizadas
        from GeobizIA.controlador.gestores.actividades import Actividades
        
        print("✅ Gestores importados correctamente")
        
        # Crear instancias
        gestor_realizadas = ActividadesRealizadas()
        gestor_actividades = Actividades()
        
        print("✅ Instancias creadas correctamente")
        return True
    except Exception as e:
        print(f"❌ Error con los gestores: {e}")
        return False

def test_plantillas():
    """Probar la generación con plantillas"""
    try:
        from GeobizIA.api.api_ia_publicaciones import generar_contenido_ia, GenerarPublicacionRequest
        
        # Crear una request de prueba
        request = GenerarPublicacionRequest(
            id_actividad_realizada=1,
            tipo_publicacion="completado",
            tono="profesional",
            plataforma="instagram",
            incluir_hashtags=True
        )
        
        contenido = generar_contenido_ia("Actividad de prueba", request)
        print(f"✅ Contenido generado: {contenido[:50]}...")
        return True
    except Exception as e:
        print(f"❌ Error en plantillas: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🧪 Iniciando pruebas del sistema IA...")
    print("="*50)
    
    tests = [
        ("Importaciones", test_imports),
        ("Gestores", test_gestor_actividades),
        ("Plantillas", test_plantillas),
    ]
    
    resultados = []
    for nombre, test_func in tests:
        print(f"\n🔍 Probando: {nombre}")
        resultado = test_func()
        resultados.append((nombre, resultado))
    
    print("\n" + "="*50)
    print("📊 RESUMEN DE PRUEBAS:")
    for nombre, resultado in resultados:
        status = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"  {nombre}: {status}")
    
    total_exitosas = sum(1 for _, resultado in resultados if resultado)
    print(f"\n🎯 Total: {total_exitosas}/{len(resultados)} pruebas exitosas")
    
    if total_exitosas == len(resultados):
        print("🎉 ¡Todas las pruebas pasaron! El sistema está listo.")
    else:
        print("⚠️ Algunas pruebas fallaron. Revisar errores arriba.")

if __name__ == "__main__":
    main()
