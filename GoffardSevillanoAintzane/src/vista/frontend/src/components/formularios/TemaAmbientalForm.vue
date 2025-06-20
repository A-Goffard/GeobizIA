<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Tema Ambiental</h1>
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
                    <label for="relevancia">Relevancia:</label>
                    <input type="text" id="relevancia" v-model="formData.relevancia" required>
                </div>
                <div class="form-group">
                    <label for="relacion_actividades">Relación Actividades:</label>
                    <input type="text" id="relacion_actividades" v-model="formData.relacion_actividades">
                </div>
                <div class="form-group">
                    <label for="relacion_publicaciones">Relación Publicaciones:</label>
                    <input type="text" id="relacion_publicaciones" v-model="formData.relacion_publicaciones">
                </div>
                <div class="center">
                    <button type="submit">Guardar Tema Ambiental</button>
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
    relevancia: '',
    relacion_actividades: '',
    relacion_publicaciones: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Tema ambiental guardado correctamente.';
    errorMessage.value = '';
}
</script>
