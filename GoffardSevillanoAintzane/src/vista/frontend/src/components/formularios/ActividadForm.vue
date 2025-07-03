<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Actividad</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label>Tipo:</label>
                    <input v-model="formData.tipo" required />
                </div>
                <div class="form-group">
                    <label>Nombre:</label>
                    <input v-model="formData.nombre" required />
                </div>
                <div class="form-group">
                    <label>Descripción:</label>
                    <input v-model="formData.descripcion" required />
                </div>
                <div class="form-group">
                    <label>Responsable:</label>
                    <input v-model="formData.responsable" required />
                </div>
                <div class="form-group">
                    <label>Duración:</label>
                    <input v-model="formData.duracion" required />
                </div>
                <div class="form-group">
                    <label>Coste Económico:</label>
                    <input v-model.number="formData.coste_economico" type="number" required />
                </div>
                <div class="form-group">
                    <label>Coste Horas:</label>
                    <input v-model.number="formData.coste_horas" type="number" required />
                </div>
                <div class="form-group">
                    <label>Facturación:</label>
                    <input v-model.number="formData.facturacion" type="number" required />
                </div>
                <div class="form-group">
                    <label>Resultados:</label>
                    <input v-model="formData.resultados" />
                </div>
                <div class="form-group">
                    <label>Valoración:</label>
                    <input v-model="formData.valoracion" />
                </div>
                <div class="form-group">
                    <label>Observaciones:</label>
                    <input v-model="formData.observaciones" />
                </div>
                <div class="form-group">
                    <label>ID Actividad:</label>
                    <input v-model.number="formData.id_actividad" type="number" required />
                </div>
                <button type="submit">Guardar</button>
            </form>
            <div v-if="successMessage" style="color:green;">{{ successMessage }}</div>
            <div v-if="errorMessage" style="color:red;">{{ errorMessage }}</div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const formData = ref({
    id_actividad: '',
    tipo: '',
    nombre: '',
    descripcion: '',
    responsable: '',
    duracion: '',
    coste_economico: '',
    coste_horas: '',
    facturacion: '',
    resultados: '',
    valoracion: '',
    observaciones: ''
})

const successMessage = ref('')
const errorMessage = ref('')

async function submitForm() {
    successMessage.value = ''
    errorMessage.value = ''
    try {
        const response = await fetch('http://localhost:8000/api/api_actividades', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData.value)
        })
        const data = await response.json()
        if (response.ok) {
            successMessage.value = data.mensaje || 'Actividad guardada correctamente.'
            errorMessage.value = ''
        } else {
            errorMessage.value = data.detail || data.error || 'Error al guardar actividad.'
        }
    } catch (err) {
        errorMessage.value = 'Error de red o servidor.'
    }
}
</script>
