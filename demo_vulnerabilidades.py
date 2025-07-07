#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔒 DEMOSTRACIÓN DE VULNERABILIDADES DE SEGURIDAD
Script educativo para entender los riesgos de seguridad en APIs

⚠️ IMPORTANTE: Este script es solo para fines educativos
"""

import json
import requests
from datetime import datetime

# =============================================================================
# 🚨 DEMOSTRACIÓN 1: INYECCIÓN DE CAMPOS CON **datos
# =============================================================================

print("=" * 70)
print("🚨 DEMOSTRACIÓN 1: VULNERABILIDAD DE INYECCIÓN DE CAMPOS")
print("=" * 70)

# Simulación de código VULNERABLE
class ActividadVulnerable:
    def __init__(self, **kwargs):
        # ❌ PELIGROSO: Acepta cualquier campo
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return f"Actividad: {self.__dict__}"

# Simulación de código SEGURO
class ActividadSegura:
    def __init__(self, tipo, nombre, descripcion, responsable, duracion, 
                 coste_economico, coste_horas, facturacion, 
                 resultados="", valoracion="", observaciones=""):
        # ✅ SEGURO: Solo campos específicos
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.responsable = responsable
        self.duracion = duracion
        self.coste_economico = coste_economico
        self.coste_horas = coste_horas
        self.facturacion = facturacion
        self.resultados = resultados
        self.valoracion = valoracion
        self.observaciones = observaciones
    
    def __str__(self):
        return f"Actividad: {self.__dict__}"

# Datos legítimos del usuario
datos_usuario = {
    "tipo": "Reunión",
    "nombre": "Reunión de proyecto",
    "descripcion": "Reunión semanal del equipo",
    "responsable": "Juan Pérez",
    "duracion": "2 horas",
    "coste_economico": 200.0,
    "coste_horas": 2.0,
    "facturacion": 250.0
}

# Datos maliciosos del atacante
datos_atacante = {
    **datos_usuario,  # Incluye datos legítimos
    # ⚠️ Campos maliciosos inyectados:
    "is_admin": True,
    "secret_key": "hack123",
    "delete_all_data": True,
    "bypass_validation": True,
    "internal_system_flag": "COMPROMISED"
}

print("\n📝 DATOS LEGÍTIMOS:")
print(json.dumps(datos_usuario, indent=2, ensure_ascii=False))

print("\n🔥 DATOS MALICIOSOS (con campos inyectados):")
print(json.dumps(datos_atacante, indent=2, ensure_ascii=False))

print("\n❌ RESULTADO CON CÓDIGO VULNERABLE:")
actividad_vulnerable = ActividadVulnerable(**datos_atacante)
print(actividad_vulnerable)
print(f"¿Es admin? {getattr(actividad_vulnerable, 'is_admin', False)}")
print(f"Clave secreta: {getattr(actividad_vulnerable, 'secret_key', 'N/A')}")

print("\n✅ RESULTADO CON CÓDIGO SEGURO:")
try:
    # Solo acepta campos definidos
    actividad_segura = ActividadSegura(**datos_atacante)
    print("❌ ERROR: El código seguro no debería ejecutarse con campos extra")
except TypeError as e:
    print(f"✅ PROTEGIDO: {e}")

# Creación segura solo con campos válidos
actividad_segura = ActividadSegura(**datos_usuario)
print(f"✅ ACTIVIDAD SEGURA: {actividad_segura}")

# =============================================================================
# 🚨 DEMOSTRACIÓN 2: EXPOSICIÓN DE DATOS EN GET vs POST
# =============================================================================

print("\n" + "=" * 70)
print("🚨 DEMOSTRACIÓN 2: EXPOSICIÓN DE DATOS EN GET REQUESTS")
print("=" * 70)

# Simulación de log de servidor
def simular_log_servidor(method, url, body=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {method} {url}"
    if body:
        log_entry += f" - Body: {json.dumps(body)[:100]}..."
    else:
        log_entry += " - No body"
    return log_entry

# Datos sensibles
datos_sensibles = {
    "nombre_cliente": "EmpresaSecreta S.A.",
    "proyecto_confidencial": "Proyecto Omega",
    "facturacion_privada": 50000,
    "responsable_interno": "Director.Financiero",
    "notas_internas": "Cliente VIP - descuento especial aplicado"
}

print("\n❌ PROBLEMA: GET REQUEST con datos sensibles")
# En GET, los parámetros van en la URL
url_get = "/api/actividades/buscar?" + "&".join([f"{k}={v}" for k, v in datos_sensibles.items()])
log_get = simular_log_servidor("GET", url_get)
print(f"📋 LOG DEL SERVIDOR: {log_get}")
print("🔍 VISIBLE EN:")
print("   - Logs del servidor ✓")
print("   - Historial del navegador ✓") 
print("   - Cache de proxies ✓")
print("   - DevTools del navegador ✓")

print("\n✅ SOLUCIÓN: POST REQUEST con datos en el body")
url_post = "/api/actividades/buscar-seguro"
log_post = simular_log_servidor("POST", url_post, datos_sensibles)
print(f"📋 LOG DEL SERVIDOR: {log_post}")
print("🔒 PROTEGIDO:")
print("   - URL limpia ✓")
print("   - Datos en body encriptado ✓")
print("   - No visible en historial ✓")

# =============================================================================
# 🚨 DEMOSTRACIÓN 3: EXPOSICIÓN EN FRONTEND
# =============================================================================

print("\n" + "=" * 70)
print("🚨 DEMOSTRACIÓN 3: EXPOSICIÓN DE DATOS EN FRONTEND")
print("=" * 70)

# Datos del backend (incluye información sensible)
datos_backend = {
    "id": 1,
    "nombre": "Proyecto Alpha",
    "descripcion": "Desarrollo de nueva aplicación",
    "responsable": "Ana García",
    "duracion": "3 meses",
    
    # ❌ DATOS SENSIBLES que NO deberían ir al frontend:
    "password_admin": "admin123",
    "api_key_secret": "sk-1234567890abcdef",
    "costo_real_interno": 75000,
    "margen_beneficio": 0.35,
    "notas_confidenciales": "Cliente tiene problemas financieros",
    "codigo_acceso_sistema": "SYS-9876",
    "datos_bancarios": {"cuenta": "ES91 2100 0418 4502 0005 1332"}
}

print("\n❌ MAL: Enviar todo al frontend")
print("JSON visible en DevTools del navegador:")
print(json.dumps(datos_backend, indent=2, ensure_ascii=False))

print("\n✅ BIEN: Solo datos necesarios para la UI")
datos_frontend_seguros = {
    "id": datos_backend["id"],
    "nombre": datos_backend["nombre"],
    "descripcion": datos_backend["descripcion"],
    "responsable": datos_backend["responsable"],
    "duracion": datos_backend["duracion"]
    # ✅ Sin datos sensibles
}
print("JSON seguro para el frontend:")
print(json.dumps(datos_frontend_seguros, indent=2, ensure_ascii=False))

# =============================================================================
# 📊 RESUMEN DE VULNERABILIDADES
# =============================================================================

print("\n" + "=" * 70)
print("📊 RESUMEN DE VULNERABILIDADES DEMOSTRADAS")
print("=" * 70)

vulnerabilidades = [
    {
        "nombre": "Inyección de campos (**datos)",
        "riesgo": "ALTO",
        "impacto": "Escalada de privilegios, corrupción de datos",
        "solucion": "Asignación explícita de campos"
    },
    {
        "nombre": "Exposición en GET requests",
        "riesgo": "MEDIO",
        "impacto": "Datos sensibles en logs y URLs",
        "solucion": "POST para datos sensibles"
    },
    {
        "nombre": "Sobre-exposición en frontend",
        "riesgo": "MEDIO",
        "impacto": "Datos internos visibles al usuario",
        "solucion": "Filtrar campos sensibles"
    }
]

for i, vuln in enumerate(vulnerabilidades, 1):
    print(f"\n{i}. {vuln['nombre']}")
    print(f"   🔥 Riesgo: {vuln['riesgo']}")
    print(f"   💥 Impacto: {vuln['impacto']}")
    print(f"   ✅ Solución: {vuln['solucion']}")

print("\n" + "=" * 70)
print("🎓 MENSAJE PARA LA DEFENSA")
print("=" * 70)
print("""
La profesora tiene razón en señalar estas vulnerabilidades. Como desarrolladores,
debemos ser conscientes de que:

1. **Seguridad no es opcional**: Cada línea de código puede ser un vector de ataque
2. **Principio de menor privilegio**: Solo procesar/exponer datos necesarios
3. **Defensa en profundidad**: Múltiples capas de validación y protección
4. **Educación continua**: La seguridad evoluciona constantemente

¡Estas correcciones demuestran madurez profesional y responsabilidad!
""")

if __name__ == "__main__":
    print("\n🔒 Demostración completa. Revisa los logs para entender los riesgos.")
