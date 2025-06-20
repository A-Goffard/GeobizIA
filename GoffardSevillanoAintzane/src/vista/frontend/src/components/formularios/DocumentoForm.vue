<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Documento</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="titulo">Título:</label>
                    <input type="text" id="titulo" v-model="formData.titulo" required>
                </div>
                <div class="form-group">
                    <label for="descripcion">Descripción:</label>
                    <textarea id="descripcion" v-model="formData.descripcion" required></textarea>
                </div>
                <div class="form-group">
                    <label for="fecha_subida">Fecha de Subida:</label>
                    <input type="text" id="fecha_subida" v-model="formData.fecha_subida" required>
                </div>
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <input type="text" id="tipo" v-model="formData.tipo" required>
                </div>
                <div class="form-group">
                    <label for="tematica">Temática:</label>
                    <input type="text" id="tematica" v-model="formData.tematica" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Documento</button>
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
    titulo: '',
    descripcion: '',
    fecha_subida: '',
    tipo: '',
    tematica: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Documento guardado correctamente.';
    errorMessage.value = '';
}
</script>
