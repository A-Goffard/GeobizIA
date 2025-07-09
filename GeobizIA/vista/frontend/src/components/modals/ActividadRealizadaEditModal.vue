<template>
    <div class="modal-backdrop" @click.self="$emit('close')">
        <div class="modal-content">
            <button class="close-button" @click="$emit('close')">&times;</button>
            <h3>Editar Registro de Actividad</h3>
            
            <!-- Formulario de Edición -->
            <form @submit.prevent="actualizar">
                <div class="form-group">
                    <label>Fecha:</label>
                    <input type="date" v-model="formData.fecha" required>
                </div>
                <div class="form-group">
                    <label>Asistentes:</label>
                    <input type="number" v-model.number="formData.asistentes">
                </div>
                <div class="form-group">
                    <label>Coste Económico (€):</label>
                    <input type="number" step="0.01" v-model.number="formData.coste_economico">
                </div>
                <div class="form-group">
                    <label>Facturación (€):</label>
                    <input type="number" step="0.01" v-model.number="formData.facturacion">
                </div>
                <div class="form-group">
                    <label>Observaciones:</label>
                    <textarea v-model="formData.observaciones"></textarea>
                </div>
                <button type="submit" :disabled="isSubmitting">
                    {{ isSubmitting ? 'Guardando...' : 'Guardar Cambios' }}
                </button>
                <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
            </form>

            <!-- Zona de Peligro -->
            <div class="danger-zone">
                <h4>Eliminar Registro</h4>
                <div class="delete-confirmation">
                    <input type="checkbox" v-model="confirmDelete">
                    <label>Confirmar eliminación de este registro.</label>
                </div>
                <button @click="eliminar" :disabled="!confirmDelete || isDeleting" class="delete-button">
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar' }}
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
    actividadRealizada: {
        type: Object,
        required: true
    }
});

const emit = defineEmits(['close', 'updated', 'deleted']);

const formData = ref({});
const isSubmitting = ref(false);
const isDeleting = ref(false);
const confirmDelete = ref(false);
const successMessage = ref('');
const errorMessage = ref('');

// Clonar el prop a un estado local para poder editarlo
watch(() => props.actividadRealizada, (newVal) => {
    formData.value = { ...newVal };
}, { immediate: true });

async function actualizar() {
    isSubmitting.value = true;
    errorMessage.value = '';
    successMessage.value = '';
    try {
        const response = await fetch(`http://localhost:8000/api/actividades_realizadas/${formData.value.id_actividad_realizada}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData.value)
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al actualizar.');
        successMessage.value = result.mensaje;
        emit('updated', { ...formData.value });
    } catch (e) {
        errorMessage.value = e.message;
    } finally {
        isSubmitting.value = false;
    }
}

async function eliminar() {
    if (!confirmDelete.value) return;
    isDeleting.value = true;
    errorMessage.value = '';
    try {
        const response = await fetch(`http://localhost:8000/api/actividades_realizadas/${formData.value.id_actividad_realizada}`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            const result = await response.json();
            throw new Error(result.detail || 'Error al eliminar.');
        }
        emit('deleted', formData.value.id_actividad_realizada);
        emit('close');
    } catch (e) {
        errorMessage.value = e.message;
    } finally {
        isDeleting.value = false;
    }
}
</script>

<style scoped>
.modal-backdrop { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center; z-index: 1000; }
.modal-content { background: white; padding: 2rem; border-radius: 8px; width: 90%; max-width: 500px; position: relative; }
.close-button { position: absolute; top: 10px; right: 10px; background: none; border: none; font-size: 1.5rem; cursor: pointer; }
.form-group { margin-bottom: 1rem; }
label { display: block; margin-bottom: 0.5rem; }
input, textarea { width: 100%; padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px; }
button { padding: 0.7rem 1rem; border: none; border-radius: 4px; color: white; background-color: var(--green); cursor: pointer; }
button:disabled { background-color: #ccc; }
.danger-zone { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; }
.delete-button { background-color: #e74c3c; }
.delete-button:disabled { background-color: #f5b7b1; }
.success-message { color: green; }
.error-message { color: red; }
</style>
