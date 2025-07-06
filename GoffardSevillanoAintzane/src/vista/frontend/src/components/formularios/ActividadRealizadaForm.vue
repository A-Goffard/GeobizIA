<template>
  <div class="contenedor-principal">
    <div class="contact-container">
      <h1>Registrar Actividad Realizada</h1>
      <form @submit.prevent="submitForm">
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
          <label>Fecha:</label>
          <input v-model="formData.fecha" type="date" required />
        </div>
        <div class="form-group">
          <label>Asistentes:</label>
          <input v-model.number="formData.asistentes" type="number" required />
        </div>
        <div class="form-group">
          <label>Coste Económico:</label>
          <input v-model.number="formData.coste_economico" type="number" step="0.01" required />
        </div>
        <div class="form-group">
          <label>Facturación:</label>
          <input v-model.number="formData.facturacion" type="number" step="0.01" required />
        </div>
        <div class="form-group">
          <label>Observaciones:</label>
          <textarea v-model="formData.observaciones"></textarea>
        </div>
        <div class="form-group">
          <label>Evento (opcional):</label>
          <select v-model.number="formData.id_evento">
            <option value="">Sin evento</option>
            <option v-for="evento in eventos" :key="evento.id_evento" :value="evento.id_evento">
              {{ evento.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label>Proyecto (opcional):</label>
          <select v-model.number="formData.id_proyecto">
            <option value="">Sin proyecto</option>
            <option v-for="proyecto in proyectos" :key="proyecto.id_proyecto" :value="proyecto.id_proyecto">
              {{ proyecto.nombre }}
            </option>
          </select>
        </div>
        <button type="submit">Guardar</button>
      </form>
      <div v-if="successMessage" style="color: green;">{{ successMessage }}</div>
      <div v-if="errorMessage" style="color: red;">{{ errorMessage }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const formData = ref({
  id_actividad: null,
  fecha: '',
  asistentes: null,
  coste_economico: 0,
  facturacion: 0,
  observaciones: '',
  id_evento: null,
  id_proyecto: null
})

const actividades = ref([])
const eventos = ref([])
const proyectos = ref([])
const actividadesRealizadas = ref([])

const successMessage = ref('')
const errorMessage = ref('')

onMounted(async () => {
  // Carga actividades
  try {
    const resAct = await fetch('http://localhost:8000/api/actividades')
    actividades.value = await resAct.json()
  } catch (e) {
    actividades.value = []
  }
  // Carga eventos
  try {
    const resEvt = await fetch('http://localhost:8000/api/eventos')
    eventos.value = await resEvt.json()
  } catch (e) {
    eventos.value = []
  }
  // Carga proyectos
  try {
    const resProy = await fetch('http://localhost:8000/api/proyectos')
    proyectos.value = await resProy.json()
  } catch (e) {
    proyectos.value = []
  }
  // Carga actividades realizadas
  await cargarActividadesRealizadas()
})

async function cargarActividadesRealizadas() {
  try {
    const res = await fetch('http://localhost:8000/api/actividades_realizadas')
    actividadesRealizadas.value = await res.json()
  } catch (e) {
    actividadesRealizadas.value = []
  }
}

function esDuplicado(nueva) {
  return actividadesRealizadas.value.some(a =>
    a.id_actividad === nueva.id_actividad &&
    a.fecha === nueva.fecha &&
    Number(a.asistentes) === Number(nueva.asistentes) &&
    Number(a.coste_economico) === Number(nueva.coste_economico) &&
    Number(a.facturacion) === Number(nueva.facturacion) &&
    (a.observaciones || '') === (nueva.observaciones || '') &&
    (a.id_evento || null) === (nueva.id_evento || null) &&
    (a.id_proyecto || null) === (nueva.id_proyecto || null)
  )
}

async function submitForm() {
  successMessage.value = ''
  errorMessage.value = ''
  // Recarga actividades realizadas antes de comparar
  await cargarActividadesRealizadas()
  if (esDuplicado(formData.value)) {
    const confirmar = window.confirm('Ya existe una actividad realizada con los mismos datos. ¿Quieres agregarla igualmente?')
    if (!confirmar) {
      errorMessage.value = 'Operación cancelada por posible duplicado.'
      return
    }
  }
  // Convierte campos opcionales vacíos a null
  const datos = { ...formData.value }
  if (datos.id_evento === '' || datos.id_evento === undefined) datos.id_evento = null
  if (datos.id_proyecto === '' || datos.id_proyecto === undefined) datos.id_proyecto = null

  try {
    const response = await fetch('http://localhost:8000/api/actividades_realizadas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    })
    const data = await response.json()
    if (response.ok) {
      successMessage.value = data.mensaje || 'Actividad realizada registrada correctamente.'
      errorMessage.value = ''
      await cargarActividadesRealizadas()
    } else {
      errorMessage.value = data.detail || data.error || 'Error al registrar la actividad.'
    }
  } catch (err) {
    errorMessage.value = 'Error de red o del servidor.'
  }
}
</script>

<style scoped>

</style>
