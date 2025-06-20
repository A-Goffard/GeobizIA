<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Cliente</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <input type="text" id="tipo" v-model="formData.tipo" required>
                </div>
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre" required>
                </div>
                <div class="form-group">
                    <label for="apellido">Apellido:</label>
                    <input type="text" id="apellido" v-model="formData.apellido" required>
                </div>
                <div class="form-group">
                    <label for="razon_social">Razón Social:</label>
                    <input type="text" id="razon_social" v-model="formData.razon_social">
                </div>
                <div class="form-group">
                    <label for="nif">NIF:</label>
                    <input type="text" id="nif" v-model="formData.nif">
                </div>
                <div class="form-group">
                    <label for="dni">DNI:</label>
                    <input type="text" id="dni" v-model="formData.dni">
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
                    <label for="direccion">Dirección:</label>
                    <input type="text" id="direccion" v-model="formData.direccion" required>
                </div>
                <div class="form-group">
                    <label for="cp">Código Postal:</label>
                    <input type="text" id="cp" v-model="formData.cp" required>
                </div>
                <div class="form-group">
                    <label for="poblacion">Población:</label>
                    <input type="text" id="poblacion" v-model="formData.poblacion" required>
                </div>
                <div class="form-group">
                    <label for="pais">País:</label>
                    <input type="text" id="pais" v-model="formData.pais" required>
                </div>
                <div class="form-group">
                    <label for="fecha_registro">Fecha de Registro:</label>
                    <input type="text" id="fecha_registro" v-model="formData.fecha_registro" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Cliente</button>
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
    nombre: '',
    apellido: '',
    razon_social: '',
    nif: '',
    dni: '',
    email: '',
    telefono: '',
    direccion: '',
    cp: '',
    poblacion: '',
    pais: '',
    fecha_registro: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Cliente guardado correctamente.';
    errorMessage.value = '';
}
</script>
