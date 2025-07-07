<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Tag</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="palabra_clave">Palabra Clave:</label>
                    <input type="text" id="palabra_clave" v-model="formData.palabra_clave" required>
                </div>
                <div class="form-group">
                    <label for="categoria">Categoría:</label>
                    <input type="text" id="categoria" v-model="formData.categoria" required>
                </div>
                <div class="form-group">
                    <label for="frecuencia_uso">Frecuencia de Uso:</label>
                    <input type="number" id="frecuencia_uso" v-model="formData.frecuencia_uso" required>
                </div>
                <div class="form-group">
                    <label for="relaciones">Relaciones:</label>
                    <input type="text" id="relaciones" v-model="formData.relaciones">
                </div>
                <div class="center">
                    <button type="submit">Guardar Tag</button>
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
    palabra_clave: '',
    categoria: '',
    frecuencia_uso: '',
    relaciones: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Tag guardado correctamente.';
    errorMessage.value = '';
}
</script>
