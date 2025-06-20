<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Participante</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre" required>
                </div>
                <div class="form-group">
                    <label for="apellido">Apellido:</label>
                    <input type="text" id="apellido" v-model="formData.apellido" required>
                </div>
                <div class="form-group">
                    <label for="email">Correo Electrónico:</label>
                    <input type="email" id="email" v-model="formData.email" required>
                </div>
                <div class="form-group">
                    <label for="telefono">Teléfono:</label>
                    <input type="tel" id="telefono" v-model="formData.telefono" required>
                </div>
                <div class="form-group">
                    <label for="numero_personas_juntas">Nº Personas Juntas:</label>
                    <input type="number" id="numero_personas_juntas" v-model="formData.numero_personas_juntas" required>
                </div>
                <div class="form-group">
                    <label for="rol">Rol:</label>
                    <input type="text" id="rol" v-model="formData.rol" required>
                </div>
                <div class="form-group">
                    <label for="como_conocer">¿Cómo conoció?:</label>
                    <input type="text" id="como_conocer" v-model="formData.como_conocer" required>
                </div>
                <div class="form-group">
                    <label for="actividad_id">ID Actividad:</label>
                    <input type="number" id="actividad_id" v-model="formData.actividad_id" required>
                </div>
                <div class="form-group">
                    <label for="fecha_registro">Fecha de Registro:</label>
                    <input type="text" id="fecha_registro" v-model="formData.fecha_registro" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Participante</button>
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
    apellido: '',
    email: '',
    telefono: '',
    numero_personas_juntas: '',
    rol: '',
    como_conocer: '',
    actividad_id: '',
    fecha_registro: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Participante guardado correctamente.';
    errorMessage.value = '';
}
</script>
