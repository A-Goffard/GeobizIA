<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Red Social</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="plataforma">Plataforma:</label>
                    <input type="text" id="plataforma" v-model="formData.plataforma" required>
                </div>
                <div class="form-group">
                    <label for="nombre_cuenta">Nombre de la Cuenta:</label>
                    <input type="text" id="nombre_cuenta" v-model="formData.nombre_cuenta" required>
                </div>
                <div class="form-group">
                    <label for="credenciales">Credenciales:</label>
                    <input type="text" id="credenciales" v-model="formData.credenciales">
                </div>
                <div class="form-group">
                    <label for="preferencias_publicacion">Preferencias de Publicación:</label>
                    <input type="text" id="preferencias_publicacion" v-model="formData.preferencias_publicacion">
                </div>
                <div class="form-group">
                    <label for="estado_conexion">Estado de Conexión:</label>
                    <input type="text" id="estado_conexion" v-model="formData.estado_conexion">
                </div>
                <div class="form-group">
                    <label for="ultima_publicacion">Última Publicación:</label>
                    <input type="text" id="ultima_publicacion" v-model="formData.ultima_publicacion">
                </div>
                <div class="center">
                    <button type="submit">Guardar Red Social</button>
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
    plataforma: '',
    nombre_cuenta: '',
    credenciales: '',
    preferencias_publicacion: '',
    estado_conexion: '',
    ultima_publicacion: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Red social guardada correctamente.';
    errorMessage.value = '';
}
</script>
