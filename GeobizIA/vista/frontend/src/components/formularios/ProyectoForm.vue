<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Proyecto</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre" required>
                </div>
                <div class="form-group">
                    <label for="descripcion">Descripción:</label>
                    <textarea id="descripcion" v-model="formData.descripcion" required></textarea>
                </div>
                <div class="form-group">
                    <label for="fecha_inicio">Fecha de Inicio:</label>
                    <input type="date" id="fecha_inicio" v-model="formData.fecha_inicio">
                </div>
                <div class="form-group">
                    <label for="fecha_fin">Fecha de Fin:</label>
                    <input type="date" id="fecha_fin" v-model="formData.fecha_fin">
                </div>
                <div class="form-group">
                    <label for="poblacion">Población:</label>
                    <input type="text" id="poblacion" v-model="formData.poblacion">
                </div>
                <div class="form-group">
                    <label for="responsable">Responsable:</label>
                    <input type="text" id="responsable" v-model="formData.responsable">
                </div>
                <div class="form-group">
                    <label for="estado">Estado:</label>
                    <select id="estado" v-model="formData.estado" required>
                        <option value="">Seleccionar estado</option>
                        <option value="PLANIFICACION">Planificación</option>
                        <option value="EN_PROGRESO">En Progreso</option>
                        <option value="PAUSADO">Pausado</option>
                        <option value="COMPLETADO">Completado</option>
                        <option value="CANCELADO">Cancelado</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="objetivos">Objetivos:</label>
                    <textarea id="objetivos" v-model="formData.objetivos"></textarea>
                </div>
                <div class="form-group">
                    <label for="presupuesto">Presupuesto:</label>
                    <input type="number" step="0.01" id="presupuesto" v-model="formData.presupuesto">
                </div>
                <div class="center">
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Guardando...' : 'Guardar Proyecto' }}
                    </button>
                </div>
                <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const formData = ref({
    nombre: '',
    descripcion: '',
    fecha_inicio: '',
    fecha_fin: '',
    poblacion: '',
    responsable: '',
    estado: '',
    objetivos: '',
    presupuesto: ''
});

const successMessage = ref('');
const errorMessage = ref('');
const isSubmitting = ref(false);

async function submitForm() {
    isSubmitting.value = true;
    successMessage.value = '';
    errorMessage.value = '';

    try {
        const response = await fetch('http://localhost:8000/api/proyectos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData.value),
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || 'Error al guardar el proyecto.');
        }

        successMessage.value = result.mensaje || 'Proyecto guardado correctamente.';
        // Resetear el formulario
        formData.value = {
            nombre: '',
            descripcion: '',
            fecha_inicio: '',
            fecha_fin: '',
            poblacion: '',
            responsable: '',
            estado: '',
            objetivos: '',
            presupuesto: ''
        };

    } catch (error) {
        errorMessage.value = error.message;
    } finally {
        isSubmitting.value = false;
    }
}
</script>
