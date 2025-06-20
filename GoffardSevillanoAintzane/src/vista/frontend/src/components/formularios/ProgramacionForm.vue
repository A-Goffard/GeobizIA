<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Programación</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="publicacion_id">ID Publicación:</label>
                    <input type="number" id="publicacion_id" v-model="formData.publicacion_id" required>
                </div>
                <div class="form-group">
                    <label for="red_social_id">ID Red Social:</label>
                    <input type="number" id="red_social_id" v-model="formData.red_social_id" required>
                </div>
                <div class="form-group">
                    <label for="fecha_programada">Fecha Programada:</label>
                    <input type="text" id="fecha_programada" v-model="formData.fecha_programada" required>
                </div>
                <div class="form-group">
                    <label for="estado">Estado:</label>
                    <input type="text" id="estado" v-model="formData.estado" required>
                </div>
                <div class="form-group">
                    <label for="notificaciones">Notificaciones:</label>
                    <input type="text" id="notificaciones" v-model="formData.notificaciones">
                </div>
                <div class="form-group">
                    <label for="responsable">Responsable:</label>
                    <input type="text" id="responsable" v-model="formData.responsable" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Programación</button>
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
    publicacion_id: '',
    red_social_id: '',
    fecha_programada: '',
    estado: '',
    notificaciones: '',
    responsable: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Programación guardada correctamente.';
    errorMessage.value = '';
}
</script>
