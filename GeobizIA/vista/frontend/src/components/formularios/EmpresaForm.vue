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

async function submitForm() {
    successMessage.value = '';
    errorMessage.value = '';
    
    try {
        const response = await fetch('http://localhost:8000/api/empresas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData.value)
        });
        
        const data = await response.json();
        
        if (response.ok) {
            successMessage.value = data.mensaje || 'Empresa guardada correctamente.';
            errorMessage.value = '';
            
            // Limpiar formulario
            formData.value = {
                nombre: '',
                sector: '',
                logo: '',
                ubicacion: ''
            };
        } else {
            errorMessage.value = data.detail || 'Error al guardar la empresa.';
            successMessage.value = '';
        }
    } catch (error) {
        errorMessage.value = 'Error de conexión. Intente nuevamente.';
        successMessage.value = '';
        console.error('Error:', error);
    }
}
</script>
