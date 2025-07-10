#!/usr/bin/env python3
"""
Test básico para verificar que la funcionalidad de empresas funciona correctamente
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GeobizIA.controlador.dominios.empresa import Empresa
from GeobizIA.controlador.gestores.empresas import Empresas
from GeobizIA.validaciones.validar_empresa import validar_datos_empresa

def test_empresas_basico():
    """Test básico para empresas"""
    print("=== TEST BÁSICO DE EMPRESAS ===")
    
    # Datos de prueba
    datos_empresa = {
        'nombre': 'Empresa Test',
        'sector': 'Tecnología',
        'logo': 'https://example.com/logo.png',
        'ubicacion': 'Barcelona, España'
    }
    
    print(f"Datos de prueba: {datos_empresa}")
    
    # 1. Validar datos
    print("\n1. Validando datos...")
    es_valido, mensaje = validar_datos_empresa(datos_empresa)
    print(f"   Validación: {es_valido}")
    if not es_valido:
        print(f"   ❌ Error de validación: {mensaje}")
        return False
    
    # 2. Crear objeto Empresa
    print("\n2. Creando objeto Empresa...")
    try:
        empresa = Empresa(
            id_empresa=None,
            nombre=datos_empresa['nombre'],
            sector=datos_empresa['sector'],
            logo=datos_empresa['logo'],
            ubicacion=datos_empresa['ubicacion']
        )
        print(f"   ✅ Empresa creada: {empresa}")
    except Exception as e:
        print(f"   ❌ Error al crear objeto Empresa: {e}")
        return False
    
    # 3. Probar gestor
    print("\n3. Probando gestor...")
    try:
        gestor = Empresas()
        
        # Agregar empresa
        resultado = gestor.agregar(empresa)
        if resultado:
            print(f"   ✅ Empresa agregada con ID: {resultado.id_empresa}")
            
            # Buscar empresa
            empresa_encontrada = gestor.buscar(resultado.id_empresa)
            if empresa_encontrada:
                print(f"   ✅ Empresa encontrada: {empresa_encontrada.nombre}")
                
                # Listar todas las empresas
                todas_empresas = gestor.mostrar_todos_los_elem()
                print(f"   ✅ Total empresas: {len(todas_empresas)}")
                
                # Eliminar empresa de prueba
                if gestor.eliminar(resultado.id_empresa):
                    print(f"   ✅ Empresa eliminada correctamente")
                else:
                    print(f"   ⚠️  No se pudo eliminar la empresa")
                
                return True
            else:
                print(f"   ❌ No se pudo encontrar la empresa")
                return False
        else:
            print(f"   ❌ No se pudo agregar la empresa")
            return False
            
    except Exception as e:
        print(f"   ❌ Error en gestor: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando test básico de empresas...")
    
    if test_empresas_basico():
        print("\n✅ Test de empresas completado exitosamente")
    else:
        print("\n❌ Test de empresas falló")
