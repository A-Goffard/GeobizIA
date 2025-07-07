import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class PredictorActividades:
    def __init__(self):
        self.modelo_asistentes = None
        self.modelo_facturacion = None
        self.entrenado = False
        self.estadisticas_modelo = {}
        
    def preparar_datos(self, lista_actividades):
        """Prepara los datos para el entrenamiento del modelo"""
        if not lista_actividades:
            return None
            
        df = pd.DataFrame(lista_actividades)
        
        # Validar columnas necesarias
        columnas_necesarias = ['id_actividad', 'fecha', 'coste_economico', 'asistentes', 'facturacion']
        if not all(col in df.columns for col in columnas_necesarias):
            return None
            
        # Limpiar datos nulos
        df = df.dropna(subset=columnas_necesarias)
        
        if len(df) < 5:  # Necesitamos al menos 5 registros para entrenar
            return None
            
        # Extraer características de la fecha
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['dia_semana'] = df['fecha'].dt.dayofweek  # 0=Lunes, 6=Domingo
        df['mes'] = df['fecha'].dt.month
        df['trimestre'] = df['fecha'].dt.quarter
        
        # Características para el modelo
        caracteristicas = ['id_actividad', 'coste_economico', 'dia_semana', 'mes', 'trimestre']
        
        X = df[caracteristicas]
        y_asistentes = df['asistentes']
        y_facturacion = df['facturacion']
        
        return X, y_asistentes, y_facturacion
        
    def entrenar_modelos(self, lista_actividades):
        """Entrena los modelos de predicción"""
        datos = self.preparar_datos(lista_actividades)
        
        if datos is None:
            return False, "No hay suficientes datos para entrenar el modelo"
            
        X, y_asistentes, y_facturacion = datos
        
        try:
            # Entrenar modelo para asistentes
            self.modelo_asistentes = RandomForestRegressor(
                n_estimators=50,
                random_state=42,
                max_depth=10
            )
            self.modelo_asistentes.fit(X, y_asistentes)
            
            # Entrenar modelo para facturación
            self.modelo_facturacion = RandomForestRegressor(
                n_estimators=50,
                random_state=42,
                max_depth=10
            )
            self.modelo_facturacion.fit(X, y_facturacion)
            
            # Calcular métricas de evaluación
            self._calcular_metricas(X, y_asistentes, y_facturacion)
            
            self.entrenado = True
            return True, "Modelos entrenados correctamente"
            
        except Exception as e:
            return False, f"Error al entrenar modelos: {str(e)}"
            
    def _calcular_metricas(self, X, y_asistentes, y_facturacion):
        """Calcula métricas de evaluación de los modelos"""
        # Predicciones
        pred_asistentes = self.modelo_asistentes.predict(X)
        pred_facturacion = self.modelo_facturacion.predict(X)
        
        # Métricas para asistentes
        mae_asistentes = mean_absolute_error(y_asistentes, pred_asistentes)
        r2_asistentes = r2_score(y_asistentes, pred_asistentes)
        
        # Métricas para facturación
        mae_facturacion = mean_absolute_error(y_facturacion, pred_facturacion)
        r2_facturacion = r2_score(y_facturacion, pred_facturacion)
        
        self.estadisticas_modelo = {
            'asistentes': {
                'mae': round(mae_asistentes, 2),
                'r2': round(r2_asistentes, 3),
                'promedio_real': round(y_asistentes.mean(), 2)
            },
            'facturacion': {
                'mae': round(mae_facturacion, 2),
                'r2': round(r2_facturacion, 3),
                'promedio_real': round(y_facturacion.mean(), 2)
            }
        }
        
    def predecir(self, id_actividad, fecha, coste_economico):
        """Realiza predicción para una actividad específica"""
        if not self.entrenado:
            return None, "El modelo no ha sido entrenado"
            
        try:
            # Preparar datos de entrada
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
            dia_semana = fecha_dt.weekday()
            mes = fecha_dt.month
            trimestre = (mes - 1) // 3 + 1
            
            X_pred = pd.DataFrame({
                'id_actividad': [id_actividad],
                'coste_economico': [coste_economico],
                'dia_semana': [dia_semana],
                'mes': [mes],
                'trimestre': [trimestre]
            })
            
            # Realizar predicciones
            pred_asistentes = self.modelo_asistentes.predict(X_pred)[0]
            pred_facturacion = self.modelo_facturacion.predict(X_pred)[0]
            
            # Asegurar valores positivos y redondear apropiadamente
            pred_asistentes = max(0, round(pred_asistentes))
            pred_facturacion = max(0, round(pred_facturacion, 2))
            
            # Calcular beneficio estimado
            beneficio_estimado = pred_facturacion - coste_economico
            
            resultado = {
                'asistentes_predichos': int(pred_asistentes),
                'facturacion_predicha': pred_facturacion,
                'beneficio_estimado': round(beneficio_estimado, 2),
                'fecha_prediccion': fecha,
                'parametros_entrada': {
                    'id_actividad': id_actividad,
                    'coste_economico': coste_economico,
                    'fecha': fecha
                },
                'metricas_modelo': self.estadisticas_modelo
            }
            
            return resultado, "Predicción realizada correctamente"
            
        except Exception as e:
            return None, f"Error al realizar predicción: {str(e)}"
            
    def obtener_prediccion_historica(self, id_actividad, lista_actividades):
        """Obtiene estadísticas históricas para una actividad específica"""
        if not lista_actividades:
            return {}
            
        df = pd.DataFrame(lista_actividades)
        
        # Filtrar por actividad
        df_actividad = df[df['id_actividad'] == id_actividad]
        
        if len(df_actividad) == 0:
            return {
                'historico_disponible': False,
                'mensaje': 'No hay datos históricos para esta actividad'
            }
            
        # Calcular estadísticas históricas
        stats = {
            'historico_disponible': True,
            'total_realizaciones': len(df_actividad),
            'asistentes_promedio': round(df_actividad['asistentes'].mean(), 1),
            'asistentes_min': int(df_actividad['asistentes'].min()),
            'asistentes_max': int(df_actividad['asistentes'].max()),
            'facturacion_promedio': round(df_actividad['facturacion'].mean(), 2),
            'facturacion_min': round(df_actividad['facturacion'].min(), 2),
            'facturacion_max': round(df_actividad['facturacion'].max(), 2),
            'coste_promedio': round(df_actividad['coste_economico'].mean(), 2),
            'beneficio_promedio': round((df_actividad['facturacion'] - df_actividad['coste_economico']).mean(), 2)
        }
        
        return stats

