<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Publicación</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="titulo">Título:</label>
                    <input type="text" id="titulo" v-model="formData.titulo" required>
                </div>
                <div class="form-group">
                    <label for="contenido">Contenido:</label>
                    <textarea id="contenido" v-model="formData.contenido" required></textarea>
                </div>
                <div class="form-group">
                    <label for="autor">Autor:</label>
                    <input type="text" id="autor" v-model="formData.autor" required>
                </div>
                <div class="form-group">
                    <label for="fecha_creacion">Fecha de Creación:</label>
                    <input type="text" id="fecha_creacion" v-model="formData.fecha_creacion" required>
                </div>
                <div class="form-group">
                    <label for="estado">Estado:</label>
                    <input type="text" id="estado" v-model="formData.estado" required>
                </div>
                <div class="form-group">
                    <label for="tags">Tags:</label>
                    <input type="text" id="tags" v-model="formData.tags">
                </div>
                <div class="form-group">
                    <label for="palabras_clave">Palabras Clave:</label>
                    <input type="text" id="palabras_clave" v-model="formData.palabras_clave">
                </div>
                <div class="form-group">
                    <label for="generada_por_ia">Generada por IA:</label>
                    <input type="checkbox" id="generada_por_ia" v-model="formData.generada_por_ia">
                </div>
                <div class="form-group">
                    <label for="id_generador_ia">ID Generador IA:</label>
                    <input type="number" id="id_generador_ia" v-model="formData.id_generador_ia">
                </div>
                <div class="form-group">
                    <label for="feedback_empresa">Feedback Empresa:</label>
                    <textarea id="feedback_empresa" v-model="formData.feedback_empresa"></textarea>
                </div>
                <div class="center">
                    <button type="submit">Guardar Publicación</button>
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
    contenido: '',
    autor: '',
    fecha_creacion: '',
    estado: '',
    tags: '',
    palabras_clave: '',
    generada_por_ia: false,
    id_generador_ia: '',
    feedback_empresa: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Publicación guardada correctamente.';
    errorMessage.value = '';
}
</script>
