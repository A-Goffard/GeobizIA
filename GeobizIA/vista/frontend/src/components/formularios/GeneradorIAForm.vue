<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Generador IA</h1>
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
                    <label for="empresa_id">ID Empresa:</label>
                    <input type="number" id="empresa_id" v-model="formData.empresa_id" required>
                </div>
                <div class="form-group">
                    <label for="configuraciones">Configuraciones:</label>
                    <textarea id="configuraciones" v-model="formData.configuraciones"></textarea>
                </div>
                <div class="form-group">
                    <label for="ejemplos_estilo">Ejemplos de Estilo:</label>
                    <textarea id="ejemplos_estilo" v-model="formData.ejemplos_estilo"></textarea>
                </div>
                <div class="form-group">
                    <label for="ultima_generacion">Última Generación:</label>
                    <input type="text" id="ultima_generacion" v-model="formData.ultima_generacion">
                </div>
                <div class="center">
                    <button type="submit">Guardar Generador IA</button>
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
    empresa_id: '',
    configuraciones: '',
    ejemplos_estilo: '',
    ultima_generacion: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Generador IA guardado correctamente.';
    errorMessage.value = '';
}
</script>