def realizar_prediccion_actividad(lista_actividades, id_actividad, fecha, coste_economico, id_to_nombre=None):
    """Función principal para realizar predicción de actividad"""
    predictor = PredictorActividades()
    
    # Entrenar modelos
    exito, mensaje = predictor.entrenar_modelos(lista_actividades)
    
    if not exito:
        return {
            'error': True,
            'mensaje': mensaje,
            'prediccion': None
        }
    
    # Realizar predicción
    prediccion, mensaje_pred = predictor.predecir(id_actividad, fecha, coste_economico)
    
    if prediccion is None:
        return {
            'error': True,
            'mensaje': mensaje_pred,
            'prediccion': None
        }
    
    # Obtener datos históricos de la actividad
    datos_historicos = predictor.obtener_prediccion_historica(id_actividad, lista_actividades)
    
    # Agregar nombre de actividad si está disponible
    nombre_actividad = "Actividad desconocida"
    if id_to_nombre and id_actividad in id_to_nombre:
        nombre_actividad = id_to_nombre[id_actividad]
    
    return {
        'error': False,
        'mensaje': mensaje_pred,
        'prediccion': prediccion,
        'datos_historicos': datos_historicos,
        'nombre_actividad': nombre_actividad,
        'modelo_entrenado': True
    }
