<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Actividad</h1>
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
                    <label for="descripcion">Descripción:</label>
                    <textarea id="descripcion" v-model="formData.descripcion" required></textarea>
                </div>
                <div class="form-group">
                    <label for="responsable">Responsable:</label>
                    <input type="text" id="responsable" v-model="formData.responsable" required>
                </div>
                <div class="form-group">
                    <label for="duracion">Duración:</label>
                    <input type="text" id="duracion" v-model="formData.duracion" required>
                </div>
                <div class="form-group">
                    <label for="coste_economico">Coste Económico:</label>
                    <input type="number" step="any" id="coste_economico" v-model="formData.coste_economico" required>
                </div>
                <div class="form-group">
                    <label for="coste_horas">Coste Horas:</label>
                    <input type="number" step="any" id="coste_horas" v-model="formData.coste_horas" required>
                </div>
                <div class="form-group">
                    <label for="facturacion">Facturación:</label>
                    <input type="number" step="any" id="facturacion" v-model="formData.facturacion" required>
                </div>
                <div class="form-group">
                    <label for="resultados">Resultados:</label>
                    <textarea id="resultados" v-model="formData.resultados"></textarea>
                </div>
                <div class="form-group">
                    <label for="valoracion">Valoración:</label>
                    <textarea id="valoracion" v-model="formData.valoracion"></textarea>
                </div>
                <div class="form-group">
                    <label for="observaciones">Observaciones:</label>
                    <textarea id="observaciones" v-model="formData.observaciones"></textarea>
                </div>
                <div class="center">
                    <button type="submit">Guardar Actividad</button>
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
    descripcion: '',
    responsable: '',
    duracion: '',
    coste_economico: '',
    coste_horas: '',
    facturacion: '',
    resultados: '',
    valoracion: '',
    observaciones: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Actividad guardada correctamente.';
    errorMessage.value = '';
}
</script>
