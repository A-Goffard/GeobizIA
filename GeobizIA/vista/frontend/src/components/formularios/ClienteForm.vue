<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Cliente</h1>
            <form @submit.prevent="submitForm">
                <!-- Datos personales -->
                <h3>Datos de la Persona</h3>
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="formData.nombre">
                </div>
                <div class="form-group">
                    <label for="apellido">Apellido:</label>
                    <input type="text" id="apellido" v-model="formData.apellido">
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" v-model="formData.email">
                </div>
                <div class="form-group">
                    <label for="telefono">Teléfono:</label>
                    <input type="tel" id="telefono" v-model="formData.telefono">
                </div>
                <div class="form-group">
                    <label for="dni">DNI:</label>
                    <input type="text" id="dni" v-model="formData.dni">
                </div>
                <div class="form-group">
                    <label for="direccion">Dirección:</label>
                    <input type="text" id="direccion" v-model="formData.direccion">
                </div>
                <div class="form-group">
                    <label for="cp">Código Postal:</label>
                    <input type="text" id="cp" v-model="formData.cp">
                </div>
                <div class="form-group">
                    <label for="poblacion">Población:</label>
                    <input type="text" id="poblacion" v-model="formData.poblacion">
                </div>
                <div class="form-group">
                    <label for="pais">País:</label>
                    <input type="text" id="pais" v-model="formData.pais">
                </div>
                
                <!-- Datos específicos del cliente -->
                <h3>Datos del Cliente</h3>
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <select id="tipo" v-model="formData.tipo">
                        <option value="">Seleccionar tipo</option>
                        <option value="EMPRESA">Empresa</option>
                        <option value="AUTONOMO">Autónomo</option>
                        <option value="PARTICULAR">Particular</option>
                        <option value="ENTIDAD">Entidad</option>
                    </select>
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
                    <label for="fecha_registro">Fecha de Registro:</label>
                    <input type="date" id="fecha_registro" v-model="formData.fecha_registro">
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
    // Datos de la persona
    nombre: '',
    apellido: '',
    email: '',
    telefono: '',
    dni: '',
    direccion: '',
    cp: '',
    poblacion: '',
    pais: '',
    // Datos específicos del cliente
    tipo: '',
    razon_social: '',
    nif: '',
    fecha_registro: ''
});

const successMessage = ref('');
const errorMessage = ref('');

async function submitForm() {
    successMessage.value = '';
    errorMessage.value = '';
    try {
        const response = await fetch('http://localhost:8000/api/clientes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData.value)
        });
        const data = await response.json();
        if (response.ok) {
            successMessage.value = data.mensaje || 'Cliente guardado correctamente.';
            errorMessage.value = '';
            // Resetear formulario
            formData.value = {
                nombre: '',
                apellido: '',
                email: '',
                telefono: '',
                dni: '',
                direccion: '',
                cp: '',
                poblacion: '',
                pais: '',
                tipo: '',
                razon_social: '',
                nif: '',
                fecha_registro: ''
            };
        } else {
            errorMessage.value = data.detail || data.error || 'Error al guardar cliente.';
        }
    } catch (err) {
        errorMessage.value = 'Error de red o servidor.';
    }
}
</script>
