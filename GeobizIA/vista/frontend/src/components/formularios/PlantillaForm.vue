<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Plantilla</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="titulo">Título:</label>
                    <input type="text" id="titulo" v-model="formData.titulo" required>
                </div>
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <input type="text" id="tipo" v-model="formData.tipo" required>
                </div>
                <div class="form-group">
                    <label for="contenido_base">Contenido Base:</label>
                    <textarea id="contenido_base" v-model="formData.contenido_base" required></textarea>
                </div>
                <div class="form-group">
                    <label for="fecha_creacion">Fecha de Creación:</label>
                    <input type="text" id="fecha_creacion" v-model="formData.fecha_creacion" required>
                </div>
                <div class="form-group">
                    <label for="ultima_modificacion">Última Modificación:</label>
                    <input type="text" id="ultima_modificacion" v-model="formData.ultima_modificacion" required>
                </div>
                <div class="form-group">
                    <label for="relaciones">Relaciones:</label>
                    <input type="text" id="relaciones" v-model="formData.relaciones">
                </div>
                <div class="center">
                    <button type="submit">Guardar Plantilla</button>
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
    tipo: '',
    contenido_base: '',
    fecha_creacion: '',
    ultima_modificacion: '',
    relaciones: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Plantilla guardada correctamente.';
    errorMessage.value = '';
}
</script>
