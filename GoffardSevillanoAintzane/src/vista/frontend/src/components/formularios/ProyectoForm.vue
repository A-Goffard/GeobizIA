<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Proyecto</h1>
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
                    <label for="fecha_inicio">Fecha de Inicio:</label>
                    <input type="text" id="fecha_inicio" v-model="formData.fecha_inicio" required>
                </div>
                <div class="form-group">
                    <label for="fecha_fin">Fecha de Fin:</label>
                    <input type="text" id="fecha_fin" v-model="formData.fecha_fin" required>
                </div>
                <div class="form-group">
                    <label for="poblacion">Población:</label>
                    <input type="text" id="poblacion" v-model="formData.poblacion" required>
                </div>
                <div class="form-group">
                    <label for="responsable">Responsable:</label>
                    <input type="text" id="responsable" v-model="formData.responsable" required>
                </div>
                <div class="form-group">
                    <label for="estado">Estado:</label>
                    <input type="text" id="estado" v-model="formData.estado" required>
                </div>
                <div class="form-group">
                    <label for="objetivos">Objetivos:</label>
                    <textarea id="objetivos" v-model="formData.objetivos"></textarea>
                </div>
                <div class="form-group">
                    <label for="presupuesto">Presupuesto:</label>
                    <input type="number" step="any" id="presupuesto" v-model="formData.presupuesto" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Proyecto</button>
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
    fecha_inicio: '',
    fecha_fin: '',
    poblacion: '',
    responsable: '',
    estado: '',
    objetivos: '',
    presupuesto: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Proyecto guardado correctamente.';
    errorMessage.value = '';
}
</script>
