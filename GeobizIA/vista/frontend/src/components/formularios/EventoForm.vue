<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Evento</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre" required>
                </div>
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <input type="text" id="tipo" v-model="formData.tipo" required>
                </div>
                <div class="form-group">
                    <label for="lugar">Lugar:</label>
                    <input type="text" id="lugar" v-model="formData.lugar" required>
                </div>
                <div class="form-group">
                    <label for="fecha_comienzo">Fecha de Comienzo:</label>
                    <input type="date" id="fecha_comienzo" v-model="formData.fecha_comienzo" required>
                </div>
                <div class="form-group">
                    <label for="fecha_final">Fecha de Finalización:</label>
                    <input type="date" id="fecha_final" v-model="formData.fecha_final" required>
                </div>
                <div class="form-group">
                    <label for="poblacion">Población:</label>
                    <input type="text" id="poblacion" v-model="formData.poblacion" required>
                </div>
                <div class="form-group">
                    <label for="tematica">Temática:</label>
                    <input type="text" id="tematica" v-model="formData.tematica" required>
                </div>
                <div class="center">
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Guardando...' : 'Guardar Evento' }}
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
    tipo: '',
    lugar: '',
    fecha_comienzo: '',
    fecha_final: '',
    poblacion: '',
    tematica: ''
});

const successMessage = ref('');
const errorMessage = ref('');
const isSubmitting = ref(false);

async function submitForm() {
    isSubmitting.value = true;
    successMessage.value = '';
    errorMessage.value = '';

    try {
        const response = await fetch('http://localhost:8000/api/eventos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData.value),
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || 'Error al guardar el evento.');
        }

        successMessage.value = result.mensaje || 'Evento guardado correctamente.';
        // Opcional: resetear el formulario
        formData.value = {
            nombre: '',
            tipo: '',
            lugar: '',
            fecha_comienzo: '',
            fecha_final: '',
            poblacion: '',
            tematica: ''
        };

    } catch (error) {
        errorMessage.value = error.message;
    } finally {
        isSubmitting.value = false;
    }
}
</script>
