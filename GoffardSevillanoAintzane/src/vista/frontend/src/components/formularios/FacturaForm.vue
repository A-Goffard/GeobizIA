<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>Crear Factura</h1>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="id_cliente">ID Cliente:</label>
                    <input type="number" id="id_cliente" v-model="formData.id_cliente" required>
                </div>
                <div class="form-group">
                    <label for="fecha_facturacion">Fecha Facturación:</label>
                    <input type="text" id="fecha_facturacion" v-model="formData.fecha_facturacion" required>
                </div>
                <div class="form-group">
                    <label for="fecha_vencimiento">Fecha Vencimiento:</label>
                    <input type="text" id="fecha_vencimiento" v-model="formData.fecha_vencimiento" required>
                </div>
                <div class="form-group">
                    <label for="concepto">Concepto:</label>
                    <input type="text" id="concepto" v-model="formData.concepto" required>
                </div>
                <div class="form-group">
                    <label for="responsable">Responsable:</label>
                    <input type="text" id="responsable" v-model="formData.responsable" required>
                </div>
                <div class="form-group">
                    <label for="iva">IVA:</label>
                    <input type="number" step="any" id="iva" v-model="formData.iva" required>
                </div>
                <div class="form-group">
                    <label for="coste_total">Coste Total:</label>
                    <input type="number" step="any" id="coste_total" v-model="formData.coste_total" required>
                </div>
                <div class="form-group">
                    <label for="base_imponible">Base Imponible:</label>
                    <input type="number" step="any" id="base_imponible" v-model="formData.base_imponible" required>
                </div>
                <div class="form-group">
                    <label for="numero_factura">Número Factura:</label>
                    <input type="text" id="numero_factura" v-model="formData.numero_factura" required>
                </div>
                <div class="form-group">
                    <label for="tipo_pago">Tipo de Pago:</label>
                    <input type="text" id="tipo_pago" v-model="formData.tipo_pago" required>
                </div>
                <div class="form-group">
                    <label for="irpf">IRPF:</label>
                    <input type="number" step="any" id="irpf" v-model="formData.irpf" required>
                </div>
                <div class="center">
                    <button type="submit">Guardar Factura</button>
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
    id_cliente: '',
    fecha_facturacion: '',
    fecha_vencimiento: '',
    concepto: '',
    responsable: '',
    iva: '',
    coste_total: '',
    base_imponible: '',
    numero_factura: '',
    tipo_pago: '',
    irpf: ''
});

const successMessage = ref('');
const errorMessage = ref('');

function submitForm() {
    successMessage.value = 'Factura guardada correctamente.';
    errorMessage.value = '';
}
</script>
