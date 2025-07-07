<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Recurso Multimedia</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <input type="text" id="tipo" v-model="formData.tipo" required>
                </div>
                <div class="form-group">
                    <label for="titulo">Título:</label>
                    <input type="text" id="titulo" v-model="formData.titulo" required>
                </div>
                <div class="form-group">
                    <label for="fecha_subida">Fecha de Subida:</label>
                    <input type="text" id="fecha_subida" v-model="formData.fecha_subida" required>
                </div>
                <div class="form-group">
                    <label for="autor">Autor:</label>
                    <input type="text" id="autor" v-model="formData.autor" required>
                </div>
                <div class="form-group">
                    <label for="relaciones">Relaciones:</label>
                    <input type="text" id="relaciones" v-model="formData.relaciones">
                </div>
                <div class="center">
                    <button type="submit">Guardar Recurso Multimedia</button>
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
    tipo: '',
    titulo: '',
    fecha_subida: '',
    autor: '',
    relaciones: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Recurso multimedia guardado correctamente.';
    errorMessage.value = '';
}
</script>
