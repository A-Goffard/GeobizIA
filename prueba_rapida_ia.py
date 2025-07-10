"""
Script de prueba rápida para verificar que el endpoint de IA funciona
"""
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("🧪 PRUEBA RÁPIDA - ENDPOINT IA")
    print("=" * 40)
    
    try:
        # Probar importaciones
        print("1. Probando importaciones...")
        from GeobizIA.api.api_ia_publicaciones import router, GenerarPublicacionRequest, PublicacionGenerada
        print("   ✅ Importaciones exitosas")
        
        # Probar creación de request
        print("2. Probando modelos Pydantic...")
        request = GenerarPublicacionRequest(
            id_actividad_realizada=1,
            tipo_publicacion="completado",
            tono="profesional",
            plataforma="instagram",
            incluir_hashtags=True
        )
        print("   ✅ Request creada correctamente")
        
        # Probar función de plantillas
        print("3. Probando generación con plantillas...")
        from GeobizIA.api.api_ia_publicaciones import generar_contenido_ia
        
        contenido = generar_contenido_ia("Actividad de prueba", request)
        print(f"   ✅ Contenido generado: {contenido[:50]}...")
        
        # Probar función de hashtags
        print("4. Probando generación de hashtags...")
        from GeobizIA.api.api_ia_publicaciones import generar_hashtags
        
        # Crear un objeto actividad simulado
        class ActividadSimulada:
            def __init__(self):
                self.nombre = "Taller de Reciclaje"
        
        actividad_test = ActividadSimulada()
        hashtags = generar_hashtags(actividad_test, request)
        print(f"   ✅ Hashtags generados: {hashtags}")
        
        print("\n🎉 TODAS LAS PRUEBAS PASARON")
        print("🚀 El servidor debería arrancar sin problemas")
        print("\n💡 Para arrancar el servidor:")
        print("   python -m uvicorn GeobizIA.api.main:app --reload --port 8000")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("🔧 Revisa la configuración del proyecto")

if __name__ == "__main__":
    main()
