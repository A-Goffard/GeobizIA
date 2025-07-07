<template>
  <div class="contenedor-principal">
    <div class="contact-container">
      <h1>Predicción de Resultados de Actividad</h1>
      <p>Introduce los datos básicos para predecir los resultados esperados de la actividad</p>
      
      <form @submit.prevent="realizarPrediccion">
        <div class="form-group">
          <label>Actividad:</label>
          <select v-model.number="formData.id_actividad" required>
            <option value="" disabled>Selecciona una actividad</option>
            <option v-for="actividad in actividades" :key="actividad.id_actividad" :value="actividad.id_actividad">
              {{ actividad.nombre }}
            </option>
          </select>
        </div>
        
        <div class="form-group">
          <label>Fecha prevista:</label>
          <input v-model="formData.fecha" type="date" required />
        </div>
        
        <div class="form-group">
          <label>Coste económico estimado (€):</label>
          <input v-model.number="formData.coste_economico" type="number" step="0.01" min="0" required />
        </div>
        
        <button type="submit" :disabled="cargandoPrediccion">
          {{ cargandoPrediccion ? 'Calculando predicción...' : 'Realizar Predicción' }}
        </button>
      </form>

      <!-- Resultados de la predicción -->
      <div v-if="prediccionRealizada" class="prediccion-resultados">
        <h2>Resultados de la Predicción</h2>
        
        <div class="resultado-card">
          <h3>{{ nombreActividad }}</h3>
          
          <div class="prediccion-valores">
            <div class="valor-predicho">
              <label>Asistentes esperados:</label>
              <span class="valor">{{ resultadoPrediccion.asistentes_predichos }}</span>
            </div>
            
            <div class="valor-predicho">
              <label>Facturación estimada:</label>
              <span class="valor">{{ resultadoPrediccion.facturacion_predicha }}€</span>
            </div>
            
            <div class="valor-predicho">
              <label>Beneficio estimado:</label>
              <span class="valor" :class="{ 'positivo': resultadoPrediccion.beneficio_estimado >= 0, 'negativo': resultadoPrediccion.beneficio_estimado < 0 }">
                {{ resultadoPrediccion.beneficio_estimado }}€
              </span>
            </div>
          </div>
        </div>

        <!-- Datos históricos si están disponibles -->
        <div v-if="datosHistoricos && datosHistoricos.historico_disponible" class="historicos-card">
          <h3>Datos Históricos de esta Actividad</h3>
          <div class="historicos-grid">
            <div class="historico-item">
              <label>Realizaciones anteriores:</label>
              <span>{{ datosHistoricos.total_realizaciones }}</span>
            </div>
            <div class="historico-item">
              <label>Asistentes promedio:</label>
              <span>{{ datosHistoricos.asistentes_promedio }}</span>
            </div>
            <div class="historico-item">
              <label>Facturación promedio:</label>
              <span>{{ datosHistoricos.facturacion_promedio }}€</span>
            </div>
            <div class="historico-item">
              <label>Beneficio promedio:</label>
              <span>{{ datosHistoricos.beneficio_promedio }}€</span>
            </div>
          </div>
        </div>

        <!-- Métricas del modelo -->
        <div v-if="metricasModelo" class="metricas-card">
          <h3>Confiabilidad del Modelo</h3>
          <div class="metricas-info">
            <p><strong>Precisión en asistentes:</strong> {{ Math.round(metricasModelo.asistentes.r2 * 100) }}%</p>
            <p><strong>Precisión en facturación:</strong> {{ Math.round(metricasModelo.facturacion.r2 * 100) }}%</p>
          </div>
        </div>
      </div>

      <!-- Mensajes -->
      <div v-if="successMessage" class="mensaje-exito">{{ successMessage }}</div>
      <div v-if="errorMessage" class="mensaje-error">{{ errorMessage }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const formData = ref({
  id_actividad: null,
  fecha: '',
  coste_economico: 0
})

const actividades = ref([])
const cargandoPrediccion = ref(false)
const prediccionRealizada = ref(false)
const resultadoPrediccion = ref(null)
const datosHistoricos = ref(null)
const metricasModelo = ref(null)
const nombreActividad = ref('')

const successMessage = ref('')
const errorMessage = ref('')

onMounted(async () => {
  // Carga actividades
  try {
    const resAct = await fetch('http://localhost:8000/api/actividades')
    actividades.value = await resAct.json()
  } catch (e) {
    actividades.value = []
    console.error('Error cargando actividades:', e)
  }
})

async function realizarPrediccion() {
  successMessage.value = ''
  errorMessage.value = ''
  cargandoPrediccion.value = true
  prediccionRealizada.value = false

  // Validar datos
  if (!formData.value.id_actividad || !formData.value.fecha || formData.value.coste_economico < 0) {
    errorMessage.value = 'Por favor, completa todos los campos correctamente.'
    cargandoPrediccion.value = false
    return
  }

  try {
    const response = await fetch('http://localhost:8000/api/actividades_realizadas/prediccion', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        id_actividad: formData.value.id_actividad,
        fecha: formData.value.fecha,
        coste_economico: formData.value.coste_economico
      })
    })

    const data = await response.json()

    if (response.ok) {
      resultadoPrediccion.value = data.prediccion
      datosHistoricos.value = data.datos_historicos
      metricasModelo.value = data.prediccion.metricas_modelo
      nombreActividad.value = data.nombre_actividad
      prediccionRealizada.value = true
      successMessage.value = 'Predicción realizada correctamente'
    } else {
      errorMessage.value = data.detail || 'Error al realizar la predicción'
    }
  } catch (err) {
    errorMessage.value = 'Error de red o del servidor al realizar la predicción'
    console.error('Error:', err)
  } finally {
    cargandoPrediccion.value = false
  }
}
</script>

<style scoped>
.contenedor-principal {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.contact-container {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

button {
  background: #007bff;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

button:hover:not(:disabled) {
  background: #0056b3;
}

button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.prediccion-resultados {
  margin-top: 30px;
  padding: 20px 0;
}

.resultado-card,
.historicos-card,
.metricas-card {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}

.resultado-card h3,
.historicos-card h3,
.metricas-card h3 {
  margin: 0 0 15px 0;
  color: #495057;
}

.prediccion-valores {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.valor-predicho {
  background: white;
  padding: 15px;
  border-radius: 4px;
  border-left: 4px solid #007bff;
}

.valor-predicho label {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.valor-predicho .valor {
  display: block;
  font-size: 24px;
  font-weight: bold;
  margin-top: 5px;
}

.valor.positivo {
  color: #28a745;
}

.valor.negativo {
  color: #dc3545;
}

.historicos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 15px;
}

.historico-item {
  background: white;
  padding: 12px;
  border-radius: 4px;
  text-align: center;
}

.historico-item label {
  font-size: 12px;
  color: #666;
  margin: 0;
}

.historico-item span {
  display: block;
  font-size: 18px;
  font-weight: bold;
  margin-top: 5px;
  color: #333;
}

.metricas-info {
  background: white;
  padding: 15px;
  border-radius: 4px;
}

.metricas-info p {
  margin: 8px 0;
}

.mensaje-exito {
  background: #d4edda;
  color: #155724;
  padding: 10px;
  border-radius: 4px;
  margin-top: 15px;
}

.mensaje-error {
  background: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 4px;
  margin-top: 15px;
}
</style>
