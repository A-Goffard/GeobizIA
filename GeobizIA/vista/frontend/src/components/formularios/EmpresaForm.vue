<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Empresa</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre" required>
                </div>
                <div class="form-group">
                    <label for="sector">Sector:</label>
                    <input type="text" id="sector" v-model="formData.sector" required>
                </div>
                <div class="form-group">
                    <label for="logo">Logo (URL):</label>
                    <input type="text" id="logo" v-model="formData.logo">
                </div>
                <div class="form-group">
                    <label for="ubicacion">Ubicación:</label>
                    <input type="text" id="ubicacion" v-model="formData.ubicacion" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Empresa</button>
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
    sector: '',
    logo: '',
    ubicacion: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    // Aquí iría la lógica para enviar los datos al backend
    // Simulación de éxito:
    successMessage.value = 'Empresa guardada correctamente.';
    errorMessage.value = '';
    // Limpiar formulario si quieres:
    // formData.value = { id_empresa: '', nombre: '', sector: '', logo: '', ubicacion: '' };
}
</script>
