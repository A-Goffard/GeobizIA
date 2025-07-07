<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Usuario</h1>
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
                    <label for="fecha_nacimiento">Fecha de Nacimiento:</label>
                    <input type="text" id="fecha_nacimiento" v-model="formData.fecha_nacimiento" required>
                </div>
                <div class="form-group">
                    <label for="direccion">Dirección:</label>
                    <input type="text" id="direccion" v-model="formData.direccion" required>
                </div>
                <div class="form-group">
                    <label for="dni">DNI:</label>
                    <input type="text" id="dni" v-model="formData.dni" required>
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
                    <label for="rol">Rol:</label>
                    <input type="text" id="rol" v-model="formData.rol" required>
                </div>
                <div class="form-group">
                    <label for="preferencias">Preferencias:</label>
                    <input type="text" id="preferencias" v-model="formData.preferencias">
                </div>
                <div class="form-group">
                    <label for="password">Contraseña:</label>
                    <input type="password" id="password" v-model="formData.password" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Usuario</button>
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
    fecha_nacimiento: '',
    direccion: '',
    dni: '',
    cp: '',
    poblacion: '',
    pais: '',
    rol: '',
    preferencias: '',
    password: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Usuario guardado correctamente.';
    errorMessage.value = '';
}
</script>
